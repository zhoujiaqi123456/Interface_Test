# -*- coding:utf-8 -*-
"""
添加用户 测试用例
自动生成于 2026-03-07 21:40:57
YAML文件: test_add_user_12345.yaml
"""

import pytest
import allure
from apimap.api_test_module.TestModule import TestModuleApi


@allure.feature("test_module")
class Test添加用户:
    """添加用户 接口测试"""
    
    @pytest.fixture(scope="class")
    def api_client(self):
        """API客户端"""
        return TestModuleApi()
    
    @pytest.mark.parametrize("kwargs", [{'url': '/api/user/add', 'method': 'POST', 'headers': {'Authorization': '$token', 'Content-Type': 'application/json'}, 'params': {}, 'data': '', 'json': {'username': '', 'email': '', 'age': 0, 'active': True}, 'timeout': 8}])
    @pytest.mark.smoke

    @allure.story("基本功能测试")
    def test_冒烟测试(self, api_client, kwargs):
        """
        基本功能测试
        
        参数来自YAML和pytest参数化
        """
        with allure.step("发送请求"):
            response = api_client._request(**kwargs)
        
        with allure.step("验证响应"):
            # 基本验证
            assert response.status_code == 200, f"状态码错误: {response.status_code}"
            
            # 验证响应内容
            expected_contains = "success"
            if expected_contains:
                assert expected_contains in response.text, f"响应不包含预期内容: {expected_contains}"
            
            # JSON路径验证
            json_path = "$.code"
            json_value = "0"
            if json_path and json_value:
                from jsonpath import jsonpath
                actual_value = jsonpath(response.json(), json_path)
                assert str(actual_value) == str(json_value), f"JSON路径值不匹配: {actual_value} != {json_value}"

    @pytest.mark.parametrize("kwargs", [{'url': '/api/user/add', 'method': 'POST', 'headers': {'Authorization': '$token', 'Content-Type': 'application/json'}, 'params': {}, 'data': '', 'json': {'username': '', 'email': '', 'age': 0, 'active': True}, 'timeout': 8}])
    @pytest.mark.edge

    @allure.story("参数边界测试")
    def test_边界测试(self, api_client, kwargs):
        """
        参数边界测试
        
        参数来自YAML和pytest参数化
        """
        with allure.step("发送请求"):
            response = api_client._request(**kwargs)
        
        with allure.step("验证响应"):
            # 基本验证
            assert response.status_code == 200, f"状态码错误: {response.status_code}"
            
            # 验证响应内容
            expected_contains = ""
            if expected_contains:
                assert expected_contains in response.text, f"响应不包含预期内容: {expected_contains}"
            
            # JSON路径验证
            json_path = ""
            json_value = ""
            if json_path and json_value:
                from jsonpath import jsonpath
                actual_value = jsonpath(response.json(), json_path)
                assert str(actual_value) == str(json_value), f"JSON路径值不匹配: {actual_value} != {json_value}"

