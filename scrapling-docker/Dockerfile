# 使用官方 Python 基礎映像
FROM python:3.9-slim

# 設置工作目錄
WORKDIR /app

# 複製依賴文件
COPY requirements.txt .

# 安裝依賴
RUN pip install --no-cache-dir -r requirements.txt

# 複製應用程式代碼
COPY . .

# 暴露端口
EXPOSE 5000

# 運行應用程式
CMD ["python", "server.py"] 