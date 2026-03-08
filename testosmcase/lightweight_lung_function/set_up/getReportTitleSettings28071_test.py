# -*- coding:utf-8 -*-
"""
设置 测试用例
自动生成于 2026-03-08 17:56:19
YAML文件: getReportTitleSettings28071_test.yaml
"""

import pytest
import allure
from apimap.lightweight_lung_function.set_up.set_up_yml import SetUpAPI


@allure.feature("设置")
class TestSetUp:
    """设置 接口测试"""
    
    @pytest.fixture(scope="class")
    def api_client(self):
        """API客户端"""
        return SetUpAPI()
    

    @pytest.mark.skip(reason="跳过测试")
    @allure.story("获取报告标题设置 /pf-lite/api/settings/getReportTitleSettings")
    def test_case_0(self, api_client):
        """
        获取报告标题设置
        请求方法: POST
        请求URL: /pf-lite/api/settings/getReportTitleSettings
        
        注意：此接口不需要参数，保持空字符串即可
        """
        # 调用API方法（不需要参数）
        response = api_client.post_get_report_title_settings28071("")
        
        assert response is not None, "响应为空"

