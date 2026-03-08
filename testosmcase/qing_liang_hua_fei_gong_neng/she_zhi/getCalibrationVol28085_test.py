# -*- coding:utf-8 -*-
"""
设置 测试用例
自动生成于 2026-03-08 17:28:49
YAML文件: getCalibrationVol28085_test.yaml
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
    @allure.story("获取定标桶容积 /pf-lite/api/settings/getCalibrationVol")
    def test_case_0(self, api_client):
        """
        获取定标桶容积
        请求方法: POST
        请求URL: /pf-lite/api/settings/getCalibrationVol
        """
        # 调用API方法
        if hasattr(api_client, 'post_get_calibration_vol28085'):
            response = getattr(api_client, 'post_get_calibration_vol28085')()
            assert response is not None, "响应为空"
        else:
            pytest.skip(f"方法 post_get_calibration_vol28085 不存在")

