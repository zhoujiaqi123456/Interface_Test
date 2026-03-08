# -*- coding:utf-8 -*-
"""
设备控制 测试用例
自动生成于 2026-03-08 17:55:58
YAML文件: pumpControl28070_test.yaml
"""

import pytest
import allure
from apimap.lightweight_lung_function.device_control.device_control_yml import DeviceControlAPI


@allure.feature("设备控制")
class TestDeviceControl:
    """设备控制 接口测试"""
    
    @pytest.fixture(scope="class")
    def api_client(self):
        """API客户端"""
        return DeviceControlAPI()
    

    @pytest.mark.skip(reason="跳过测试")
    @allure.story("泵控制 /pf-lite/api/device/pumpControl")
    def test_case_0(self, api_client):
        """
        泵控制
        请求方法: POST
        请求URL: /pf-lite/api/device/pumpControl
        
        注意：此接口不需要参数，保持空字符串即可
        """
        # 调用API方法（不需要参数）
        response = api_client.post_pump_control28070("")
        
        assert response is not None, "响应为空"

