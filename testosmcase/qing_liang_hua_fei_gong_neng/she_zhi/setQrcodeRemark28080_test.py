# -*- coding:utf-8 -*-
"""
设置 测试用例
自动生成于 2026-03-08 17:28:49
YAML文件: setQrcodeRemark28080_test.yaml
"""

import pytest
import allure
from apimap.qing_liang_hua_fei_gong_neng.she_zhi.she_zhi_yml import she_zhiAPI


@allure.feature("设置")
class Testshe_zhi:
    """设置 接口测试"""
    
    @pytest.fixture(scope="class")
    def api_client(self):
        """API客户端"""
        return she_zhiAPI()
    

    @pytest.mark.skip(reason="跳过测试")
    @allure.story("设置二维码文案 /pf-lite/api/settings/setQrcodeRemark")
    def test_case_0(self, api_client):
        """
        设置二维码文案
        请求方法: POST
        请求URL: /pf-lite/api/settings/setQrcodeRemark
        """
        # 调用API方法
        if hasattr(api_client, 'post_set_qrcode_remark28080'):
            response = getattr(api_client, 'post_set_qrcode_remark28080')()
            assert response is not None, "响应为空"
        else:
            pytest.skip(f"方法 post_set_qrcode_remark28080 不存在")

