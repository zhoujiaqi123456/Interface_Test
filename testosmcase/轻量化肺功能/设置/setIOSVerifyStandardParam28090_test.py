# -*- coding:utf-8 -*-
"""
设置 测试用例
自动生成于 2026-03-08 16:15:15
YAML文件: setIOSVerifyStandardParam28090_test.yaml
"""

import pytest
import allure
from apimap.轻量化肺功能.设置.设置_yml import 设置API


@allure.feature("设置")
class Test设置:
    """设置 接口测试"""
    
    @pytest.fixture(scope="class")
    def api_client(self):
        """API客户端"""
        return 设置API()
    

    @pytest.mark.skip(reason="跳过测试")
    @allure.story("设置阻抗校准参考值 /pf-lite/api/settings/setIOSVerifyStandardParam")
    def test_case_0(self, api_client):
        """
        设置阻抗校准参考值
        请求方法: POST
        请求URL: /pf-lite/api/settings/setIOSVerifyStandardParam
        """
        # 调用API方法
        if hasattr(api_client, 'post_set_ios_verify_standard_param28090'):
            response = getattr(api_client, 'post_set_ios_verify_standard_param28090')()
            assert response is not None, "响应为空"
        else:
            pytest.skip(f"方法 post_set_ios_verify_standard_param28090 不存在")

