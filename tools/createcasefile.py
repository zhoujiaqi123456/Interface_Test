# -*- coding:utf-8 -*-
"""
根据update文件夹下的YAML文件生成API模块和测试用例文件
- 按照update文件夹的层级结构，在apimap和testosmcase下创建相同的层级
- 每个目录生成一个API模块文件
- 每个YAML生成一个测试文件
"""
import os
import yaml
from typing import Dict, List, Any


class CreateCaseFile:
    """创建API模块和测试用例文件"""

    def __init__(self, update_path=None, api_path=None, test_path=None):
        """
        初始化
        :param update_path: update文件夹路径，默认：./update
        :param api_path: API模块路径，默认：./apimap
        :param test_path: 测试用例路径，默认：./testosmcase
        """
        self.root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.update_path = update_path or os.path.join(self.root_dir, "update")
        self.api_path = api_path or os.path.join(self.root_dir, "apimap")
        self.test_path = test_path or os.path.join(self.root_dir, "testosmcase")

    def create_all(self):
        """生成所有API和测试文件"""
        print(f"📁 Update路径: {self.update_path}")
        print(f"📁 API路径: {self.api_path}")
        print(f"📁 测试路径: {self.test_path}")
        
        # 遍历update文件夹的所有子目录
        for root_dir, dirs, files in os.walk(self.update_path):
            if root_dir == self.update_path:
                continue
            
            # 获取相对路径
            rel_path = os.path.relpath(root_dir, self.update_path)
            
            # 获取该目录下的YAML文件
            yaml_files = [f for f in files if f.endswith('.yaml')]
            
            if not yaml_files:
                continue
            
            print(f"\n📦 处理目录: {rel_path}")
            print(f"📋 找到 {len(yaml_files)} 个YAML文件")
            
            # 创建API模块文件
            self._create_api_file(rel_path, yaml_files, root_dir)
            
            # 为每个YAML创建测试文件
            for yaml_file in yaml_files:
                yaml_full_path = os.path.join(root_dir, yaml_file)
                self._create_test_file(rel_path, yaml_file, yaml_full_path)
        
        print("\n✅ 所有文件生成完成！")

    def _create_api_file(self, rel_path, yaml_files, yaml_dir):
        """创建API模块文件"""
        # 创建API目录
        api_dir = os.path.join(self.api_path, rel_path)
        if not os.path.exists(api_dir):
            os.makedirs(api_dir)
            print(f"  📁 创建API目录: {rel_path}")
        
        # 获取目录名作为模块名
        dir_name = os.path.basename(rel_path)
        class_name = self._camel_case(dir_name)
        module_name = self._snake_case(dir_name)
        
        # API文件名
        api_filename = f"{class_name}Api.py"
        api_file = os.path.join(api_dir, api_filename)
        
        # 生成接口方法
        methods = []
        for yaml_file in yaml_files:
            yaml_full_path = os.path.join(yaml_dir, yaml_file)
            yaml_data = self._load_yaml(yaml_full_path)
            if yaml_data:
                method_code = self._generate_api_method(yaml_data, yaml_file)
                methods.append(method_code)
        
        # 生成API文件内容
        content = f'''# -*- coding:utf-8 -*-
"""
{dir_name} 模块API
自动生成于 {self._get_timestamp()}
"""

from public.request_handler import RequestHandler


class {class_name}Api:
    """{dir_name} 接口"""
    
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

{chr(10).join(methods)}
'''

        # 写入文件
        with open(api_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"  ✅ 生成API文件: {api_filename}")

    def _generate_api_method(self, yaml_data, yaml_file):
        """生成API方法代码"""
        testinfo = yaml_data.get("testinfo", {})
        test_case = yaml_data.get("test_case", [])
        
        if not test_case:
            return ""
        
        case_info = test_case[0]
        test_name = case_info.get("test_name", "")
        info = case_info.get("info", "")
        method = case_info.get("method", "")
        url = case_info.get("url", "")
        
        # 生成方法名：根据yaml文件名或者info
        method_name = self._generate_method_name(yaml_file, info, method, url)
        
        code = f'''
    def {method_name}(self):
        """
        {info or yaml_file}
        请求方法: {method}
        请求URL: {url}
        """
        self.json_data = self.request('{yaml_file}')
        print(self.verbose(self.json_data))
        return self.json_data
'''
        return code

    def _generate_method_name(self, yaml_file, info, method, url):
        """生成方法名"""
        # 优先使用yaml文件名（去掉后缀）
        base_name = yaml_file.replace('.yaml', '').replace('_test', '')
        
        # 转为蛇形命名
        method_name = self._snake_case(base_name)
        
        # 添加方法前缀
        method_lower = method.lower() if method else 'get'
        method_name = f"{method_lower}_{method_name}"
        
        return method_name

    def _create_test_file(self, rel_path, yaml_file, yaml_full_path):
        """创建测试用例文件"""
        yaml_data = self._load_yaml(yaml_full_path)
        if not yaml_data:
            return
        
        testinfo = yaml_data.get("testinfo", {})
        test_case = yaml_data.get("test_case", [])
        
        # 获取模块信息
        dir_name = os.path.basename(rel_path)
        module_name = self._snake_case(dir_name)
        class_name = self._camel_case(dir_name)
        
        # 创建测试目录
        test_dir = os.path.join(self.test_path, rel_path)
        if not os.path.exists(test_dir):
            os.makedirs(test_dir)
            print(f"  📁 创建测试目录: test_{rel_path}")
        
        # 生成测试文件名（去掉.yaml，加上.py）
        test_filename = yaml_file.replace('.yaml', '.py')
        test_file = os.path.join(test_dir, test_filename)
        
        # 导入API类
        api_import = f"apimap.{rel_path.replace(os.sep, '.')}.{class_name}Api"
        api_class = f"{class_name}Api"
        
        # 获取方法名
        method_name = self._generate_method_name_from_yaml(yaml_file, test_case)
        
        # 生成测试用例
        test_methods = []
        for idx, case in enumerate(test_case):
            test_method = self._generate_test_method(case, idx, testinfo, method_name)
            test_methods.append(test_method)
        
        # 生成测试文件内容
        content = f'''# -*- coding:utf-8 -*-
"""
{dir_name} 测试用例
自动生成于 {self._get_timestamp()}
YAML文件: {yaml_file}
"""

import pytest
import allure
from {api_import} import {api_class}


@allure.feature("{dir_name}")
class Test{class_name}:
    """{dir_name} 接口测试"""
    
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

    def _generate_test_method(self, test_case, idx, testinfo, method_name):
        """生成测试方法代码"""
        test_name = test_case.get("test_name", f"case_{idx}")
        info = test_case.get("info", "")
        method = test_case.get("method", "GET")
        url = test_case.get("url", "")
        mark = test_case.get("mark", "")
        
        # 生成方法名
        test_method_name = f"test_{self._snake_case(test_name or f'case_{idx}')}"
        
        # 生成方法装饰器
        skip_decorator = f'    @pytest.mark.skip(reason="跳过测试")' if not test_case.get("test_name") else ''
        mark_decorator = f'    @pytest.mark.{mark}' if mark else ''
        
        code = f'''{mark_decorator}
{skip_decorator}
    @allure.story("{info or method} {url}")
    def {test_method_name}(self, api_client):
        """
        {info or f"测试用例 {idx + 1}"}
        请求方法: {method}
        请求URL: {url}
        """
        # 调用API方法
        if hasattr(api_client, '{method_name}'):
            response = getattr(api_client, '{method_name}')()
            assert response is not None, "响应为空"
        else:
            pytest.skip(f"方法 {method_name} 不存在")
'''
        return code

    def _generate_method_name_from_yaml(self, yaml_file, test_case):
        """根据YAML文件名生成方法名"""
        base_name = yaml_file.replace('.yaml', '').replace('_test', '')
        
        # 获取方法类型
        method = 'GET'
        if test_case:
            method = test_case[0].get("method", "GET")
        
        method_lower = method.lower()
        return f"{method_lower}_{self._snake_case(base_name)}"

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
