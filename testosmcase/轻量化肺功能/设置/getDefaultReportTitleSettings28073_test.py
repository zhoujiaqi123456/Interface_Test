# -*- coding:utf-8 -*-
"""
设置 测试用例
自动生成于 2026-03-08 16:15:15
YAML文件: getDefaultReportTitleSettings28073_test.yaml
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
    @allure.story("获取报告默认标题 /pf-lite/api/settings/getDefaultReportTitleSettings")
    def test_case_0(self, api_client):
        """
        获取报告默认标题
        请求方法: POST
        请求URL: /pf-lite/api/settings/getDefaultReportTitleSettings
        """
        # 调用API方法
        if hasattr(api_client, 'post_get_default_report_title_settings28073'):
            response = getattr(api_client, 'post_get_default_report_title_settings28073')()
            assert response is not None, "响应为空"
        else:
            pytest.skip(f"方法 post_get_default_report_title_settings28073 不存在")

