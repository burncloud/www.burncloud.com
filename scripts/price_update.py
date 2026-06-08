#!/usr/bin/env python3
"""
BurnCloud Price Update Task
每天早上9点执行 - 更新所有模型价格
"""

import json
import os
from datetime import datetime
from pathlib import Path

BASE_DIR = Path("/home/hermes/www.burncloud.com")
DATA_DIR = BASE_DIR / "data"
REPORTS_DIR = BASE_DIR / "reports"

def load_models():
    """加载模型数据"""
    models_path = DATA_DIR / "models.json"
    with open(models_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_models(data):
    """保存模型数据"""
    models_path = DATA_DIR / "models.json"
    with open(models_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def fetch_official_prices():
    """
    抓取官方价格
    TODO: 实现真实的价格抓取逻辑
    目前返回模拟数据
    """
    # 这里应该实现真实的价格抓取
    # 从各官方API获取最新价格
    return {}

def update_prices():
    """主更新逻辑"""
    print(f"[{datetime.now().isoformat()}] 开始价格更新任务...")
    
    # 确保报告目录存在
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    
    data = load_models()
    models = data.get("models", [])
    
    changes = []
    official_prices = fetch_official_prices()
    
    for model in models:
        model_name = model["name"]
        if model_name in official_prices:
            new_input = official_prices[model_name].get("input")
            new_output = official_prices[model_name].get("output")
            
            if new_input and new_input != model["input_price"]:
                old_price = model["input_price"]
                model["input_price"] = new_input
                change_pct = (new_input - old_price) / old_price * 100
                changes.append({
                    "model": model_name,
                    "field": "input_price",
                    "old": old_price,
                    "new": new_input,
                    "change_pct": round(change_pct, 2)
                })
            
            if new_output and new_output != model["output_price"]:
                old_price = model["output_price"]
                model["output_price"] = new_output
                change_pct = (new_input - old_price) / old_price * 100
                changes.append({
                    "model": model_name,
                    "field": "output_price",
                    "old": old_price,
                    "new": new_output,
                    "change_pct": round(change_pct, 2)
                })
    
    # 更新时间戳
    data["last_updated"] = datetime.now().strftime("%Y-%m-%d")
    
    if changes:
        # 检查是否有异常价格变动 (>50%)
        alerts = [c for c in changes if abs(c["change_pct"]) > 50]
        if alerts:
            # 写入告警文件
            alert_path = REPORTS_DIR / "alert.md"
            with open(alert_path, 'w', encoding='utf-8') as f:
                f.write(f"# 价格异常告警\n\n")
                f.write(f"时间: {datetime.now().isoformat()}\n\n")
                f.write("## 异常变动 (>50%)\n\n")
                for a in alerts:
                    f.write(f"- **{a['model']}**: {a['old']} → {a['new']} ({a['change_pct']}%)\n")
            print(f"⚠️ 检测到异常价格变动，已写入 {alert_path}")
            return False
        
        # 保存更新
        save_models(data)
        
        # 写入日志
        log_path = REPORTS_DIR / "price-log.md"
        with open(log_path, 'a', encoding='utf-8') as f:
            f.write(f"\n## {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")
            for c in changes:
                f.write(f"- {c['model']}: {c['field']} ${c['old']}/1M → ${c['new']}/1M ({c['change_pct']:+.1f}%)\n")
        
        print(f"✓ 更新了 {len(changes)} 个价格")
    else:
        print("✓ 无价格变动")
    
    return True

if __name__ == "__main__":
    update_prices()
