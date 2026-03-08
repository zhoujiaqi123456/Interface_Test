# -*- coding:utf-8 -*-
"""
外部申请模块 - his模块 测试用例
自动生成于 2026-03-08 17:56:31
YAML文件: setHisServerSetting28300_test.yaml
"""

import pytest
import allure
from apimap.lightweight_lung_function.external_application_module_his_module.external_application_module_his_module_yml import ExternalApplicationModuleHisModuleAPI


@allure.feature("外部申请模块 - his模块")
class TestExternalApplicationModuleHisModule:
    """外部申请模块 - his模块 接口测试"""
    
    @pytest.fixture(scope="class")
    def api_client(self):
        """API客户端"""
        return ExternalApplicationModuleHisModuleAPI()
    

    @pytest.mark.skip(reason="跳过测试")
    @allure.story("保存his设置 /pf-lite/api/outApply/setHisServerSetting")
    def test_case_0(self, api_client):
        """
        保存his设置
        请求方法: POST
        请求URL: /pf-lite/api/outApply/setHisServerSetting
        
        注意：此接口不需要参数，保持空字符串即可
        """
        # 调用API方法（不需要参数）
        response = api_client.post_set_his_server_setting28300("")
        
        assert response is not None, "响应为空"

