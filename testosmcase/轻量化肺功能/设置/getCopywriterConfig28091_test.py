# -*- coding:utf-8 -*-
"""
设置 测试用例
自动生成于 2026-03-08 16:15:15
YAML文件: getCopywriterConfig28091_test.yaml
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
    @allure.story("获取文案配置 /pf-lite/api/settings/getCopywriterConfig")
    def test_case_0(self, api_client):
        """
        获取文案配置
        请求方法: POST
        请求URL: /pf-lite/api/settings/getCopywriterConfig
        """
        # 调用API方法
        if hasattr(api_client, 'post_get_copywriter_config28091'):
            response = getattr(api_client, 'post_get_copywriter_config28091')()
            assert response is not None, "响应为空"
        else:
            pytest.skip(f"方法 post_get_copywriter_config28091 不存在")

