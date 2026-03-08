# -*- coding:utf-8 -*-
"""
设备控制 测试用例
自动生成于 2026-03-08 10:10:14
YAML文件: getIOSImpedanceParamsValues28065_test.yaml
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
    @allure.story("获取IOS 的 阻抗系统 /pf-lite/api/device/getIOSImpedanceParamsValues")
    def test_case_0(self, api_client):
        """
        获取IOS 的 阻抗系统
        请求方法: POST
        请求URL: /pf-lite/api/device/getIOSImpedanceParamsValues
        """
        # 调用API方法
        if hasattr(api_client, 'post_get_ios_impedance_params_values28065'):
            response = getattr(api_client, 'post_get_ios_impedance_params_values28065')()
            assert response is not None, "响应为空"
        else:
            pytest.skip(f"方法 post_get_ios_impedance_params_values28065 不存在")

