# -*- coding:utf-8 -*-
"""
请求处理器
负责发送HTTP请求
"""
import os
import yaml
import requests
from typing import Dict, Any
from public.logger import log


class RequestHandler:
    """请求处理器"""
    
    def __init__(self, base_url=None, token=None):
        """
        初始化
        :param base_url: 基础URL
        :param token: 认证token
        """
        self.base_url = base_url or ""
        self.token = token or ""
        self.headers = {"Authorization": token} if token else {}
        self.json_data = None
    
    def request(self, yaml_file):
        """
        根据YAML文件发送请求
        :param yaml_file: YAML文件名
        :return: 响应数据
        """
        # 查找YAML文件
        yaml_path = self._find_yaml_file(yaml_file)
        
        if not yaml_path:
            raise FileNotFoundError(f"找不到YAML文件: {yaml_file}")
        
        # 加载YAML文件
        yaml_data = self._load_yaml(yaml_path)
        
        if not yaml_data:
            raise ValueError(f"加载YAML文件失败: {yaml_file}")
        
        # 获取测试用例
        test_case = yaml_data.get("test_case", [])
        
        if not test_case:
            raise ValueError(f"YAML文件中没有测试用例: {yaml_file}")
        
        case = test_case[0]
        
        # 构建请求参数
        url = case.get("url", "")
        method = case.get("method", "GET").upper()
        headers = case.get("headers", {})
        params = case.get("params", {})
        data = case.get("data", "")
        json_data = case.get("json", {})
        files = case.get("files", "")
        timeout = case.get("timeout", 8)
        
        # 合并headers
        final_headers = {**self.headers, **headers}
        
        # 替换token
        if "$token" in final_headers.get("Authorization", ""):
            final_headers["Authorization"] = self.token
        
        # 清理空值
        if params is None:
            params = {}
        if data is None:
            data = None
        if json_data is None:
            json_data = {}
        
        # 发送请求
        full_url = self.base_url + url
        log.info(f"请求地址: {method} {full_url}")
        log.info(f"请求参数: params={params}, json={json_data}")
        
        try:
            if files:
                # 文件上传
                response = requests.request(
                    method=method,
                    url=full_url,
                    headers=final_headers,
                    files=eval(files) if isinstance(files, str) else files,
                    data=data,
                    params=params,
                    timeout=timeout,
                    verify=False
                )
            else:
                # 普通请求
                response = requests.request(
                    method=method,
                    url=full_url,
                    headers=final_headers,
                    params=params,
                    data=data,
                    json=json_data,
                    timeout=timeout,
                    verify=False
                )
            
            log.info(f"响应状态码: {response.status_code}")
            log.info(f"响应内容: {response.text[:500]}")
            
            # 返回响应数据
            try:
                self.json_data = response.json()
            except:
                self.json_data = {"text": response.text}
            
            return self.json_data
            
        except Exception as e:
            log.error(f"请求失败: {e}")
            raise
    
    def _find_yaml_file(self, yaml_file):
        """
        查找YAML文件
        :param yaml_file: YAML文件名
        :return: YAML文件路径
        """
        # 在update文件夹中查找
        update_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "update")
        
        for root, dirs, files in os.walk(update_dir):
            if yaml_file in files:
                return os.path.join(root, yaml_file)
        
        return None
    
    def _load_yaml(self, yaml_file):
        """
        加载YAML文件
        :param yaml_file: YAML文件路径
        :return: YAML数据
        """
        try:
            with open(yaml_file, 'r', encoding='utf-8') as f:
                return yaml.load(f, Loader=yaml.Loader)
        except Exception as e:
            log.error(f"加载YAML失败 {yaml_file}: {e}")
            return None


if __name__ == '__main__':
    # 测试
    handler = RequestHandler(base_url="http://example.com", token="test_token")
    # response = handler.request("login28294_test.yaml")
    # print(response)
