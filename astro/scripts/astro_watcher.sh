#!/bin/bash
# BurnCloud Astro Server Watcher
# 检查并确保 Astro preview 服务器在 8080 端口运行

LOG_FILE="/tmp/burncloud_astro.log"
PORT=8080
ASTRO_DIR="/home/hermes/www.burncloud.com/astro"

log() {
  echo "$(date '+%Y-%m-%d %H:%M:%S') $1" >> "$LOG_FILE"
}

# 检查 Astro preview 服务是否运行
if pgrep -f "astro preview.*$PORT" > /dev/null 2>&1; then
  if curl -s -o /dev/null -w "%{http_code}" "http://localhost:$PORT/" 2>/dev/null | grep -q "200"; then
    log "✓ Astro preview server is running on port $PORT"
    exit 0
  fi
fi

log "! Astro preview server not responding, attempting to start..."

# 停止旧的 Python HTTP 服务器（如果存在）
pkill -f "python.*http.server.*$PORT" 2>/dev/null || true

# 停止旧的 Astro preview 进程
pkill -f "astro preview.*$PORT" 2>/dev/null || true
sleep 2

# 检查 Astro 项目目录
if [ ! -d "$ASTRO_DIR" ]; then
  log "✗ Astro directory not found: $ASTRO_DIR"
  exit 1
fi

# 确保已构建
cd "$ASTRO_DIR"
if [ ! -d "dist" ]; then
  log "! Building Astro project..."
  npm run build >> "$LOG_FILE" 2>&1
fi

# 启动 Astro preview 服务器
log "Starting Astro preview server..."
nohup npm run preview -- --port $PORT > /tmp/astro_preview.log 2>&1 &
sleep 3

# 验证
if curl -s -o /dev/null -w "%{http_code}" "http://localhost:$PORT/" 2>/dev/null | grep -q "200"; then
  log "✓ Astro preview server started successfully on port $PORT"
  exit 0
else
  log "✗ Failed to start Astro preview server"
  cat /tmp/astro_preview.log >> "$LOG_FILE"
  exit 1
fi
