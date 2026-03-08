# -*- coding:utf-8 -*-
"""
设备控制 测试用例
自动生成于 2026-03-08 16:15:15
YAML文件: stopTest28061_test.yaml
"""

import pytest
import allure
from apimap.轻量化肺功能.设备控制.设备控制_yml import 设备控制API


@allure.feature("设备控制")
class Test设备控制:
    """设备控制 接口测试"""
    
    @pytest.fixture(scope="class")
    def api_client(self):
        """API客户端"""
        return 设备控制API()
    

    @pytest.mark.skip(reason="跳过测试")
    @allure.story("停止测量 /pf-lite/api/device/stopTest")
    def test_case_0(self, api_client):
        """
        停止测量
        请求方法: POST
        请求URL: /pf-lite/api/device/stopTest
        """
        # 调用API方法
        if hasattr(api_client, 'post_stop_test28061'):
            response = getattr(api_client, 'post_stop_test28061')()
            assert response is not None, "响应为空"
        else:
            pytest.skip(f"方法 post_stop_test28061 不存在")

