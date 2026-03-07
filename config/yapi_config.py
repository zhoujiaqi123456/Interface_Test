# -*- coding:utf-8 -*-
"""
YAPI配置文件
"""
import os


class YapiConfig:
    """YAPI配置"""
    
    # YAPI服务地址
    BASE_URL = os.getenv("YAPI_BASE_URL", "http://yapi.u-breath.cn:9009")
    
    # 项目ID
    PROJECT_ID = os.getenv("YAPI_PROJECT_ID", "309")
    
    # 登录Cookie
    COOKIE = os.getenv("YAPI_COOKIE", "_yapi_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjYxMCwiaWF0IjoxNzcyNDUwMzYwLCJleHAiOjE3NzMwNTUxNjB9.Ojg_dLbDqF72dFfNRJFMP-Vo63QW6mMsOJewBfXk_IY; _yapi_uid=610")
    
    # 额外的请求头
    HEADERS = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
    }
    
    # 生成文件路径
    ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    YAML_DIR = os.path.join(ROOT_DIR, "testdata")
    API_DIR = os.path.join(ROOT_DIR, "apimap")
    TEST_DIR = os.path.join(ROOT_DIR, "testosmcase")


if __name__ == '__main__':
    print("YAPI配置:")
    print(f"  基础URL: {YapiConfig.BASE_URL}")
    print(f"  项目ID: {YapiConfig.PROJECT_ID}")
    print(f"  YAML目录: {YapiConfig.YAML_DIR}")
    print(f"  API目录: {YapiConfig.API_DIR}")
    print(f"  测试目录: {YapiConfig.TEST_DIR}")
