# -*- coding:utf-8 -*-
"""
账号相关 测试用例
自动生成于 2026-03-08 17:56:02
YAML文件: login28294_test.yaml
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
    

    @pytest.mark.skip(reason="跳过测试")
    @allure.story("登录 /pf-lite/api/account/login")
    def test_case_0(self, api_client):
        """
        登录
        请求方法: POST
        请求URL: /pf-lite/api/account/login
        
        注意：此接口不需要参数，保持空字符串即可
        """
        # 调用API方法（不需要参数）
        response = api_client.post_login28294("")
        
        assert response is not None, "响应为空"

