# -*- coding:utf-8 -*-
"""
外部申请模块 - his模块 测试用例
自动生成于 2026-03-08 10:10:14
YAML文件: setHisServerSetting28300_test.yaml
"""

import pytest
import allure
from apimap.轻量化肺功能.外部申请模块 - his模块.外部申请模块His模块Api import 外部申请模块His模块Api


@allure.feature("外部申请模块 - his模块")
class Test外部申请模块His模块:
    """外部申请模块 - his模块 接口测试"""
    
    @pytest.fixture(scope="class")
    def api_client(self):
        """API客户端"""
        return 外部申请模块His模块Api()
    

    @pytest.mark.skip(reason="跳过测试")
    @allure.story("保存his设置 /pf-lite/api/outApply/setHisServerSetting")
    def test_case_0(self, api_client):
        """
        保存his设置
        请求方法: POST
        请求URL: /pf-lite/api/outApply/setHisServerSetting
        """
        # 调用API方法
        if hasattr(api_client, 'post_set_his_server_setting28300'):
            response = getattr(api_client, 'post_set_his_server_setting28300')()
            assert response is not None, "响应为空"
        else:
            pytest.skip(f"方法 post_set_his_server_setting28300 不存在")

