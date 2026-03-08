# -*- coding:utf-8 -*-
"""
外部申请模块 - his模块 测试用例
自动生成于 2026-03-08 16:15:15
YAML文件: getAgentApplySheetListPage28306_test.yaml
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
    @allure.story("获取申请检查单列表 /pf-lite/api/outApply/getAgentApplySheetListPage")
    def test_case_0(self, api_client):
        """
        获取申请检查单列表
        请求方法: POST
        请求URL: /pf-lite/api/outApply/getAgentApplySheetListPage
        """
        # 调用API方法
        if hasattr(api_client, 'post_get_agent_apply_sheet_list_page28306'):
            response = getattr(api_client, 'post_get_agent_apply_sheet_list_page28306')()
            assert response is not None, "响应为空"
        else:
            pytest.skip(f"方法 post_get_agent_apply_sheet_list_page28306 不存在")

