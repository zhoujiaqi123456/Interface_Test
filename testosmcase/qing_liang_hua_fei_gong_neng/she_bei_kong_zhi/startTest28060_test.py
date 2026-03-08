# -*- coding:utf-8 -*-
"""
设备控制 测试用例
自动生成于 2026-03-08 17:28:49
YAML文件: startTest28060_test.yaml
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
    @allure.story("开始测量 /pf-lite/api/device/startTest")
    def test_case_0(self, api_client):
        """
        开始测量
        请求方法: POST
        请求URL: /pf-lite/api/device/startTest
        """
        # 调用API方法
        if hasattr(api_client, 'post_start_test28060'):
            response = getattr(api_client, 'post_start_test28060')()
            assert response is not None, "响应为空"
        else:
            pytest.skip(f"方法 post_start_test28060 不存在")

