#!/usr/bin/env python3
"""
BurnCloud Competitor Monitor Task
每周五早上10点执行 - 竞品监控
"""

import json
from datetime import datetime
from pathlib import Path

BASE_DIR = Path("/home/hermes/www.burncloud.com")
REPORTS_DIR = BASE_DIR / "reports"
DATA_DIR = BASE_DIR / "data"

# 监控的竞品
COMPETITORS = [
    {
        "name": "OpenRouter",
        "url": "https://openrouter.ai/api/v1/models",
        "pricing_url": "https://openrouter.ai/api/v1/models"
    },
    {
        "name": "SiliconFlow",
        "url": "https://siliconflow.cn/models",
        "pricing_url": "https://siliconflow.cn/pricing"
    },
    {
        "name": "LiteLLM",
        "url": "https://litellm.ai/",
        "pricing_url": "https://litellm.ai/pricing"
    }
]

def fetch_competitor_data(competitor):
    """
    获取竞品数据
    TODO: 实现真实的数据抓取
    """
    # 模拟数据
    return {
        "name": competitor["name"],
        "new_models": [],
        "new_compare_pages": [],
        "price_changes": [],
        "lower_than_burncloud": []
    }

def monitor_competitors():
    """运行竞品监控"""
    print(f"[{datetime.now().isoformat()}] 开始竞品监控...")
    
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    
    # 加载 BurnCloud 价格
    models_path = DATA_DIR / "models.json"
    with open(models_path, 'r', encoding='utf-8') as f:
        bc_data = json.load(f)
    bc_models = {m["name"]: m for m in bc_data["models"]}
    
    all_findings = []
    alerts = []
    
    for competitor in COMPETITORS:
        data = fetch_competitor_data(competitor)
        print(f"检查 {competitor['name']}...")
        
        findings = {
            "competitor": competitor["name"],
            "timestamp": datetime.now().isoformat(),
            "new_models": data["new_models"],
            "new_compare_pages": data["new_compare_pages"],
            "price_changes": data["price_changes"],
            "lower_than_burncloud": data["lower_than_burncloud"]
        }
        
        all_findings.append(findings)
        
        # 检查竞品价格是否低于 BurnCloud
        if data["lower_than_burncloud"]:
            alerts.append({
                "competitor": competitor["name"],
                "issue": "竞品价格低于 BurnCloud",
                "details": data["lower_than_burncloud"]
            })
    
    # 写入报告
    report_path = REPORTS_DIR / "competitive.md"
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(f"# 竞品监控报告\n\n")
        f.write(f"时间: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")
        
        for finding in all_findings:
            f.write(f"## {finding['competitor']}\n\n")
            
            if finding["new_models"]:
                f.write(f"### 新增模型\n\n")
                for m in finding["new_models"]:
                    f.write(f"- {m}\n")
                f.write("\n")
            
            if finding["new_compare_pages"]:
                f.write(f"### 新增对比页\n\n")
                for p in finding["new_compare_pages"]:
                    f.write(f"- {p}\n")
                f.write("\n")
            
            if finding["price_changes"]:
                f.write(f"### 价格变动\n\n")
                for pc in finding["price_changes"]:
                    f.write(f"- {pc}\n")
                f.write("\n")
            
            if finding["lower_than_burncloud"]:
                f.write(f"### ⚠️ 价格低于 BurnCloud\n\n")
                for item in finding["lower_than_burncloud"]:
                    f.write(f"- **{item['model']}**: 竞品 ${item['competitor_price']}/1M vs BurnCloud ${item['bc_price']}/1M\n")
    
    # 如果有告警，写入 alert 文件
    if alerts:
        alert_path = REPORTS_DIR / "alert.md"
        with open(alert_path, 'w', encoding='utf-8') as f:
            f.write(f"# 竞品监控告警\n\n")
            f.write(f"时间: {datetime.now().isoformat()}\n\n")
            f.write(f"## 需要人工处理\n\n")
            for alert in alerts:
                f.write(f"### {alert['competitor']}\n\n")
                f.write(f"**问题**: {alert['issue']}\n\n")
                f.write(f"**详情**:\n")
                for detail in alert["details"]:
                    f.write(f"- {detail}\n")
                f.write("\n")
        
        print(f"⚠️ 发现 {len(alerts)} 个告警，已写入 {alert_path}")
        return False
    
    print(f"✓ 竞品监控完成，报告已写入 {report_path}")
    return True

if __name__ == "__main__":
    monitor_competitors()
