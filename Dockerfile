# 使用官方 Python 镜像作为基础镜像
FROM python:3.11-slim

# 设置工作目录为 /app
WORKDIR /app

# 复制 requirements.txt 到容器中
COPY requirements.txt /app/

# 安装 Python 依赖
RUN pip install --no-cache-dir -r requirements.txt

# 复制当前项目代码到容器的 /app 目录
COPY . /app/

# 暴露 FastAPI 应用默认的端口
EXPOSE 8000

# 启动 FastAPI 应用，使用 Uvicorn 运行
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]