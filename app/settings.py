import socket


def get_local_ip():
    """
    获取当前计算机的ip地址
    """
    return socket.gethostbyname(socket.gethostname())


# 服务端口
SERVICE_PORT = 8000
SERVICE_IP = get_local_ip()
# 服务名
SERVICE_NAME = "ocr-service"

# Nacos 配置
NACOS_SERVER_ADDRESS = "172.16.201.26:8848"
NACOS_NAMESPACE = "test"
NACOS_DATA_ID = "ocr-service"
NACOS_USERNAME = "nacos"
NACOS_PASSWORD = "nacos"
NACOS_GROUP_NAME = "CCLOUD_GROUP"

# 语言熟悉
LANG = "ch"


def set_lang(new_lang):
    """
    设置OCR模型语言熟悉
    :param new_lang: 新的语言属性
    :return:
    """
    print("设置OCR模型语言属性为:", new_lang)
    global LANG
    LANG = new_lang
