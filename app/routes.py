import os.path

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from pocr.pocr import recognize_image_text


# 定义请求体模型
# 创建一个请求体模型，用于接收文件路径


class FilePathModel(BaseModel):
    filePath: str


# 创建路由
# 创建一个API路由对象
router = APIRouter()


# 定义一个异步函数，用于处理POST请求，接收文件路径并识别图片中的文本信息
@router.post("/ocr/")
async def print_file_path(file_path_model: FilePathModel):
    filePath = file_path_model.filePath
    if not os.path.exists(filePath):
        raise HTTPException(status_code=400, detail="File path does not exist")
    print(f"Received file path: {filePath}")
    text = recognize_image_text(filePath)
    return {"message": text}
