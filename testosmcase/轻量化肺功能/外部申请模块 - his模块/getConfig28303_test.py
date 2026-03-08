# -*- coding:utf-8 -*-
"""
外部申请模块 - his模块 测试用例
自动生成于 2026-03-08 10:10:14
YAML文件: getConfig28303_test.yaml
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
    @allure.story("获取配置1 /pf-lite/api/outApply/getConfig")
    def test_case_0(self, api_client):
        """
        获取配置1
        请求方法: GET
        请求URL: /pf-lite/api/outApply/getConfig
        """
        # 调用API方法
        if hasattr(api_client, 'get_get_config28303'):
            response = getattr(api_client, 'get_get_config28303')()
            assert response is not None, "响应为空"
        else:
            pytest.skip(f"方法 get_get_config28303 不存在")

