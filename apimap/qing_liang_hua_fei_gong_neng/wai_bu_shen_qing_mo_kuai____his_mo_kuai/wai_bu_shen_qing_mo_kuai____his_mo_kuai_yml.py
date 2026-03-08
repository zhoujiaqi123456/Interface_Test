# -*- coding:utf-8 -*-
"""
外部申请模块 - his模块 模块API
自动生成于 2026-03-08 17:28:49
"""
from public.base import BaseAPI
from public.login import Login


class wai_bu_shen_qing_mo_kuai____his_mo_kuaiAPI(BaseAPI):
    """外部申请模块 - his模块 接口"""
    
    def __init__(self, base_url=None, token=None, sso_ip=None, url_ip=None):
        """
        初始化
        :param base_url: 基础URL
        :param token: 认证token
        :param sso_ip: SSO服务器IP
        :param url_ip: API服务器IP
        """
        super().__init__(base_url, token)
        self.login = Login(sso_ip, url_ip) if sso_ip and url_ip else None
    
    def verbose(self, data):
        """
        格式化输出
        :param data: 数据
        :return: 格式化后的字符串
        """
        import json
        return json.dumps(data, indent=2, ensure_ascii=False)


    def post_set_his_server_setting28300(self):
        """
        保存his设置
        请求方法: POST
        请求URL: /pf-lite/api/outApply/setHisServerSetting
        
        :return: 响应数据
        """
        self.json_data = self.request('setHisServerSetting28300_test.yaml')
        print(self.verbose(self.json_data))
        return self.json_data


    def post_out_apply_sheet_select28309(self):
        """
        检查单申请 - 选择检查单
        请求方法: POST
        请求URL: /pf-lite/api/outApply/outApplySheetSelect
        
        :return: 响应数据
        """
        self.json_data = self.request('outApplySheetSelect28309_test.yaml')
        print(self.verbose(self.json_data))
        return self.json_data


    def get_get_log_list28304(self):
        """
        获取请求日志
        请求方法: GET
        请求URL: /pf-lite/api/outApply/getLogList
        
        :return: 响应数据
        """
        self.json_data = self.request('getLogList28304_test.yaml')
        print(self.verbose(self.json_data))
        return self.json_data


    def post_out_apply_patient_select28308(self):
        """
        患者申请 - 选择患者
        请求方法: POST
        请求URL: /pf-lite/api/outApply/outApplyPatientSelect
        
        :return: 响应数据
        """
        self.json_data = self.request('outApplyPatientSelect28308_test.yaml')
        print(self.verbose(self.json_data))
        return self.json_data


    def get_get_his_server_setting28299(self):
        """
        获取his设置
        请求方法: GET
        请求URL: /pf-lite/api/outApply/getHisServerSetting
        
        :return: 响应数据
        """
        self.json_data = self.request('getHisServerSetting28299_test.yaml')
        print(self.verbose(self.json_data))
        return self.json_data


    def get_refresh_config28302(self):
        """
        刷新配置
        请求方法: GET
        请求URL: /pf-lite/api/outApply/refreshConfig
        
        :return: 响应数据
        """
        self.json_data = self.request('refreshConfig28302_test.yaml')
        print(self.verbose(self.json_data))
        return self.json_data


    def post_get_agent_apply_patient_page28305(self):
        """
        获取患者申请列表
        请求方法: POST
        请求URL: /pf-lite/api/outApply/getAgentApplyPatientPage
        
        :return: 响应数据
        """
        self.json_data = self.request('getAgentApplyPatientPage28305_test.yaml')
        print(self.verbose(self.json_data))
        return self.json_data


    def post_get_agent_apply_sheet_list_page28306(self):
        """
        获取申请检查单列表
        请求方法: POST
        请求URL: /pf-lite/api/outApply/getAgentApplySheetListPage
        
        :return: 响应数据
        """
        self.json_data = self.request('getAgentApplySheetListPage28306_test.yaml')
        print(self.verbose(self.json_data))
        return self.json_data


    def post_get_agent_apply_sheet_page28307(self):
        """
        获取申请检查单列表
        请求方法: POST
        请求URL: /pf-lite/api/outApply/getAgentApplySheetPage
        
        :return: 响应数据
        """
        self.json_data = self.request('getAgentApplySheetPage28307_test.yaml')
        print(self.verbose(self.json_data))
        return self.json_data


    def get_test_server28301(self):
        """
        测试服务
        请求方法: GET
        请求URL: /pf-lite/api/outApply/testServer
        
        :return: 响应数据
        """
        self.json_data = self.request('testServer28301_test.yaml')
        print(self.verbose(self.json_data))
        return self.json_data


    def get_get_config28303(self):
        """
        获取配置1
        请求方法: GET
        请求URL: /pf-lite/api/outApply/getConfig
        
        :return: 响应数据
        """
        self.json_data = self.request('getConfig28303_test.yaml')
        print(self.verbose(self.json_data))
        return self.json_data

