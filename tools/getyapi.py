# -*- coding:utf-8 -*-
"""
从YAPI接口地址获取接口数据并生成YAML文件
支持新的接口格式：http://yapi.u-breath.cn:9009/api/project/get?id=309
"""
import requests
import os
import time
import json
from ruamel import yaml


class GetYapi(object):
    """从YAPI接口获取数据并生成YAML文件"""

    def __init__(self, project_id=None, base_url=None, cookie=None, headers=None):
        """
        初始化
        :param project_id: 项目ID
        :param base_url: YAPI地址，默认：http://yapi.u-breath.cn:9009
        :param cookie: 登录cookie，格式："_yapi_token=xxx; _yapi_uid=xxx"
        :param headers: 请求头字典
        """
        self.base_url = base_url or "http://yapi.u-breath.cn:9009"
        self.project_id = project_id
        self.cookie = cookie
        self.count = 0  # 统计接口总数
        self.filecount = 0  # 统计yaml总数
        self.root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.yaml_dir = os.path.join(self.root_dir, "testdata")
        self.api_dir = os.path.join(self.root_dir, "apimap")
        
        # 默认请求头
        self.default_headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36'
        }
        if headers:
            self.default_headers.update(headers)
        
        # 请求cookie
        self.cookies = {}
        if cookie:
            for item in cookie.split(';'):
                key, value = item.strip().split('=', 1)
                self.cookies[key] = value

    def create_yaml_by_yapi(self):
        """从YAPI创建YAML文件"""
        self._get_module_list()
        print(f"\n✅ 完成！共处理 {self.count} 个接口，生成 {self.filecount} 个YAML文件")

    def _get_module_list(self):
        """获取模块列表"""
        print(f"📥 正在获取项目 {self.project_id} 的模块列表...")
        
        url = f"{self.base_url}/api/project/get?id={self.project_id}"
        res = self._request(url)
        
        if not res or res.get("errcode") != 0:
            print(f"❌ 获取项目信息失败: {res.get('errmsg', '未知错误')}")
            return
        
        data = res.get("data", {})
        project_name = data.get("name", f"project_{self.project_id}")
        basepath = data.get("basepath", "")
        
        print(f"📦 项目名称: {project_name}")
        print(f"📦 基础路径: {basepath}")
        
        # 获取分类列表
        cat_list = data.get("cat", [])
        print(f"📦 找到 {len(cat_list)} 个分类")
        
        for cat in cat_list:
            cat_id = cat.get("_id")
            cat_name = cat.get("name", f"cat_{cat_id}")
            print(f"\n📂 处理分类: {cat_name} (ID: {cat_id})")
            self._get_interface_list(cat_id, cat_name, basepath)

    def _get_interface_list(self, cat_id, cat_name, basepath):
        """获取接口列表"""
        url = f"{self.base_url}/api/interface/list_cat"
        params = {
            "page": 1,
            "limit": 1000,
            "catid": cat_id
        }
        
        res = self._request(url, params=params)
        
        if not res or res.get("errcode") != 0:
            print(f"❌ 获取接口列表失败: {res.get('errmsg', '未知错误')}")
            return
        
        data = res.get("data", {})
        interface_list = data.get("list", [])
        
        print(f"📋 找到 {len(interface_list)} 个接口")
        
        # 创建模块目录
        module_dir = os.path.join(self.yaml_dir, self._sanitize_filename(cat_name))
        if not os.path.exists(module_dir):
            os.makedirs(module_dir)
            print(f"📁 创建目录: {module_dir}")
        
        for interface in interface_list:
            self._process_interface(interface, cat_name, module_dir, basepath)

    def _process_interface(self, interface, cat_name, module_dir, basepath):
        """处理单个接口"""
        interface_id = interface.get("_id")
        print(f"\n🔧 处理接口 (ID: {interface_id}): {interface.get('title')}")
        
        # 获取接口详情
        url = f"{self.base_url}/api/interface/get?id={interface_id}"
        res = self._request(url)
        
        if not res or res.get("errcode") != 0:
            print(f"❌ 获取接口详情失败: {res.get('errmsg', '未知错误')}")
            return
        
        interface_data = res.get("data", {})
        self._create_yaml_file(interface_data, cat_name, module_dir, basepath)

    def _create_yaml_file(self, interface_data, cat_name, module_dir, basepath):
        """创建YAML文件"""
        interface_id = interface_data.get("_id")
        title = interface_data.get("title", "")
        path = interface_data.get("path", "")
        method = interface_data.get("method", "GET")
        
        # 生成YAML文件名
        file_name = f"{self._sanitize_filename(title)}_{interface_id}.yaml"
        yaml_file = os.path.join(module_dir, file_name)
        
        # 解析请求参数
        yaml_content = {
            "testinfo": {
                "interface_id": interface_id,
                "title": title,
                "category": cat_name,
                "description": interface_data.get("desc", "")
            },
            "request": {
                "url": basepath + path,
                "method": method,
                "headers": self._parse_headers(interface_data),
                "params": self._parse_params(interface_data),
                "data": self._parse_data(interface_data),
                "json": self._parse_json(interface_data),
                "files": "",
                "timeout": 8
            },
            "test_case": [
                {
                    "case_name": "冒烟测试",
                    "description": "基本功能测试",
                    "mark": "smoke",
                    "skip": False,
                    "extract": "",
                    "validate": {
                        "status_code": 200,
                        "contains": "",
                        "json_path": "",
                        "json_value": ""
                    }
                }
            ]
        }
        
        # 写入YAML文件
        with open(yaml_file, 'w', encoding='utf-8') as f:
            yaml.dump(yaml_content, f, Dumper=yaml.RoundTripDumper, allow_unicode=True)
        
        self.filecount += 1
        self.count += 1
        print(f"✅ 生成YAML: {file_name}")

    def _parse_headers(self, interface_data):
        """解析请求头"""
        req_headers = interface_data.get("req_headers", [])
        headers = {}
        for header in req_headers:
            headers[header.get("name", "")] = header.get("value", "")
        
        # 默认添加Authorization
        if "Authorization" not in headers:
            headers["Authorization"] = "$token"
        
        return headers

    def _parse_params(self, interface_data):
        """解析URL参数"""
        req_query = interface_data.get("req_query", [])
        params = {}
        for param in req_query:
            params[param.get("name", "")] = ""
        return params

    def _parse_data(self, interface_data):
        """解析表单数据"""
        req_body_form = interface_data.get("req_body_form", [])
        data = {}
        for form in req_body_form:
            data[form.get("name", "")] = ""
        return data

    def _parse_json(self, interface_data):
        """解析JSON数据"""
        req_body_other = interface_data.get("req_body_other", "")
        if req_body_other:
            try:
                json_schema = json.loads(req_body_other)
                if json_schema.get("type") == "object":
                    properties = json_schema.get("properties", {})
                    result = {}
                    for key, value in properties.items():
                        if value.get("type") == "string":
                            result[key] = ""
                        elif value.get("type") == "number":
                            result[key] = 0
                        elif value.get("type") == "boolean":
                            result[key] = True
                        elif value.get("type") == "array":
                            result[key] = []
                        elif value.get("type") == "object":
                            result[key] = {}
                        else:
                            result[key] = ""
                    return result
            except json.JSONDecodeError:
                pass
        return {}

    def _request(self, url, params=None, method="GET"):
        """发送请求"""
        try:
            if method.upper() == "GET":
                res = requests.get(
                    url,
                    params=params,
                    headers=self.default_headers,
                    cookies=self.cookies,
                    verify=False,
                    timeout=10
                )
            else:
                res = requests.post(
                    url,
                    params=params,
                    headers=self.default_headers,
                    cookies=self.cookies,
                    verify=False,
                    timeout=10
                )
            return res.json()
        except Exception as e:
            print(f"❌ 请求失败: {e}")
            return None

    def _sanitize_filename(self, filename):
        """清理文件名中的非法字符"""
        import re
        # 替换特殊字符为下划线
        filename = re.sub(r'[<>:"/\\|?*]', '_', filename)
        # 去除首尾空格
        filename = filename.strip()
        # 限制长度
        if len(filename) > 50:
            filename = filename[:50]
        return filename


if __name__ == '__main__':
    # 示例使用
    yapi = GetYapi(
        project_id=309,
        base_url="http://yapi.u-breath.cn:9009",
        cookie="_yapi_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjYxMCwiaWF0IjoxNzcyNDUwMzYwLCJleHAiOjE3NzMwNTUxNjB9.Ojg_dLbDqF72dFfNRJFMP-Vo63QW6mMsOJewBfXk_IY; _yapi_uid=610"
    )
    yapi.create_yaml_by_yapi()
