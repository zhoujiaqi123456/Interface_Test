# -*- coding:utf-8 -*-
"""
账号相关 测试用例
自动生成于 2026-03-08 16:15:15
YAML文件: set-print-account28297_test.yaml
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
    @allure.story("设置是否云打印账号 /pf-lite/api/account/set-print-account")
    def test_case_0(self, api_client):
        """
        设置是否云打印账号
        请求方法: POST
        请求URL: /pf-lite/api/account/set-print-account
        """
        # 调用API方法
        if hasattr(api_client, 'post_set-print-account28297'):
            response = getattr(api_client, 'post_set-print-account28297')()
            assert response is not None, "响应为空"
        else:
            pytest.skip(f"方法 post_set-print-account28297 不存在")

