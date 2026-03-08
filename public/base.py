# -*- coding:utf-8 -*-
"""
基础类 - 公共请求方法和YAML解析
"""
import os
import yaml
import requests
from typing import Dict, Any, Optional
from public.logger import log
import string
import re


class BaseAPI:
    """API 基础类"""
    
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
    
    def request(self, file_name: str, context: Optional[Dict] = None, **kwargs):
        """
        发送请求
        :param file_name: yaml文件名称
        :param context: 要替换的参数，比如 params, json
        :param kwargs: 其他参数
        :return: 响应数据
        """
        # 1. 读取yaml文件
        yaml_data = self._load_yaml(file_name)
        
        if not yaml_data:
            raise FileNotFoundError(f"找不到yaml文件: {file_name}")
        
        # 2. 获取测试用例
        test_case = yaml_data.get("test_case", [])
        
        if not test_case:
            raise ValueError(f"yaml文件中没有测试用例: {file_name}")
        
        case = test_case[0]
        
        # 3. 替换参数（支持 {{id}} 格式）
        url = case.get("url", "")
        method = case.get("method", "GET").upper()
        headers = case.get("headers", {})
        params = case.get("params", {})
        data = case.get("data", "")
        json_data = case.get("json", {})
        files = case.get("files", "")
        timeout = case.get("timeout", 8)
        
        # 4. 参数替换
        if context:
            params = self._replace_params(params, context)
            json_data = self._replace_params(json_data, context)
            data = self._replace_params(data, context)
        
        # 5. 合并headers
        final_headers = {**self.headers, **headers}
        
        # 6. 替换token
        if "$token" in final_headers.get("Authorization", ""):
            final_headers["Authorization"] = self.token
        
        # 7. 清理空值
        if params is None:
            params = {}
        if data is None:
            data = None
        if json_data is None:
            json_data = {}
        
        # 8. 发送请求
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
            
            # 9. 返回响应数据
            try:
                self.json_data = response.json()
            except:
                self.json_data = {"text": response.text}
            
            return self.json_data
            
        except Exception as e:
            log.error(f"请求失败: {e}")
            raise
    
    def _load_yaml(self, file_name):
        """
        读取yaml文件
        :param file_name: yaml文件名
        :return: yaml数据
        """
        # 在update文件夹中查找
        update_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "update")
        
        for root, dirs, files in os.walk(update_dir):
            if file_name in files:
                yaml_file = os.path.join(root, file_name)
                try:
                    with open(yaml_file, 'r', encoding='utf-8') as f:
                        return yaml.load(f, Loader=yaml.Loader)
                except Exception as e:
                    log.error(f"加载yaml失败 {yaml_file}: {e}")
                    return None
        
        return None
    
    def _replace_params(self, source_data, context):
        """
        替换参数（支持 {{key}} 格式）
        :param source_data: 源数据（dict 或 str）
        :param context: 上下文参数
        :return: 替换后的数据
        """
        if not context:
            return source_data
        
        if isinstance(source_data, dict):
            result = {}
            for key, value in source_data.items():
                if isinstance(value, str):
                    # 替换 {{key}} 格式
                    for k, v in context.items():
                        value = value.replace(f"{{{{{k}}}}}", str(v))
                    result[key] = value
                elif isinstance(value, dict):
                    result[key] = self._replace_params(value, context)
                elif isinstance(value, list):
                    result[key] = self._replace_params(value, context)
                else:
                    result[key] = value
            return result
        elif isinstance(source_data, list):
            return [self._replace_params(item, context) for item in source_data]
        elif isinstance(source_data, str):
            result = source_data
            for k, v in context.items():
                result = result.replace(f"{{{{{k}}}}}", str(v))
            return result
        else:
            return source_data
    
    def verbose(self, data):
        """
        格式化输出
        :param data: 数据
        :return: 格式化后的字符串
        """
        import json
        return json.dumps(data, indent=2, ensure_ascii=False)
