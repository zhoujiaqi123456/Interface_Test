# -*- coding:utf-8 -*-
"""
设置 测试用例
自动生成于 2026-03-08 17:56:19
YAML文件: saveEnvParams28083_test.yaml
"""

import pytest
import allure
from apimap.lightweight_lung_function.set_up.set_up_yml import SetUpAPI


@allure.feature("设置")
class TestSetUp:
    """设置 接口测试"""
    
    @pytest.fixture(scope="class")
    def api_client(self):
        """API客户端"""
        return SetUpAPI()
    

    @pytest.mark.skip(reason="跳过测试")
    @allure.story("保存环境参数 /pf-lite/api/settings/saveEnvParams")
    def test_case_0(self, api_client):
        """
        保存环境参数
        请求方法: POST
        请求URL: /pf-lite/api/settings/saveEnvParams
        
        注意：此接口不需要参数，保持空字符串即可
        """
        # 调用API方法（不需要参数）
        response = api_client.post_save_env_params28083("")
        
        assert response is not None, "响应为空"

