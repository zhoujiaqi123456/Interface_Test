# -*- coding:utf-8 -*-
"""
设备控制 模块API
自动生成于 2026-03-08 17:28:49
"""
from public.base import BaseAPI
from public.login import Login


class she_bei_kong_zhiAPI(BaseAPI):
    """设备控制 接口"""
    
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


    def post_stop_test28061(self):
        """
        停止测量
        请求方法: POST
        请求URL: /pf-lite/api/device/stopTest
        
        :return: 响应数据
        """
        self.json_data = self.request('stopTest28061_test.yaml')
        print(self.verbose(self.json_data))
        return self.json_data


    def post_refresh_env_params28063(self):
        """
        刷新环境参数
        请求方法: POST
        请求URL: /pf-lite/api/device/refreshEnvParams
        
        :return: 响应数据
        """
        self.json_data = self.request('refreshEnvParams28063_test.yaml')
        print(self.verbose(self.json_data))
        return self.json_data


    def post_start_test28060(self):
        """
        开始测量
        请求方法: POST
        请求URL: /pf-lite/api/device/startTest
        
        :return: 响应数据
        """
        self.json_data = self.request('startTest28060_test.yaml')
        print(self.verbose(self.json_data))
        return self.json_data


    def post_update_firmware_param28066(self):
        """
        固件升级
        请求方法: POST
        请求URL: /pf-lite/api/device/updateFirmwareParam
        
        :return: 响应数据
        """
        self.json_data = self.request('updateFirmwareParam28066_test.yaml')
        print(self.verbose(self.json_data))
        return self.json_data


    def post_pump_control28070(self):
        """
        泵控制
        请求方法: POST
        请求URL: /pf-lite/api/device/pumpControl
        
        :return: 响应数据
        """
        self.json_data = self.request('pumpControl28070_test.yaml')
        print(self.verbose(self.json_data))
        return self.json_data


    def post_get_dev_instrument_info28062(self):
        """
        获取仪器信息
        请求方法: POST
        请求URL: /pf-lite/api/device/getDevInstrumentInfo
        
        :return: 响应数据
        """
        self.json_data = self.request('getDevInstrumentInfo28062_test.yaml')
        print(self.verbose(self.json_data))
        return self.json_data


    def post_get_battery_status28064(self):
        """
        获取设备电量
        请求方法: POST
        请求URL: /pf-lite/api/device/getBatteryStatus
        
        :return: 响应数据
        """
        self.json_data = self.request('getBatteryStatus28064_test.yaml')
        print(self.verbose(self.json_data))
        return self.json_data


    def post_get_ios_impedance_params_values28065(self):
        """
        获取IOS 的 阻抗系统
        请求方法: POST
        请求URL: /pf-lite/api/device/getIOSImpedanceParamsValues
        
        :return: 响应数据
        """
        self.json_data = self.request('getIOSImpedanceParamsValues28065_test.yaml')
        print(self.verbose(self.json_data))
        return self.json_data

