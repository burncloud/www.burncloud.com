#!/usr/bin/env python3
"""
修复 BurnCloud 网站内部链接
将模板文件名链接转换为正确的相对路径
"""

import os
import re
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

# 模板文件名到实际路径的映射
TEMPLATE_TO_PATH = {
    'BurnCloud Landing Page (Light).html': '/',
    'BurnCloud Models Hub.html': '/models/',
    'BurnCloud Pricing.html': '/pricing/',
    'BurnCloud Compare.html': '/compare/',
    'BurnCloud Security.html': '/security/',
    'BurnCloud Blog.html': '/blog/',
    'BurnCloud Docs - Quickstart.html': '/docs/quickstart/',
    'BurnCloud Docs — Quickstart.html': '/docs/quickstart/',  # em dash
    'BurnCloud Alternatives - OpenRouter.html': '/alternatives/openrouter/',
    'BurnCloud Alternatives — OpenRouter.html': '/alternatives/openrouter/',  # em dash
    'BurnCloud Blog — DeepSeek V4 API Guide.html': '/blog/deepseek-v4-api-guide/',
    'BurnCloud Blog — Cheapest LLM API.html': '/blog/cheapest-llm-api/',
    'BurnCloud Blog — Cut AI Costs.html': '/blog/cut-ai-costs/',
    'BurnCloud Compare — DeepSeek vs OpenAI.html': '/compare/deepseek-vs-openai/',
    'BurnCloud Model — DeepSeek V4 Flash.html': '/models/deepseek-v4-flash/',
    'BurnCloud Model — DeepSeek V3.html': '/models/deepseek-v3/',
}

def get_relative_path(from_file: Path, to_path: str) -> str:
    """计算从源文件到目标路径的相对路径"""
    if to_path == '/':
        # 返回根目录
        depth = len(from_file.relative_to(BASE_DIR).parts) - 1
        return '../' * depth + 'index.html' if depth > 0 else 'index.html'
    
    target = BASE_DIR / to_path.lstrip('/')
    from_dir = from_file.parent
    
    try:
        rel_path = os.path.relpath(str(target), str(from_dir))
        if rel_path.endswith('/'):
            rel_path += 'index.html'
        elif not rel_path.endswith('.html'):
            rel_path += '/index.html'
        return rel_path
    except:
        return to_path

def fix_links(content: str, file_path: Path) -> tuple:
    """修复文件中的链接"""
    changes = 0
    fixed_links = []
    
    for template_name, actual_path in TEMPLATE_TO_PATH.items():
        if template_name in content:
            relative_link = get_relative_path(file_path, actual_path)
            # 替换链接
            old_pattern = f'href="{template_name}"'
            new_pattern = f'href="{relative_link}"'
            if old_pattern in content:
                content = content.replace(old_pattern, new_pattern)
                changes += 1
                fixed_links.append(f"{template_name} -> {relative_link}")
    
    # 修复 https://burncloud.com 绝对链接
    content, abs_changes = fix_absolute_links(content, file_path)
    changes += abs_changes
    
    return content, changes, fixed_links

def fix_absolute_links(content: str, file_path: Path) -> tuple:
    """修复 https://burncloud.com 绝对链接为相对路径"""
    changes = 0
    pattern = r'href="https://burncloud\.com([^"]*)"'
    
    def replace_link(match):
        nonlocal changes
        path = match.group(1)
        if not path:
            path = '/'
        relative = get_relative_path(file_path, path)
        changes += 1
        return f'href="{relative}"'
    
    content = re.sub(pattern, replace_link, content)
    return content, changes

def main():
    print("=== BurnCloud 链接修复工具 ===\n")
    
    # 找到所有 HTML 文件
    html_files = []
    for ext in ['*.html']:
        html_files.extend(BASE_DIR.rglob(ext))
    
    # 排除模板目录
    html_files = [f for f in html_files if 'template' not in str(f)]
    
    total_changes = 0
    fixed_files = []
    
    for html_file in html_files:
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except:
            continue
        
        new_content, changes, fixed_links = fix_links(content, html_file)
        
        if changes > 0:
            total_changes += changes
            fixed_files.append((html_file.relative_to(BASE_DIR), changes, fixed_links))
            
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(new_content)
    
    print(f"✅ 扫描了 {len(html_files)} 个文件")
    print(f"✅ 修复了 {len(fixed_files)} 个文件")
    print(f"✅ 共修复 {total_changes} 个链接\n")
    
    if fixed_files:
        print("修复详情:")
        for file, count, links in fixed_files[:10]:
            print(f"  📄 {file}: {count} 个链接")

if __name__ == '__main__':
    main()
