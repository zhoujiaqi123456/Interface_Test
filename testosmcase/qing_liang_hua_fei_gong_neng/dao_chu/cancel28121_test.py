# -*- coding:utf-8 -*-
"""
导出 测试用例
自动生成于 2026-03-08 17:28:49
YAML文件: cancel28121_test.yaml
"""

import pytest
import allure
from apimap.qing_liang_hua_fei_gong_neng.dao_chu.dao_chu_yml import dao_chuAPI


@allure.feature("导出")
class Testdao_chu:
    """导出 接口测试"""
    
    @pytest.fixture(scope="class")
    def api_client(self):
        """API客户端"""
        return dao_chuAPI()
    

    @pytest.mark.skip(reason="跳过测试")
    @allure.story("取消导出 /pf-lite/api/export/cancel")
    def test_case_0(self, api_client):
        """
        取消导出
        请求方法: POST
        请求URL: /pf-lite/api/export/cancel
        """
        # 调用API方法
        if hasattr(api_client, 'post_cancel28121'):
            response = getattr(api_client, 'post_cancel28121')()
            assert response is not None, "响应为空"
        else:
            pytest.skip(f"方法 post_cancel28121 不存在")

