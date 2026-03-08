# -*- coding:utf-8 -*-
"""
账号相关 测试用例
自动生成于 2026-03-08 16:15:15
YAML文件: get_user_by_id28299_test.yaml
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
    


    @allure.story("根据ID获取用户信息 /pf-lite/api/account/getUserById")
    def test_test_get_user_by_id(self, api_client):
        """
        根据ID获取用户信息
        请求方法: POST
        请求URL: /pf-lite/api/account/getUserById
        
        注意：此接口需要传递参数，请根据实际情况修改 context 参数
        """
        # 调用API方法，传递参数
        context = {"id": 1}  # 根据实际情况修改参数
        if hasattr(api_client, 'post_get_user_by_id28299'):
            response = getattr(api_client, 'post_get_user_by_id28299')(context=context)
            assert response is not None, "响应为空"
        else:
            pytest.skip(f"方法 post_get_user_by_id28299 不存在")

