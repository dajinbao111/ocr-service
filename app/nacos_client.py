import asyncio

import nacos
import yaml

import app.settings as settings

# 初始化 Nacos 客户端
# 使用settings中的NACOS参数
client = nacos.NacosClient(server_addresses=settings.NACOS_SERVER_ADDRESS, namespace=settings.NACOS_NAMESPACE,
                           username=settings.NACOS_USERNAME, password=settings.NACOS_PASSWORD)


def register_service():
    # 向Nacos注册服务实例
    client.add_naming_instance(service_name=settings.SERVICE_NAME, ip=settings.SERVICE_IP, port=settings.SERVICE_PORT,
                               group_name=settings.NACOS_GROUP_NAME)


async def send_heartbeat():
    # 异步发送心跳，每10秒发送一次心跳
    while True:
        try:
            client.send_heartbeat(service_name=settings.SERVICE_NAME, ip=settings.SERVICE_IP,
                                  port=settings.SERVICE_PORT, group_name=settings.NACOS_GROUP_NAME)

        except Exception as e:
            print(f"Failed to send heartbeat: {e}")
        await asyncio.sleep(10)  # 每10秒发送一次心跳


def load_config(content):
    # 加载配置文件，解析yaml格式，设置语言
    yaml_config = yaml.full_load(content)
    print("yaml_config:", yaml_config)
    lang = yaml_config['lang']
    settings.set_lang(lang)


def nacos_config_callback(args):
    # Nacos配置回调函数，处理配置更新
    content = args['raw_content']
    load_config(content)


def watch_config():
    # 启动时，强制同步一次配置
    config = client.get_config(settings.NACOS_DATA_ID, settings.NACOS_GROUP_NAME)
    print("config:", config)
    load_config(config)
    # 启动监听器，监控配置变化
    client.add_config_watcher(settings.NACOS_DATA_ID, settings.NACOS_GROUP_NAME, nacos_config_callback)
