# -*- coding:utf-8 -*-
"""
账号相关 测试用例
自动生成于 2026-03-08 10:10:14
YAML文件: login28294_test.yaml
"""

import pytest
import allure
from apimap.轻量化肺功能.账号相关.账号相关Api import 账号相关Api


@allure.feature("账号相关")
class Test账号相关:
    """账号相关 接口测试"""
    
    @pytest.fixture(scope="class")
    def api_client(self):
        """API客户端"""
        return 账号相关Api()
    

    @pytest.mark.skip(reason="跳过测试")
    @allure.story("登录 /pf-lite/api/account/login")
    def test_case_0(self, api_client):
        """
        登录
        请求方法: POST
        请求URL: /pf-lite/api/account/login
        """
        # 调用API方法
        if hasattr(api_client, 'post_login28294'):
            response = getattr(api_client, 'post_login28294')()
            assert response is not None, "响应为空"
        else:
            pytest.skip(f"方法 post_login28294 不存在")

