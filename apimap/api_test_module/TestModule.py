# -*- coding:utf-8 -*-
"""
test_module 模块API
自动生成于 2026-03-07 21:40:57
"""

import requests
from public.logger import log


class TestModuleApi:
    """test_module 接口"""
    
    def __init__(self, base_url=None, token=None):
        """
        初始化
        :param base_url: 基础URL
        :param token: 认证token
        """
        self.base_url = base_url or ""
        self.token = token or ""
        self.headers = {"Authorization": token} if token else {}
    
    def _request(self, method, url, **kwargs):
        """
        发送请求
        :param method: 请求方法
        :param url: 请求URL
        :param kwargs: 其他参数
        :return: 响应对象
        """
        full_url = self.base_url + url
        log.info(f"请求地址: {method} {full_url}")
        log.info(f"请求参数: {kwargs}")
        
        try:
            response = requests.request(
                method=method,
                url=full_url,
                headers={**self.headers, **kwargs.get('headers', {})},
                timeout=kwargs.get('timeout', 8),
                verify=False,
                **{k: v for k, v in kwargs.items() if k not in ['headers', 'timeout']}
            )
            log.info(f"响应状态码: {response.status_code}")
            log.info(f"响应内容: {response.text[:500]}")
            return response
        except Exception as e:
            log.error(f"请求失败: {e}")
            raise


    def 添加用户_12345(self, url="/api/user/add", method="POST", headers=None, params=None, data=None, json=None, files=None, timeout=8, **kwargs):
        """
        添加用户
        
        :param url: 请求URL，默认: /api/user/add
        :param method: 请求方法，默认: POST
        :param headers: 请求头，默认包含Authorization
        :param params: URL参数
        :param data: 表单数据
        :param json: JSON数据
        :param files: 文件上传
        :param timeout: 超时时间，默认8秒
        :param kwargs: 其他参数
        :return: 响应对象
        """
        # 合并默认参数
        final_headers = {'Authorization': '$token', 'Content-Type': 'application/json'}
        if headers:
            final_headers.update(headers)
        
        final_params = {}
        if params:
            final_params.update(params)
        
        final_data = data
        if data is None and "":
            final_data = 
        
        final_json = json
        if json is None:
            final_json = {'username': '', 'email': '', 'age': 0, 'active': True}
        
        # 清理空值
        if final_params is None:
            final_params = {}
        if final_data is None:
            final_data = None
        if final_json is None:
            final_json = None
        
        return self._request(
            method=method,
            url=url,
            headers=final_headers,
            params=final_params,
            data=final_data,
            json=final_json,
            files=files,
            timeout=timeout,
            **kwargs
        )

