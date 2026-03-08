# -*- coding:utf-8 -*-
"""
根据yaml文件夹下的YAML文件生成API模块和测试用例文件
- 按照yaml文件夹的层级结构，在apimap下生成department_yml.py
- 在testcase下生成test_department_yml.py
- 使用googletrans将中文翻译成英文下划线命名
- 测试用例调用方式：self.api_client.method_name("1")（带参数）
- 支持参数替换（{{id}}格式）
"""
import os
import sys
import yaml
from typing import Dict, List, Any

# 添加项目根目录到路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
from public.translator import Translator


class CreateCaseFile:
    """创建API模块和测试用例文件"""

    def __init__(self, yaml_path=None, api_path=None, test_path=None):
        """
        初始化
        :param yaml_path: yaml文件夹路径，默认：./yaml
        :param api_path: API模块路径，默认：./apimap
        :param test_path: 测试用例路径，默认：./testcase
        """
        self.root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.yaml_path = yaml_path or os.path.join(self.root_dir, "yaml")
        self.api_path = api_path or os.path.join(self.root_dir, "apimap")
        self.test_path = test_path or os.path.join(self.root_dir, "testcase")
        self.translator = Translator()

    def create_all(self):
        """生成所有API和测试文件"""
        print(f"📁 YAML路径: {self.yaml_path}")
        print(f"📁 API路径: {self.api_path}")
        print(f"📁 测试路径: {self.test_path}")
        
        # 遍历yaml文件夹的所有子目录
        for root_dir, dirs, files in os.walk(self.yaml_path):
            if root_dir == self.yaml_path:
                continue
            
            # 获取相对路径（中文）
            rel_path_cn = os.path.relpath(root_dir, self.yaml_path)
            
            # 获取该目录下的YAML文件
            yaml_files = [f for f in files if f.endswith('.yaml')]
            
            if not yaml_files:
                continue
            
            print(f"\n📦 处理目录: {rel_path_cn}")
            print(f"📋 找到 {len(yaml_files)} 个YAML文件")
            
            # 创建API模块文件（department_yml.py）
            self._create_department_api(rel_path_cn, yaml_files, root_dir)
            
            # 为每个YAML创建测试文件（test_department_yml.py）
            for yaml_file in yaml_files:
                yaml_full_path = os.path.join(root_dir, yaml_file)
                self._create_test_file(rel_path_cn, yaml_file, yaml_full_path)
        
        print("\n✅ 所有文件生成完成！")

    def _create_department_api(self, rel_path_cn, yaml_files, yaml_dir):
        """创建API模块文件（department_yml.py）"""
        # 翻译目录路径
        rel_path_en = self._translate_path(rel_path_cn)
        
        # 创建API目录
        api_dir = os.path.join(self.api_path, rel_path_en)
        if not os.path.exists(api_dir):
            os.makedirs(api_dir)
            print(f"  📁 创建API目录: {rel_path_en}")
        
        # 获取目录名作为模块名
        dir_name_cn = os.path.basename(rel_path_cn)
        dir_name_en = self.translator.translate_filename(dir_name_cn)
        
        # 生成文件名
        module_filename = f"{dir_name_en}_yml.py"
        api_file = os.path.join(api_dir, module_filename)
        
        # 生成类名
        class_name = self.translator.translate_class_name(dir_name_cn)
        class_name_en = f"{class_name}API"
        
        # 生成接口方法
        methods = []
        for yaml_file in yaml_files:
            yaml_full_path = os.path.join(yaml_dir, yaml_file)
            yaml_data = self._load_yaml(yaml_full_path)
            if yaml_data:
                method_code = self._generate_api_method(yaml_data, yaml_file, class_name_en)
                methods.append(method_code)
        
        # 生成API文件内容
        content = f'''# -*- coding:utf-8 -*-
"""
{dir_name_cn} 模块API
自动生成于 {self._get_timestamp()}
"""
from public.base import BaseAPI
from public.login import Login


class {class_name_en}(BaseAPI):
    """{dir_name_cn} 接口"""
    
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

{chr(10).join(methods)}
'''

        # 写入文件
        with open(api_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"  ✅ 生成API文件: {module_filename}")

    def _generate_api_method(self, yaml_data, yaml_file, class_name_en):
        """生成API方法代码"""
        testinfo = yaml_data.get("testinfo", {})
        test_case = yaml_data.get("test_case", [])
        
        if not test_case:
            return ""
        
        case_info = test_case[0]
        info_cn = case_info.get("info", "")
        method = case_info.get("method", "")
        url = case_info.get("url", "")
        
        # 翻译接口描述
        info_en = self.translator.translate_description(info_cn) if info_cn else ""
        
        # 生成方法名：根据yaml文件名
        method_name = self._generate_method_name(yaml_file, method, url, info_en)
        
        # 检查是否有需要替换的参数（{{id}} 格式）
        json_data = case_info.get("json", {})
        params = case_info.get("params", {})
        has_placeholders = self._check_placeholders(json_data) or self._check_placeholders(params)
        
        # 如果有占位符，添加参数（支持字符串参数，如 "1"）
        if has_placeholders:
            code = f'''
    def {method_name}(self, param=""):
        """
        {info_cn or yaml_file}
        请求方法: {method}
        请求URL: {url}
        
        :param param: 参数，可以是字符串如 "1" 或字典如 {{"id": 1}}
        :return: 响应数据
        """
        # 如果参数是字符串，构建context字典
        if isinstance(param, str):
            context = {{"id": param}} if param else {{}}
        else:
            context = param
        
        self.json_data = self.request('{yaml_file}', context=context)
        print(self.verbose(self.json_data))
        return self.json_data
'''
        else:
            code = f'''
    def {method_name}(self, param=""):
        """
        {info_cn or yaml_file}
        请求方法: {method}
        请求URL: {url}
        
        :param param: 参数（此接口不需要参数，保留接口一致性）
        :return: 响应数据
        """
        self.json_data = self.request('{yaml_file}')
        print(self.verbose(self.json_data))
        return self.json_data
'''
        return code

    def _generate_method_name(self, yaml_file, method, url, info_en):
        """生成方法名"""
        # 从yaml文件名提取方法名（去掉后缀和_test）
        base_name = yaml_file.replace('.yaml', '').replace('_test', '')
        
        # 提取ID部分（最后一个数字段）
        parts = base_name.split('_')
        if parts and parts[-1].isdigit():
            base_name = '_'.join(parts[:-1])
        
        # 转为蛇形命名（英文）
        method_name = self.translator.translate_method_name(base_name)
        
        # 添加方法前缀
        method_lower = method.lower() if method else 'get'
        method_name = f"{method_lower}_{method_name}"
        
        return method_name

    def _check_placeholders(self, data):
        """检查是否有占位符（{{key}}格式）"""
        if isinstance(data, dict):
            for v in data.values():
                if isinstance(v, str) and '{{' in v and '}}' in v:
                    return True
                elif isinstance(v, (dict, list)):
                    if self._check_placeholders(v):
                        return True
        elif isinstance(data, list):
            for item in data:
                if isinstance(item, (dict, list)):
                    if self._check_placeholders(item):
                        return True
        return False

    def _create_test_file(self, rel_path_cn, yaml_file, yaml_full_path):
        """创建测试用例文件（test_department_yml.py）"""
        yaml_data = self._load_yaml(yaml_full_path)
        if not yaml_data:
            return
        
        testinfo = yaml_data.get("testinfo", {})
        test_case = yaml_data.get("test_case", [])
        
        # 获取模块信息
        dir_name_cn = os.path.basename(rel_path_cn)
        dir_name_en = self.translator.translate_filename(dir_name_cn)
        class_name_en = f"{self.translator.translate_class_name(dir_name_cn)}API"
        
        # 翻译目录路径
        rel_path_en = self._translate_path(rel_path_cn)
        
        # 创建测试目录
        test_dir = os.path.join(self.test_path, rel_path_en)
        if not os.path.exists(test_dir):
            os.makedirs(test_dir)
            print(f"  📁 创建测试目录: {rel_path_en}")
        
        # 生成测试文件名
        test_filename = yaml_file.replace('.yaml', '.py')
        test_file = os.path.join(test_dir, test_filename)
        
        # 导入API类
        api_import = f"apimap.{rel_path_en.replace(os.sep, '.')}.{dir_name_en}_yml"
        api_class = class_name_en
        
        # 获取方法名
        method_name = self._generate_method_name_from_yaml(yaml_file, test_case)
        
        # 检查是否有占位符
        case_info = test_case[0] if test_case else {}
        json_data = case_info.get("json", {})
        params = case_info.get("params", {})
        has_placeholders = self._check_placeholders(json_data) or self._check_placeholders(params)
        
        # 生成测试用例
        test_methods = []
        for idx, case in enumerate(test_case):
            test_method = self._generate_test_method(case, idx, testinfo, method_name, has_placeholders)
            test_methods.append(test_method)
        
        # 生成测试文件内容
        content = f'''# -*- coding:utf-8 -*-
"""
{dir_name_cn} 测试用例
自动生成于 {self._get_timestamp()}
YAML文件: {yaml_file}
"""

import pytest
import allure
from {api_import} import {api_class}


@allure.feature("{dir_name_cn}")
class Test{self.translator.translate_class_name(dir_name_cn)}:
    """{dir_name_cn} 接口测试"""
    
    @pytest.fixture(scope="class")
    def api_client(self):
        """API客户端"""
        return {api_class}()
    
{chr(10).join(test_methods)}
'''

        # 写入文件
        with open(test_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"  ✅ 生成测试文件: test_{test_filename}")

    def _generate_test_method(self, test_case, idx, testinfo, method_name, has_placeholders):
        """生成测试方法代码"""
        test_name = test_case.get("test_name", f"case_{idx}")
        info = test_case.get("info", "")
        method = test_case.get("method", "GET")
        url = test_case.get("url", "")
        mark = test_case.get("mark", "")
        
        # 生成方法名
        test_method_name = f"test_{self.translator.translate_method_name(test_name or f'case_{idx}')}"
        
        # 生成方法装饰器
        skip_decorator = f'    @pytest.mark.skip(reason="跳过测试")' if not test_case.get("test_name") else ''
        mark_decorator = f'    @pytest.mark.{mark}' if mark else ''
        
        if has_placeholders:
            code = f'''{mark_decorator}
{skip_decorator}
    @allure.story("{info or method} {url}")
    def {test_method_name}(self, api_client):
        """
        {info or f"测试用例 {idx + 1}"}
        请求方法: {method}
        请求URL: {url}
        
        注意：此接口需要传递参数
        """
        # 调用API方法，传递参数
        # 方式1：字符串参数（适合单个ID）
        response = api_client.{method_name}("1")
        
        # 方式2：字典参数（适合多个参数）
        # response = api_client.{method_name}({{"userId": 1, "name": "test"}})
        
        assert response is not None, "响应为空"
'''
        else:
            code = f'''{mark_decorator}
{skip_decorator}
    @allure.story("{info or method} {url}")
    def {test_method_name}(self, api_client):
        """
        {info or f"测试用例 {idx + 1}"}
        请求方法: {method}
        请求URL: {url}
        
        注意：此接口不需要参数，保持空字符串即可
        """
        # 调用API方法（不需要参数）
        response = api_client.{method_name}("")
        
        assert response is not None, "响应为空"
'''
        return code

    def _generate_method_name_from_yaml(self, yaml_file, test_case):
        """根据YAML文件名生成方法名"""
        # 从yaml文件名提取方法名（去掉后缀和_test）
        base_name = yaml_file.replace('.yaml', '').replace('_test', '')
        
        # 提取ID部分（最后一个数字段）
        parts = base_name.split('_')
        if parts and parts[-1].isdigit():
            base_name = '_'.join(parts[:-1])
        
        # 获取方法类型
        method = 'GET'
        if test_case:
            method = test_case[0].get("method", "GET")
        
        method_lower = method.lower()
        return f"{method_lower}_{self.translator.translate_method_name(base_name)}"

    def _translate_path(self, path):
        """
        翻译路径
        :param path: 中文路径
        :return: 英文路径
        """
        parts = path.split(os.sep)
        translated_parts = []
        for part in parts:
            translated_parts.append(self.translator.translate_filename(part))
        return os.sep.join(translated_parts)

    def _load_yaml(self, yaml_file):
        """加载YAML文件"""
        try:
            with open(yaml_file, 'r', encoding='utf-8') as f:
                return yaml.load(f, Loader=yaml.Loader)
        except Exception as e:
            print(f"❌ 加载YAML失败 {yaml_file}: {e}")
            return None

    def _get_timestamp(self):
        """获取当前时间"""
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


if __name__ == '__main__':
    # 示例使用
    creator = CreateCaseFile()
    creator.create_all()
