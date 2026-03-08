# -*- coding:utf-8 -*-
"""
设备控制 测试用例
自动生成于 2026-03-08 10:10:14
YAML文件: updateFirmwareParam28066_test.yaml
"""

import pytest
import allure
from apimap.轻量化肺功能.设备控制.设备控制Api import 设备控制Api


@allure.feature("设备控制")
class Test设备控制:
    """设备控制 接口测试"""
    
    @pytest.fixture(scope="class")
    def api_client(self):
        """API客户端"""
        return 设备控制Api()
    

    @pytest.mark.skip(reason="跳过测试")
    @allure.story("固件升级 /pf-lite/api/device/updateFirmwareParam")
    def test_case_0(self, api_client):
        """
        固件升级
        请求方法: POST
        请求URL: /pf-lite/api/device/updateFirmwareParam
        """
        # 调用API方法
        if hasattr(api_client, 'post_update_firmware_param28066'):
            response = getattr(api_client, 'post_update_firmware_param28066')()
            assert response is not None, "响应为空"
        else:
            pytest.skip(f"方法 post_update_firmware_param28066 不存在")

