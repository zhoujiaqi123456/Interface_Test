# -*- coding:utf-8 -*-
'''
@Time       : 2022/4/12 15:51
@Author     : xiongting
@FileName   : test_01_bussiness_add.py
@Description:
'''

import allure
import pytest
from jsonpath import jsonpath

from apimap.ApiMapGather import osmapi
from mode.ModeMapGather import osmmode
from public.load_test_data import CaseYamlParser

@allure.feature("新增业务系统")
class TestBussinessSystem():
    """新增业务系统正常及异常用例
    """
    #初始化用例数据
    inicase = CaseYamlParser("osmasset", "bussiness_add_2435.yaml")

    @allure.story("正常用例")
    @allure.title("添加业务系统成功")
    @allure.description("冒烟用例，添加业务系统")
    @pytest.mark.smoking
    @pytest.mark.osm
    @pytest.mark.XIONGTING
    def test_bussiness_add(self,testdata):
        """新增业务系统成功"""
        with allure.step("添加业务系统"):
            res = osmapi.bussinessSystem_add(testdata)
            ret_value = jsonpath(res,"$.result.name")[0]
            assert ret_value == testdata["name"]



    @allure.story("正常用例")
    @allure.title("添加业务系统成功")
    @allure.description("冒烟用例，添加业务系统")
    @pytest.mark.smoking
    @pytest.mark.osm
    @pytest.mark.XIONGTING
    def test_bussiness_add(self):
        """新增业务系统成功"""
        args = {
            "name":"",
            "need_health": 1,
            "module": ""
        }
        osmmode.get_bussiness_list(args)









