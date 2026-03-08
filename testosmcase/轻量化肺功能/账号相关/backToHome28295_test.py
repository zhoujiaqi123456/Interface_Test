# -*- coding:utf-8 -*-
"""
账号相关 测试用例
自动生成于 2026-03-08 16:15:15
YAML文件: backToHome28295_test.yaml
"""

import pytest
import allure
from apimap.轻量化肺功能.账号相关.账号相关_yml import 账号相关API


@allure.feature("账号相关")
class Test账号相关:
    """账号相关 接口测试"""
    
    @pytest.fixture(scope="class")
    def api_client(self):
        """API客户端"""
        return 账号相关API()
    

    @pytest.mark.skip(reason="跳过测试")
    @allure.story("返回到首页 /pf-lite/api/account/backToHome")
    def test_case_0(self, api_client):
        """
        返回到首页
        请求方法: POST
        请求URL: /pf-lite/api/account/backToHome
        """
        # 调用API方法
        if hasattr(api_client, 'post_back_to_home28295'):
            response = getattr(api_client, 'post_back_to_home28295')()
            assert response is not None, "响应为空"
        else:
            pytest.skip(f"方法 post_back_to_home28295 不存在")

