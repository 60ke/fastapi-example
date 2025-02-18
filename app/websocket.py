from fastapi import WebSocket
from datetime import datetime
import json

async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()  # 接受 WebSocket 连接
    
    while True:
        try:
            data = await websocket.receive_text()  # 接收客户端发送的消息
            print(f"Received message: {data}")
            
            # 返回服务器时间
            response = {
                "server_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            await websocket.send_text(json.dumps(response))  # 发送服务器时间回客户端

        except Exception as e:
            print(f"Error: {e}")
            await websocket.close()  # 出现异常时关闭连接