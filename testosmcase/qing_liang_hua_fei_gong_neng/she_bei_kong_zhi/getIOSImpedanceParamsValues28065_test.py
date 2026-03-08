# -*- coding:utf-8 -*-
"""
设备控制 测试用例
自动生成于 2026-03-08 17:28:49
YAML文件: getIOSImpedanceParamsValues28065_test.yaml
"""

import pytest
import allure
from apimap.qing_liang_hua_fei_gong_neng.she_bei_kong_zhi.she_bei_kong_zhi_yml import she_bei_kong_zhiAPI


@allure.feature("设备控制")
class Testshe_bei_kong_zhi:
    """设备控制 接口测试"""
    
    @pytest.fixture(scope="class")
    def api_client(self):
        """API客户端"""
        return she_bei_kong_zhiAPI()
    

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

