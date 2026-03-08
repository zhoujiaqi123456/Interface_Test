# -*- coding:utf-8 -*-
"""
账号相关 测试用例
自动生成于 2026-03-08 17:28:49
YAML文件: set-print-account28297_test.yaml
"""

import pytest
import allure
from apimap.qing_liang_hua_fei_gong_neng.zhang_hao_xiang_guan.zhang_hao_xiang_guan_yml import zhang_hao_xiang_guanAPI


@allure.feature("账号相关")
class Testzhang_hao_xiang_guan:
    """账号相关 接口测试"""
    
    @pytest.fixture(scope="class")
    def api_client(self):
        """API客户端"""
        return zhang_hao_xiang_guanAPI()
    

    @pytest.mark.skip(reason="跳过测试")
    @allure.story("设置是否云打印账号 /pf-lite/api/account/set-print-account")
    def test_case_0(self, api_client):
        """
        设置是否云打印账号
        请求方法: POST
        请求URL: /pf-lite/api/account/set-print-account
        """
        # 调用API方法
        if hasattr(api_client, 'post_set_print_account28297'):
            response = getattr(api_client, 'post_set_print_account28297')()
            assert response is not None, "响应为空"
        else:
            pytest.skip(f"方法 post_set_print_account28297 不存在")

