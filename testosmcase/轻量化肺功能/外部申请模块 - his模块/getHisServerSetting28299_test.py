# -*- coding:utf-8 -*-
"""
外部申请模块 - his模块 测试用例
自动生成于 2026-03-08 16:15:15
YAML文件: getHisServerSetting28299_test.yaml
"""

import pytest
import allure
from apimap.轻量化肺功能.外部申请模块 - his模块.外部申请模块 - his模块_yml import 外部申请模块His模块API


@allure.feature("外部申请模块 - his模块")
class Test外部申请模块His模块:
    """外部申请模块 - his模块 接口测试"""
    
    @pytest.fixture(scope="class")
    def api_client(self):
        """API客户端"""
        return 外部申请模块His模块API()
    

    @pytest.mark.skip(reason="跳过测试")
    @allure.story("获取his设置 /pf-lite/api/outApply/getHisServerSetting")
    def test_case_0(self, api_client):
        """
        获取his设置
        请求方法: GET
        请求URL: /pf-lite/api/outApply/getHisServerSetting
        """
        # 调用API方法
        if hasattr(api_client, 'get_get_his_server_setting28299'):
            response = getattr(api_client, 'get_get_his_server_setting28299')()
            assert response is not None, "响应为空"
        else:
            pytest.skip(f"方法 get_get_his_server_setting28299 不存在")

