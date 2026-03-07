# -*- coding:utf-8 -*-
"""
根据YAML文件生成API模块和测试用例文件
- 一个模块对应一个api.py（可能包含多个yaml）
- 一个yaml对应一个test_api.py
- 支持pytest参数化传递参数
"""
import os
import yaml
from typing import Dict, List, Any


class CreateCaseFile:
    """创建API模块和测试用例文件"""

    def __init__(self, yaml_path=None, api_path=None, test_path=None):
        """
        初始化
        :param yaml_path: YAML文件路径，默认：./testdata
        :param api_path: API模块路径，默认：./apimap
        :param test_path: 测试用例路径，默认：./testosmcase
        """
        self.root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.yaml_path = yaml_path or os.path.join(self.root_dir, "testdata")
        self.api_path = api_path or os.path.join(self.root_dir, "apimap")
        self.test_path = test_path or os.path.join(self.root_dir, "testosmcase")

    def create_all(self):
        """生成所有API和测试文件"""
        print(f"📁 YAML路径: {self.yaml_path}")
        print(f"📁 API路径: {self.api_path}")
        print(f"📁 测试路径: {self.test_path}")
        
        # 遍历所有模块目录
        for module_name in os.listdir(self.yaml_path):
            module_yaml_dir = os.path.join(self.yaml_path, module_name)
            if not os.path.isdir(module_yaml_dir):
                continue
            
            print(f"\n📦 处理模块: {module_name}")
            self._create_module_files(module_name, module_yaml_dir)
        
        print("\n✅ 所有文件生成完成！")

    def _create_module_files(self, module_name, module_yaml_dir):
        """为单个模块创建API和测试文件"""
        # 读取该模块的所有YAML文件
        yaml_files = []
        for file in os.listdir(module_yaml_dir):
            if file.endswith('.yaml'):
                yaml_file = os.path.join(module_yaml_dir, file)
                # 检查yaml格式
                yaml_data = self._load_yaml(yaml_file)
                if yaml_data and isinstance(yaml_data, dict) and "testinfo" in yaml_data:
                    yaml_files.append(yaml_file)
                else:
                    print(f"  ⚠️  跳过旧格式YAML: {file}")
        
        if not yaml_files:
            print(f"⚠️  模块 {module_name} 没有找到新格式的YAML文件")
            return
        
        print(f"📋 找到 {len(yaml_files)} 个YAML文件")
        
        # 创建API模块文件
        self._create_api_file(module_name, yaml_files)
        
        # 为每个YAML创建测试文件
        for yaml_file in yaml_files:
            self._create_test_file(module_name, yaml_file)

    def _create_api_file(self, module_name, yaml_files):
        """创建API模块文件（一个模块一个文件）"""
        # 创建模块目录
        module_dir = os.path.join(self.api_path, f"api_{module_name.lower()}")
        if not os.path.exists(module_dir):
            os.makedirs(module_dir)
        
        # API文件名
        api_filename = f"{self._camel_case(module_name)}.py"
        api_file = os.path.join(module_dir, api_filename)
        
        # 生成API类
        class_name = f"{self._camel_case(module_name)}Api"
        
        # 收集所有接口方法
        methods = []
        for yaml_file in yaml_files:
            yaml_data = self._load_yaml(yaml_file)
            if yaml_data:
                method_code = self._generate_api_method(yaml_data, yaml_file)
                methods.append(method_code)
        
        # 生成API文件内容
        content = f'''# -*- coding:utf-8 -*-
"""
{module_name} 模块API
自动生成于 {self._get_timestamp()}
"""

import requests
from public.logger import log


class {class_name}:
    """{module_name} 接口"""
    
    def __init__(self, base_url=None, token=None):
        """
        初始化
        :param base_url: 基础URL
        :param token: 认证token
        """
        self.base_url = base_url or ""
        self.token = token or ""
        self.headers = {{"Authorization": token}} if token else {{}}
    
    def _request(self, method, url, **kwargs):
        """
        发送请求
        :param method: 请求方法
        :param url: 请求URL
        :param kwargs: 其他参数
        :return: 响应对象
        """
        full_url = self.base_url + url
        log.info(f"请求地址: {{method}} {{full_url}}")
        log.info(f"请求参数: {{kwargs}}")
        
        try:
            response = requests.request(
                method=method,
                url=full_url,
                headers={{**self.headers, **kwargs.get('headers', {{}})}},
                timeout=kwargs.get('timeout', 8),
                verify=False,
                **{{k: v for k, v in kwargs.items() if k not in ['headers', 'timeout']}}
            )
            log.info(f"响应状态码: {{response.status_code}}")
            log.info(f"响应内容: {{response.text[:500]}}")
            return response
        except Exception as e:
            log.error(f"请求失败: {{e}}")
            raise

{chr(10).join(methods)}
'''

        # 写入文件
        with open(api_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ 生成API文件: {api_filename}")

    def _generate_api_method(self, yaml_data, yaml_file):
        """生成API方法代码"""
        testinfo = yaml_data.get("testinfo", {})
        request = yaml_data.get("request", {})
        
        title = testinfo.get("title", "")
        interface_id = testinfo.get("interface_id", "")
        
        # 生成方法名
        method_name = self._snake_case(title)
        method_name = f"{method_name}_{interface_id}"
        
        url = request.get("url", "")
        method = request.get("method", "GET").upper()
        default_headers = request.get("headers", {})
        default_params = request.get("params", {})
        default_data = request.get("data", "")
        default_json = request.get("json", {})
        
        code = f'''
    def {method_name}(self, url="{url}", method="{method}", headers=None, params=None, data=None, json=None, files=None, timeout=8, **kwargs):
        """
        {title}
        
        :param url: 请求URL，默认: {url}
        :param method: 请求方法，默认: {method}
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
        final_headers = {default_headers}
        if headers:
            final_headers.update(headers)
        
        final_params = {default_params}
        if params:
            final_params.update(params)
        
        final_data = data
        if data is None and "{default_data}":
            final_data = {default_data}
        
        final_json = json
        if json is None:
            final_json = {default_json}
        
        # 清理空值
        if final_params is None:
            final_params = {{}}
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
'''
        return code

    def _create_test_file(self, module_name, yaml_file):
        """创建测试用例文件（一个YAML一个文件）"""
        yaml_data = self._load_yaml(yaml_file)
        if not yaml_data:
            return
        
        testinfo = yaml_data.get("testinfo", {})
        request = yaml_data.get("request", {})
        test_cases = yaml_data.get("test_case", [])
        
        title = testinfo.get("title", "")
        interface_id = testinfo.get("interface_id", "")
        
        # 生成测试类名
        test_class_name = f"Test{self._camel_case(title)}"
        
        # 创建测试目录
        test_module_dir = os.path.join(self.test_path, f"test_{module_name.lower()}")
        if not os.path.exists(test_module_dir):
            os.makedirs(test_module_dir)
        
        # 生成测试文件名
        test_filename = f"test_{self._snake_case(title)}_{interface_id}.py"
        test_file = os.path.join(test_module_dir, test_filename)
        
        # 导入API类
        api_module = f"apimap.api_{module_name.lower()}.{self._camel_case(module_name)}"
        api_class = f"{self._camel_case(module_name)}Api"
        
        # 生成测试用例
        test_methods = []
        for idx, test_case in enumerate(test_cases):
            test_method = self._generate_test_method(test_case, idx, request)
            test_methods.append(test_method)
        
        # 生成测试文件内容
        content = f'''# -*- coding:utf-8 -*-
"""
{title} 测试用例
自动生成于 {self._get_timestamp()}
YAML文件: {os.path.basename(yaml_file)}
"""

import pytest
import allure
from {api_module} import {api_class}


@allure.feature("{module_name}")
class {test_class_name}:
    """{title} 接口测试"""
    
    @pytest.fixture(scope="class")
    def api_client(self):
        """API客户端"""
        return {api_class}()
    
{chr(10).join(test_methods)}
'''

        # 写入文件
        with open(test_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"  ✅ 生成测试文件: {test_filename}")

    def _generate_test_method(self, test_case, idx, request):
        """生成测试方法代码"""
        case_name = test_case.get("case_name", f"case_{idx}")
        description = test_case.get("description", "")
        mark = test_case.get("mark", "")
        skip = test_case.get("skip", False)
        validate = test_case.get("validate", {})
        
        # 生成方法名
        method_name = f"test_{self._snake_case(case_name)}"
        
        # 生成参数化数据
        test_data = []
        
        # 添加默认参数（来自YAML）
        default_params = {
            "url": request.get("url", ""),
            "method": request.get("method", "GET").upper(),
            "headers": request.get("headers", {}),
            "params": request.get("params", {}),
            "data": request.get("data", ""),
            "json": request.get("json", {}),
            "timeout": request.get("timeout", 8)
        }
        test_data.append(default_params)
        
        # 生成参数化装饰器
        parametrize_decorator = f'    @pytest.mark.parametrize("kwargs", {test_data})'
        
        # 生成测试方法
        skip_decorator = f'    @pytest.mark.skip(reason="跳过测试")' if skip else ''
        mark_decorator = f'    @pytest.mark.{mark}' if mark else ''
        
        code = f'''{parametrize_decorator}
{mark_decorator}
{skip_decorator}
    @allure.story("{description}")
    def {method_name}(self, api_client, kwargs):
        """
        {description}
        
        参数来自YAML和pytest参数化
        """
        with allure.step("发送请求"):
            response = api_client._request(**kwargs)
        
        with allure.step("验证响应"):
            # 基本验证
            assert response.status_code == {validate.get('status_code', 200)}, f"状态码错误: {{response.status_code}}"
            
            # 验证响应内容
            expected_contains = "{validate.get('contains', '')}"
            if expected_contains:
                assert expected_contains in response.text, f"响应不包含预期内容: {{expected_contains}}"
            
            # JSON路径验证
            json_path = "{validate.get('json_path', '')}"
            json_value = "{validate.get('json_value', '')}"
            if json_path and json_value:
                from jsonpath import jsonpath
                actual_value = jsonpath(response.json(), json_path)
                assert str(actual_value) == str(json_value), f"JSON路径值不匹配: {{actual_value}} != {{json_value}}"
'''
        return code

    def _load_yaml(self, yaml_file):
        """加载YAML文件"""
        try:
            with open(yaml_file, 'r', encoding='utf-8') as f:
                return yaml.load(f, Loader=yaml.Loader)
        except Exception as e:
            print(f"❌ 加载YAML失败 {yaml_file}: {e}")
            return None

    def _camel_case(self, name):
        """转驼峰命名"""
        # 先转成单词首字母大写
        words = name.replace('-', '_').replace(' ', '_').split('_')
        return ''.join(word.capitalize() for word in words if word)

    def _snake_case(self, name):
        """转蛇形命名"""
        import re
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

    def _get_timestamp(self):
        """获取当前时间"""
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


if __name__ == '__main__':
    # 示例使用
    creator = CreateCaseFile()
    creator.create_all()
