# -*- coding:utf-8 -*-
"""
账号相关 测试用例
自动生成于 2026-03-08 17:56:02
YAML文件: get_user_by_id28299_test.yaml
"""

import pytest
import allure
from apimap.lightweight_lung_function.account_related.account_related_yml import AccountRelatedAPI


@allure.feature("账号相关")
class TestAccountRelated:
    """账号相关 接口测试"""
    
    @pytest.fixture(scope="class")
    def api_client(self):
        """API客户端"""
        return AccountRelatedAPI()
    


    @allure.story("根据ID获取用户信息 /pf-lite/api/account/getUserById")
    def test_test_get_user_by_id(self, api_client):
        """
        根据ID获取用户信息
        请求方法: POST
        请求URL: /pf-lite/api/account/getUserById
        
        注意：此接口需要传递参数
        """
        # 调用API方法，传递参数
        # 方式1：字符串参数（适合单个ID）
        response = api_client.post_get_user_by_id28299("1")
        
        # 方式2：字典参数（适合多个参数）
        # response = api_client.post_get_user_by_id28299({"userId": 1, "name": "test"})
        
        assert response is not None, "响应为空"

