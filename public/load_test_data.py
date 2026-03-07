# -*- coding:utf-8 -*-
'''
@Time       : 2022/4/12 15:45
@Author     : xiongting
@FileName   : ApiMapGather.py
@Description:
'''
import yaml
import os

import conftest
from public.logger import log


# 字典属性化访问,获取字典内的信息时
class AttrDict:
    def __init__(self, d: dict):
        self.__dict__.update(d if isinstance(d, dict) else {})

    def __setattr__(self, key, value):
        # 允许修改属性
        raise NotImplementedError

    def __repr__(self):
        print(self.__dict__)
        return "<AttrDict {}> ".format(self.__dict__)

    def __len__(self):
        return len(self.__dict__)



class CaseYamlParser:
    """
    用例文件解析器,根据传参方式来
    """
    def __init__(self,folder,filename,rep_dict=None):
        """

        :param folder:  用例所在文件夹名称
        :param filename: 用例文件名称
        :param rep_dict: 替换值的字典，预留位置
        """
        self.yaml_path = os.path.join(conftest.ROOTDIR,"testdata",folder,filename)
        self.rep_dict = rep_dict
        self.casename = ""

    def read_yaml_file(self):
        """
        读取yaml，最终读取结果为
        :param yaml_path: yaml文件的路径
        :return: 转为python格式的yaml数据
        """
        with open(self.yaml_path, encoding='utf-8') as cf:
            try:
                data = yaml.load(cf, Loader=yaml.Loader)
                log.info(f"获取用例成功，文件为{self.yaml_path}")
                return data
            except yaml.parser.ParserError:
                log.error(f"用例格式错误，请修改用例格式")
            except:
                log.error("获取用例失败，请检查，文件为{self.yaml_path}")



    def find_case(self):
        """
        查找单个用例
        :param casename:
        :return:
        """
        try:
            alldata = self.read_yaml_file()
            for data in alldata:
                log.info(f"获取到的用例为{data}")
                if self.casename == data["casename"]:
                    casedata = data
                    return casedata
        except:
            log.info(f"未读取到用例")


    def get_case_headers(self,casename):
        """
        获取用例的headers
        :param casename:
        :return:
        """
        self.casename = casename
        try:
            inidata = self.find_case()
            attrdata = AttrDict(inidata)
            log.info(f"获取用例json成功，为{attrdata.headers}")
            return attrdata.headers
        except:
            log.error(f"该{self.casename}无headers")


    def get_case_params(self,casename):
        """
        获取用例的params
        :param casename:
        :return:
        """
        self.casename = casename
        try:
            inidata = self.find_case()
            attrdata = AttrDict(inidata)
            log.info(f"获取用例json成功，为{attrdata.params}")
            return attrdata.params
        except:
            log.error(f"该{self.casename}无params")


    def get_case_data(self,casename):
        """
        获取用例的data
        :param casename:
        :return:
        """
        self.casename = casename
        try:
            inidata = self.find_case()
            attrdata = AttrDict(inidata)
            log.info(f"获取用例json成功，为{attrdata.data}")
            return attrdata.data
        except:
            log.error(f"该{self.casename}无data")


    def get_case_files(self,casename):
        """
        获取用例的files
        :param casename:
        :return:
        """
        self.casename = casename
        try:
            inidata = self.find_case()
            attrdata = AttrDict(inidata)
            log.info(f"获取用例json成功，为{attrdata.files}")
            return attrdata.files
        except:
            log.error(f"该{self.casename}无files")


    def get_case_json(self,casename):
        """
        获取用例的json
        :param casename:
        :return:
        """
        self.casename = casename
        try:
            inidata = self.find_case()
            attrdata = AttrDict(inidata)
            log.info(f"获取用例json为{attrdata.json}")
            return attrdata.json
        except:
            log.error(f"该{self.casename}无json")


    def replace_case_value(self, rep_value,source_data):
        "使用config内的值替换source"
        new_case = source_data.update(rep_value)
        return new_case




if __name__ == '__main__':
    a = CaseYamlParser("osmasset","assert_sence_case.yaml")
    source_data = a.get_case_json("添加MSSQL无主机资产")
    print(conftest.mssql_nohost)
    data = a.replace_case_value(conftest.mssql_nohost,source_data)
    print(data)




