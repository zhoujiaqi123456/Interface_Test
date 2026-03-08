# -*- coding:utf-8 -*-
"""
导出 测试用例
自动生成于 2026-03-08 17:55:50
YAML文件: export28120_test.yaml
"""

import pytest
import allure
from apimap.lightweight_lung_function.export.export_yml import ExportAPI


@allure.feature("导出")
class TestExport:
    """导出 接口测试"""
    
    @pytest.fixture(scope="class")
    def api_client(self):
        """API客户端"""
        return ExportAPI()
    

    @pytest.mark.skip(reason="跳过测试")
    @allure.story("开始导出 /pf-lite/api/export/export")
    def test_case_0(self, api_client):
        """
        开始导出
        请求方法: POST
        请求URL: /pf-lite/api/export/export
        
        注意：此接口不需要参数，保持空字符串即可
        """
        # 调用API方法（不需要参数）
        response = api_client.post_export28120("")
        
        assert response is not None, "响应为空"

