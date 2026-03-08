# -*- coding:utf-8 -*-
"""
外部申请模块 - his模块 测试用例
自动生成于 2026-03-08 17:28:49
YAML文件: outApplyPatientSelect28308_test.yaml
"""

import pytest
import allure
from apimap.qing_liang_hua_fei_gong_neng.wai_bu_shen_qing_mo_kuai____his_mo_kuai.wai_bu_shen_qing_mo_kuai____his_mo_kuai_yml import wai_bu_shen_qing_mo_kuai____his_mo_kuaiAPI


@allure.feature("外部申请模块 - his模块")
class Testwai_bu_shen_qing_mo_kuai____his_mo_kuai:
    """外部申请模块 - his模块 接口测试"""
    
    @pytest.fixture(scope="class")
    def api_client(self):
        """API客户端"""
        return wai_bu_shen_qing_mo_kuai____his_mo_kuaiAPI()
    

    @pytest.mark.skip(reason="跳过测试")
    @allure.story("患者申请 - 选择患者 /pf-lite/api/outApply/outApplyPatientSelect")
    def test_case_0(self, api_client):
        """
        患者申请 - 选择患者
        请求方法: POST
        请求URL: /pf-lite/api/outApply/outApplyPatientSelect
        """
        # 调用API方法
        if hasattr(api_client, 'post_out_apply_patient_select28308'):
            response = getattr(api_client, 'post_out_apply_patient_select28308')()
            assert response is not None, "响应为空"
        else:
            pytest.skip(f"方法 post_out_apply_patient_select28308 不存在")

