# -*- coding:utf-8 -*-
"""
设置 测试用例
自动生成于 2026-03-08 10:10:14
YAML文件: saveEnvParams28083_test.yaml
"""

import pytest
import allure
from apimap.轻量化肺功能.设置.设置Api import 设置Api


@allure.feature("设置")
class Test设置:
    """设置 接口测试"""
    
    @pytest.fixture(scope="class")
    def api_client(self):
        """API客户端"""
        return 设置Api()
    

    @pytest.mark.skip(reason="跳过测试")
    @allure.story("保存环境参数 /pf-lite/api/settings/saveEnvParams")
    def test_case_0(self, api_client):
        """
        保存环境参数
        请求方法: POST
        请求URL: /pf-lite/api/settings/saveEnvParams
        """
        # 调用API方法
        if hasattr(api_client, 'post_save_env_params28083'):
            response = getattr(api_client, 'post_save_env_params28083')()
            assert response is not None, "响应为空"
        else:
            pytest.skip(f"方法 post_save_env_params28083 不存在")

