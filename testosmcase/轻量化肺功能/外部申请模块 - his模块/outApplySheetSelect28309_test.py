# -*- coding:utf-8 -*-
"""
外部申请模块 - his模块 测试用例
自动生成于 2026-03-08 16:15:15
YAML文件: outApplySheetSelect28309_test.yaml
"""

import pytest
import allure
from apimap.轻量化肺功能.外部申请模块 - his模块.外部申请模块 - his模块_yml import 外部申请模块His模块API


@allure.feature("外部申请模块 - his模块")
class Test外部申请模块His模块:
    """外部申请模块 - his模块 接口测试"""
    
    @pytest.fixture(scope="class")
    def api_client(self):
        """API客户端"""
        return 外部申请模块His模块API()
    

    @pytest.mark.skip(reason="跳过测试")
    @allure.story("检查单申请 - 选择检查单 /pf-lite/api/outApply/outApplySheetSelect")
    def test_case_0(self, api_client):
        """
        检查单申请 - 选择检查单
        请求方法: POST
        请求URL: /pf-lite/api/outApply/outApplySheetSelect
        """
        # 调用API方法
        if hasattr(api_client, 'post_out_apply_sheet_select28309'):
            response = getattr(api_client, 'post_out_apply_sheet_select28309')()
            assert response is not None, "响应为空"
        else:
            pytest.skip(f"方法 post_out_apply_sheet_select28309 不存在")

