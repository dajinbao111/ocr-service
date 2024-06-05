import asyncio

import uvicorn
from fastapi import FastAPI

from app import settings
from app.nacos_client import register_service, watch_config, send_heartbeat
from app.routes import router

# 创建 FastAPI 应用
app = FastAPI()

# 注册路由
app.include_router(router)


# 当应用启动时执行的事件
@app.on_event("startup")
async def startup_event():
    register_service()  # 调用注册服务函数
    watch_config()  # 调用监听配置函数

    # 启动心跳任务
    asyncio.create_task(send_heartbeat())  # 创建异步任务发送心跳


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=settings.SERVICE_PORT)  # 运行应用，监听指定端口
