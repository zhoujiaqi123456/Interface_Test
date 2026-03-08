# -*- coding:utf-8 -*-
"""
设置 模块API
自动生成于 2026-03-08 10:10:14
"""

from public.request_handler import RequestHandler


class 设置Api:
    """设置 接口"""
    
    def __init__(self, base_url=None, token=None):
        """
        初始化
        :param base_url: 基础URL
        :param token: 认证token
        """
        self.request_handler = RequestHandler(base_url, token)
    
    def request(self, yaml_file):
        """
        发送请求
        :param yaml_file: YAML文件名
        :return: 响应数据
        """
        return self.request_handler.request(yaml_file)
    
    def verbose(self, data):
        """
        格式化输出
        :param data: 数据
        :return: 格式化后的字符串
        """
        import json
        return json.dumps(data, indent=2, ensure_ascii=False)


    def post_get_connect_device_type_list28228(self):
        """
        *
        请求方法: POST
        请求URL: /pf-lite/api/settings/getConnectDeviceTypeList
        """
        self.json_data = self.request('getConnectDeviceTypeList28228_test.yaml')
        print(self.verbose(self.json_data))
        return self.json_data


    def post_get_calibration_vol28085(self):
        """
        获取定标桶容积
        请求方法: POST
        请求URL: /pf-lite/api/settings/getCalibrationVol
        """
        self.json_data = self.request('getCalibrationVol28085_test.yaml')
        print(self.verbose(self.json_data))
        return self.json_data


    def post_get_saved_env_params28084(self):
        """
        获取当前的和前一次的环境参数
        请求方法: POST
        请求URL: /pf-lite/api/settings/getSavedEnvParams
        """
        self.json_data = self.request('getSavedEnvParams28084_test.yaml')
        print(self.verbose(self.json_data))
        return self.json_data


    def post_get_report_title_settings28071(self):
        """
        获取报告标题设置
        请求方法: POST
        请求URL: /pf-lite/api/settings/getReportTitleSettings
        """
        self.json_data = self.request('getReportTitleSettings28071_test.yaml')
        print(self.verbose(self.json_data))
        return self.json_data


    def post_get_common_setting28082(self):
        """
        获取通用配置
        请求方法: POST
        请求URL: /pf-lite/api/settings/getCommonSetting
        """
        self.json_data = self.request('getCommonSetting28082_test.yaml')
        print(self.verbose(self.json_data))
        return self.json_data


    def post_set_pred_algorithm_list28077(self):
        """
        设置预计值算法，一次性可以传多个模板设置
        请求方法: POST
        请求URL: /pf-lite/api/settings/setPredAlgorithmList
        """
        self.json_data = self.request('setPredAlgorithmList28077_test.yaml')
        print(self.verbose(self.json_data))
        return self.json_data


    def post_set_ios_verify_standard_param28090(self):
        """
        设置阻抗校准参考值
        请求方法: POST
        请求URL: /pf-lite/api/settings/setIOSVerifyStandardParam
        """
        self.json_data = self.request('setIOSVerifyStandardParam28090_test.yaml')
        print(self.verbose(self.json_data))
        return self.json_data


    def post_get_copywriter_config_remind28093(self):
        """
        文案是否不再提醒
        请求方法: POST
        请求URL: /pf-lite/api/settings/getCopywriterConfigRemind
        """
        self.json_data = self.request('getCopywriterConfigRemind28093_test.yaml')
        print(self.verbose(self.json_data))
        return self.json_data


    def post_set_pred_algorithm28074(self):
        """
        设置预计值算法
        请求方法: POST
        请求URL: /pf-lite/api/settings/setPredAlgorithm
        """
        self.json_data = self.request('setPredAlgorithm28074_test.yaml')
        print(self.verbose(self.json_data))
        return self.json_data


    def post_save_env_params28083(self):
        """
        保存环境参数
        请求方法: POST
        请求URL: /pf-lite/api/settings/saveEnvParams
        """
        self.json_data = self.request('saveEnvParams28083_test.yaml')
        print(self.verbose(self.json_data))
        return self.json_data


    def post_set_qrcode_remark28080(self):
        """
        设置二维码文案
        请求方法: POST
        请求URL: /pf-lite/api/settings/setQrcodeRemark
        """
        self.json_data = self.request('setQrcodeRemark28080_test.yaml')
        print(self.verbose(self.json_data))
        return self.json_data


    def post_get_pred_algorithm28075(self):
        """
        获取预计值算法
        请求方法: POST
        请求URL: /pf-lite/api/settings/getPredAlgorithm
        """
        self.json_data = self.request('getPredAlgorithm28075_test.yaml')
        print(self.verbose(self.json_data))
        return self.json_data


    def post_set_calibration_vol28086(self):
        """
        获取定标桶容积
        请求方法: POST
        请求URL: /pf-lite/api/settings/setCalibrationVol
        """
        self.json_data = self.request('setCalibrationVol28086_test.yaml')
        print(self.verbose(self.json_data))
        return self.json_data


    def post_get_default_report_title_settings28073(self):
        """
        获取报告默认标题
        请求方法: POST
        请求URL: /pf-lite/api/settings/getDefaultReportTitleSettings
        """
        self.json_data = self.request('getDefaultReportTitleSettings28073_test.yaml')
        print(self.verbose(self.json_data))
        return self.json_data


    def post_get_qrcode28079(self):
        """
        获取二维码信息
        请求方法: POST
        请求URL: /pf-lite/api/settings/getQrcode
        """
        self.json_data = self.request('getQrcode28079_test.yaml')
        print(self.verbose(self.json_data))
        return self.json_data


    def post_set_common_setting28081(self):
        """
        设置通用配置
        请求方法: POST
        请求URL: /pf-lite/api/settings/setCommonSetting
        """
        self.json_data = self.request('setCommonSetting28081_test.yaml')
        print(self.verbose(self.json_data))
        return self.json_data


    def post_get_last_update_time28094(self):
        """
        获取上次更新时间
        请求方法: POST
        请求URL: /pf-lite/api/settings/getLastUpdateTime
        """
        self.json_data = self.request('getLastUpdateTime28094_test.yaml')
        print(self.verbose(self.json_data))
        return self.json_data


    def post_get_co2_standard_value28088(self):
        """
        获取CO2标定浓度
        请求方法: POST
        请求URL: /pf-lite/api/settings/getCo2StandardValue
        """
        self.json_data = self.request('getCo2StandardValue28088_test.yaml')
        print(self.verbose(self.json_data))
        return self.json_data


    def post_update_report_title_settings28072(self):
        """
        更新报告标题设置
        请求方法: POST
        请求URL: /pf-lite/api/settings/updateReportTitleSettings
        """
        self.json_data = self.request('updateReportTitleSettings28072_test.yaml')
        print(self.verbose(self.json_data))
        return self.json_data


    def post_get_pred_algorithm_setting_list28076(self):
        """
        获取预计值算法枚举列表
        请求方法: POST
        请求URL: /pf-lite/api/settings/getPredAlgorithmSettingList
        """
        self.json_data = self.request('getPredAlgorithmSettingList28076_test.yaml')
        print(self.verbose(self.json_data))
        return self.json_data


    def post_set_copywriter_config_remind28092(self):
        """
        设置文案不再提醒
        请求方法: POST
        请求URL: /pf-lite/api/settings/setCopywriterConfigRemind
        """
        self.json_data = self.request('setCopywriterConfigRemind28092_test.yaml')
        print(self.verbose(self.json_data))
        return self.json_data


    def post_get_pred_algorithm_list28078(self):
        """
        获取预计值算法，一次性可以传多个模板设置
        请求方法: POST
        请求URL: /pf-lite/api/settings/getPredAlgorithmList
        """
        self.json_data = self.request('getPredAlgorithmList28078_test.yaml')
        print(self.verbose(self.json_data))
        return self.json_data


    def post_get_ios_verify_standard_param28089(self):
        """
        获取阻抗校准参考值
        请求方法: POST
        请求URL: /pf-lite/api/settings/getIOSVerifyStandardParam
        """
        self.json_data = self.request('getIOSVerifyStandardParam28089_test.yaml')
        print(self.verbose(self.json_data))
        return self.json_data


    def post_set_co2_standard_value28087(self):
        """
        设置CO2标定浓度
        请求方法: POST
        请求URL: /pf-lite/api/settings/setCo2StandardValue
        """
        self.json_data = self.request('setCo2StandardValue28087_test.yaml')
        print(self.verbose(self.json_data))
        return self.json_data


    def post_get_copywriter_config28091(self):
        """
        获取文案配置
        请求方法: POST
        请求URL: /pf-lite/api/settings/getCopywriterConfig
        """
        self.json_data = self.request('getCopywriterConfig28091_test.yaml')
        print(self.verbose(self.json_data))
        return self.json_data

