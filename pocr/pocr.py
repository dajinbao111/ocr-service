import sys

from paddleocr import PaddleOCR

import app.settings as settings

def recognize_image_text(image_path):
    # 初始化PaddleOCR对象，加载预训练模型
    ocr = PaddleOCR(use_angle_cls=True, lang=settings.LANG)     # 更改lang参数以支持不同语言

    # 加载图片并进行识别
    result = ocr.ocr(image_path)
    print(result)

    # 提取并格式化识别出的文本
    recognized_text = ''
    for line in result:
        # 每个line是一个包含坐标信息和文字识别结果的元祖列表
        for item in line:
            recognized_text += item[1][0] + '\n'    # 提取文字内容

    # 去除末尾的换行符（如果存在）
    if recognized_text.endswith('\n'):
        recognized_text = recognized_text[:-1]

    return recognized_text

if __name__ == "__main__":
    # 输入图片路径
    image_path = "C:/Users/Administrator/Desktop/微信截图_20240605102742.png"

    # 提取图片中的文字
    output_text = recognize_image_text(image_path)
    print("Recognized text:", output_text)