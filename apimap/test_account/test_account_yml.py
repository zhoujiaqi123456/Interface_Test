# -*- coding:utf-8 -*-
"""
test_account 模块API
自动生成于 2026-03-08 17:56:31
"""
from public.base import BaseAPI
from public.login import Login


class TestAccountAPI(BaseAPI):
    """test_account 接口"""
    
    def __init__(self, base_url=None, token=None, sso_ip=None, url_ip=None):
        """
        初始化
        :param base_url: 基础URL
        :param token: 认证token
        :param sso_ip: SSO服务器IP
        :param url_ip: API服务器IP
        """
        super().__init__(base_url, token)
        self.login = Login(sso_ip, url_ip) if sso_ip and url_ip else None
    
    def verbose(self, data):
        """
        格式化输出
        :param data: 数据
        :return: 格式化后的字符串
        """
        import json
        return json.dumps(data, indent=2, ensure_ascii=False)


    def post_login28294(self, param=""):
        """
        登录
        请求方法: POST
        请求URL: /pf-lite/api/account/login
        
        :param param: 参数（此接口不需要参数，保留接口一致性）
        :return: 响应数据
        """
        self.json_data = self.request('login28294_test.yaml')
        print(self.verbose(self.json_data))
        return self.json_data

