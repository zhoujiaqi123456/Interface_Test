# -*- coding:utf-8 -*-
"""
导出 模块API
自动生成于 2026-03-08 10:10:14
"""

from public.request_handler import RequestHandler


class 导出Api:
    """导出 接口"""
    
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


    def post_cancel28121(self):
        """
        取消导出
        请求方法: POST
        请求URL: /pf-lite/api/export/cancel
        """
        self.json_data = self.request('cancel28121_test.yaml')
        print(self.verbose(self.json_data))
        return self.json_data


    def post_export28120(self):
        """
        开始导出
        请求方法: POST
        请求URL: /pf-lite/api/export/export
        """
        self.json_data = self.request('export28120_test.yaml')
        print(self.verbose(self.json_data))
        return self.json_data

