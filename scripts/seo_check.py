#!/usr/bin/env python3
"""
BurnCloud SEO Quality Check Task
每周三早上10点执行 - 页面质量检查
"""

import json
import os
import re
from datetime import datetime
from pathlib import Path
from html.parser import HTMLParser

BASE_DIR = Path("/home/hermes/www.burncloud.com")
REPORTS_DIR = BASE_DIR / "reports"

class SEOChecker(HTMLParser):
    """HTML SEO 检查器"""
    
    def __init__(self):
        super().__init__()
        self.checks = {
            "has_title": False,
            "title_length": 0,
            "has_meta_description": False,
            "meta_desc_length": 0,
            "has_canonical": False,
            "canonical_no_html": True,
            "has_h1": False,
            "h1_count": 0,
            "h2_count": 0,
            "has_schema": False,
            "has_breadcrumb": False,
            "internal_links": 0,
            "links_with_html_extension": []
        }
        self.current_tag = None
        self.in_head = False
        self.title_text = ""
        self.meta_desc = ""
        self.canonical_url = ""
        
    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        
        if tag == "head":
            self.in_head = True
        elif tag == "title":
            self.current_tag = "title"
            self.checks["has_title"] = True
        elif tag == "meta":
            name = attrs_dict.get("name", "")
            prop = attrs_dict.get("property", "")
            if name == "description" or prop == "og:description":
                self.current_tag = "meta_desc"
                self.checks["has_meta_description"] = True
        elif tag == "link":
            if attrs_dict.get("rel") == "canonical":
                self.checks["has_canonical"] = True
                self.canonical_url = attrs_dict.get("href", "")
                if ".html" in self.canonical_url:
                    self.checks["canonical_no_html"] = False
        elif tag == "h1":
            self.checks["has_h1"] = True
            self.checks["h1_count"] += 1
            self.current_tag = "h1"
        elif tag == "h2":
            self.checks["h2_count"] += 1
        elif tag == "script":
            script_type = attrs_dict.get("type", "")
            if "application/ld+json" in script_type:
                self.checks["has_schema"] = True
        elif tag == "a":
            href = attrs_dict.get("href", "")
            if href and not href.startswith("http") and not href.startswith("#"):
                self.checks["internal_links"] += 1
                if ".html" in href:
                    self.checks["links_with_html_extension"].append(href)
        
    def handle_endtag(self, tag):
        if tag == "head":
            self.in_head = False
        self.current_tag = None
        
    def handle_data(self, data):
        if self.current_tag == "title":
            self.title_text += data
            self.checks["title_length"] = len(self.title_text.strip())
        elif self.current_tag == "meta_desc":
            self.meta_desc += data
            self.checks["meta_desc_length"] = len(self.meta_desc.strip())


def check_page(file_path):
    """检查单个页面的 SEO 质量"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        checker = SEOChecker()
        checker.feed(content)
        
        # 额外检查
        issues = []
        
        if not checker.checks["has_title"]:
            issues.append("缺少 <title> 标签")
        elif checker.checks["title_length"] > 60:
            issues.append(f"Title 过长 ({checker.checks['title_length']} 字符)")
        
        if not checker.checks["has_meta_description"]:
            issues.append("缺少 meta description")
        
        if not checker.checks["has_canonical"]:
            issues.append("缺少 canonical URL")
        elif not checker.checks["canonical_no_html"]:
            issues.append("Canonical URL 包含 .html 后缀")
        
        if not checker.checks["has_h1"]:
            issues.append("缺少 H1 标题")
        elif checker.checks["h1_count"] > 1:
            issues.append(f"多个 H1 标题 ({checker.checks['h1_count']} 个)")
        
        if checker.checks["internal_links"] < 3:
            issues.append(f"内链不足 ({checker.checks['internal_links']} 个)")
        
        if checker.checks["links_with_html_extension"]:
            issues.append(f"内链包含 .html: {checker.checks['links_with_html_extension'][:3]}")
        
        return {
            "file": str(file_path.relative_to(BASE_DIR)),
            "issues": issues,
            "checks": checker.checks,
            "passed": len(issues) == 0
        }
    except Exception as e:
        return {
            "file": str(file_path.relative_to(BASE_DIR)),
            "issues": [f"解析错误: {str(e)}"],
            "passed": False
        }


def run_seo_check():
    """运行完整的 SEO 检查"""
    print(f"[{datetime.now().isoformat()}] 开始 SEO 质量检查...")
    
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    
    # 查找所有 HTML 文件
    html_files = list(BASE_DIR.rglob("*.html"))
    
    # 排除 template 目录
    html_files = [f for f in html_files if "template" not in str(f)]
    
    print(f"找到 {len(html_files)} 个页面待检查")
    
    results = []
    for file_path in html_files:
        result = check_page(file_path)
        results.append(result)
        
    # 统计
    passed = sum(1 for r in results if r["passed"])
    failed = len(results) - passed
    
    # 写入报告
    report_path = REPORTS_DIR / "seo-check.md"
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(f"# SEO 质量检查报告\n\n")
        f.write(f"时间: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")
        f.write(f"## 统计\n\n")
        f.write(f"- 总页面数: {len(results)}\n")
        f.write(f"- 通过: {passed}\n")
        f.write(f"- 问题: {failed}\n\n")
        
        if failed > 0:
            f.write(f"## 问题页面\n\n")
            for r in results:
                if not r["passed"]:
                    f.write(f"### {r['file']}\n\n")
                    for issue in r["issues"]:
                        f.write(f"- {issue}\n")
                    f.write("\n")
    
    print(f"✓ 检查完成: {passed} 通过, {failed} 有问题")
    print(f"报告已写入: {report_path}")
    
    return failed == 0

if __name__ == "__main__":
    run_seo_check()
