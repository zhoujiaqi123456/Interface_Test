# -*- coding:utf-8 -*-
"""
账号相关 模块API
自动生成于 2026-03-08 17:28:49
"""
from public.base import BaseAPI
from public.login import Login


class zhang_hao_xiang_guanAPI(BaseAPI):
    """账号相关 接口"""
    
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


    def post_get_user_by_id28299(self, context=None):
        """
        根据ID获取用户信息
        请求方法: POST
        请求URL: /pf-lite/api/account/getUserById
        
        :param context: 要替换的参数，格式: {"id": 1, "name": "xxx"}
        :return: 响应数据
        """
        self.json_data = self.request('get_user_by_id28299_test.yaml', context=context)
        print(self.verbose(self.json_data))
        return self.json_data


    def post_init_check28293(self):
        """
        初始化检查
        请求方法: POST
        请求URL: /pf-lite/api/account/initCheck
        
        :return: 响应数据
        """
        self.json_data = self.request('initCheck28293_test.yaml')
        print(self.verbose(self.json_data))
        return self.json_data


    def post_set_print_account28297(self):
        """
        设置是否云打印账号
        请求方法: POST
        请求URL: /pf-lite/api/account/set-print-account
        
        :return: 响应数据
        """
        self.json_data = self.request('set-print-account28297_test.yaml')
        print(self.verbose(self.json_data))
        return self.json_data


    def post_back_to_home28295(self):
        """
        返回到首页
        请求方法: POST
        请求URL: /pf-lite/api/account/backToHome
        
        :return: 响应数据
        """
        self.json_data = self.request('backToHome28295_test.yaml')
        print(self.verbose(self.json_data))
        return self.json_data


    def post_change_password28298(self):
        """
        修改密码
        请求方法: POST
        请求URL: /pf-lite/api/account/changePassword
        
        :return: 响应数据
        """
        self.json_data = self.request('changePassword28298_test.yaml')
        print(self.verbose(self.json_data))
        return self.json_data


    def post_get_user_info28296(self):
        """
        获取用户信息
        请求方法: POST
        请求URL: /pf-lite/api/account/getUserInfo
        
        :return: 响应数据
        """
        self.json_data = self.request('getUserInfo28296_test.yaml')
        print(self.verbose(self.json_data))
        return self.json_data


    def post_login28294(self):
        """
        登录
        请求方法: POST
        请求URL: /pf-lite/api/account/login
        
        :return: 响应数据
        """
        self.json_data = self.request('login28294_test.yaml')
        print(self.verbose(self.json_data))
        return self.json_data

