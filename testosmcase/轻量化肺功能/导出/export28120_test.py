# -*- coding:utf-8 -*-
"""
导出 测试用例
自动生成于 2026-03-08 10:10:14
YAML文件: export28120_test.yaml
"""

import pytest
import allure
from apimap.轻量化肺功能.导出.导出Api import 导出Api


@allure.feature("导出")
class Test导出:
    """导出 接口测试"""
    
    @pytest.fixture(scope="class")
    def api_client(self):
        """API客户端"""
        return 导出Api()
    

    @pytest.mark.skip(reason="跳过测试")
    @allure.story("开始导出 /pf-lite/api/export/export")
    def test_case_0(self, api_client):
        """
        开始导出
        请求方法: POST
        请求URL: /pf-lite/api/export/export
        """
        # 调用API方法
        if hasattr(api_client, 'post_export28120'):
            response = getattr(api_client, 'post_export28120')()
            assert response is not None, "响应为空"
        else:
            pytest.skip(f"方法 post_export28120 不存在")

