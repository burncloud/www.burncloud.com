#!/bin/bash
# BurnCloud 测试服务器监控脚本
# 检查 8080 端口是否有服务运行，如果没有则启动

PORT=8080
SERVER_SCRIPT="/home/hermes/www.burncloud.com/server.py"
LOG_FILE="/tmp/burncloud_server.log"

# 检查端口是否被占用
if netstat -tlnp 2>/dev/null | grep -q ":${PORT} " || ss -tlnp 2>/dev/null | grep -q ":${PORT} "; then
    echo "$(date): 服务器已在端口 ${PORT} 运行"
    exit 0
fi

# 检查 python 进程
if pgrep -f "server.py ${PORT}" > /dev/null; then
    echo "$(date): 服务器进程已存在"
    exit 0
fi

# 启动服务器
echo "$(date): 启动测试服务器..."
cd /home/hermes/www.burncloud.com
nohup python3 "${SERVER_SCRIPT}" ${PORT} >> "${LOG_FILE}" 2>&1 &

sleep 2

# 验证启动成功
if curl -s -o /dev/null -w "%{http_code}" http://localhost:${PORT}/ | grep -q "200"; then
    echo "$(date): ✅ 服务器启动成功 - http://localhost:${PORT}"
else
    echo "$(date): ❌ 服务器启动失败"
    exit 1
fi