# -*- coding:utf-8 -*-
"""
账号相关 模块API
自动生成于 2026-03-08 10:10:14
"""

from public.request_handler import RequestHandler


class 账号相关Api:
    """账号相关 接口"""
    
    def __init__(self, base_url=None, token=None):
        """
        初始化
        :param base_url: 基础URL
        :param token: 认证token
        """
        self.request_handler = RequestHandler(base_url, token)
    
    def request(self, yaml_file):
        """
        发送请求
        :param yaml_file: YAML文件名
        :return: 响应数据
        """
        return self.request_handler.request(yaml_file)
    
    def verbose(self, data):
        """
        格式化输出
        :param data: 数据
        :return: 格式化后的字符串
        """
        import json
        return json.dumps(data, indent=2, ensure_ascii=False)


    def post_init_check28293(self):
        """
        初始化检查
        请求方法: POST
        请求URL: /pf-lite/api/account/initCheck
        """
        self.json_data = self.request('initCheck28293_test.yaml')
        print(self.verbose(self.json_data))
        return self.json_data


    def post_set-print-account28297(self):
        """
        设置是否云打印账号
        请求方法: POST
        请求URL: /pf-lite/api/account/set-print-account
        """
        self.json_data = self.request('set-print-account28297_test.yaml')
        print(self.verbose(self.json_data))
        return self.json_data


    def post_back_to_home28295(self):
        """
        返回到首页
        请求方法: POST
        请求URL: /pf-lite/api/account/backToHome
        """
        self.json_data = self.request('backToHome28295_test.yaml')
        print(self.verbose(self.json_data))
        return self.json_data


    def post_change_password28298(self):
        """
        修改密码
        请求方法: POST
        请求URL: /pf-lite/api/account/changePassword
        """
        self.json_data = self.request('changePassword28298_test.yaml')
        print(self.verbose(self.json_data))
        return self.json_data


    def post_get_user_info28296(self):
        """
        获取用户信息
        请求方法: POST
        请求URL: /pf-lite/api/account/getUserInfo
        """
        self.json_data = self.request('getUserInfo28296_test.yaml')
        print(self.verbose(self.json_data))
        return self.json_data


    def post_login28294(self):
        """
        登录
        请求方法: POST
        请求URL: /pf-lite/api/account/login
        """
        self.json_data = self.request('login28294_test.yaml')
        print(self.verbose(self.json_data))
        return self.json_data

