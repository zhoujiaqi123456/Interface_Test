# -*- coding:utf-8 -*-
'''
@Time       : 2022/4/12 15:28
@Author     : xiongting
@FileName   : BusinessSystem.py
@Description:
'''


import allure
from jsonpath import jsonpath

from public.logger import log
from mode.ModeMapGather import osmmode
from jsonpath import jsonpath

class BussinessSystemApi:

     def bussinessSystem_add(self,*args,**kwargs):
         "新增数据库并回回请求结果"
         with allure.step("新增业务系统"):
             res = osmmode.add_business_system(*args,**kwargs)
             return res


     def bussiness_list_get(self,args):
         """
         TODO:非通用方法,待修改
         :param args:
         :return:
         """
         with allure.step("获取业务系统列表"):
             data = {"name":args.get("bussiness_name")}
             res = osmmode.get_bussiness_list(data)
         with allure.step("获取列表id"):
             business_id = jsonpath(res,"$.result[0].id")
         return business_id,res


     def bussiness_delete_nomal(self,id):
         """根据id删除业务系统"""

         with allure.step("根据传入的id删除业务系统"):
             osmmode.delete_bussiness_by_id(id)
