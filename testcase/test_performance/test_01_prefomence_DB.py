# -*- coding:utf-8 -*-
'''
@Time       : 2022/7/12 17:41
@Author     : xiongting
@FileName   : test_01_prefomence_DB.py
@Description:
'''


import allure
import pytest

from apimap.ApiMapGather import osmapi
from public.load_test_data import CaseYamlParser
from conftest import mssql_normal,orale_cdb,mysql7
from public.logger import log



@allure.feature("性能诊断数据库资源")
class TestPerfomanceDB:
    """新增业务系统正常及异常用例"""
    #传入conftest内的无主机字段获取IP，得到db_id，请求
    data = {
         "ip": mssql_normal["ip"]
     }
    opdata = {
         "ip": orale_cdb["ip"]
     }
    mysql_7_data = {
        "ip": mysql7["ip"]
    }


###############################mssql 性能诊断相关case#############################
    @allure.story("MSSQL性能诊断")
    @allure.title("login每秒登录数")
    @allure.description("mssql性能诊断图表,ID:3083")
    @pytest.mark.smoking
    @pytest.mark.osm
    @pytest.mark.XIONGTING
    @pytest.mark.parametrize("testdata",[data])
    def test_mssql_per_picture_login_get(self, testdata):
        with allure.step("更新query_filed内容"):
            testdata["query_filed"] = "logins"
        with allure.step("断言返回值"):
            res = osmapi.mssql_performance_picture_get(testdata)
            if len(res.get("result")) == 0:
                assert 1 != 1
            else:
                for datas in res.get("result"):
                    for data in datas.get("data"):
                        values = data.get("y")
                        for value in values:
                            assert value is not None



    @allure.story("MSSQL性能诊断")
    @allure.title("activesessions活动会话数")
    @allure.description("mssql性能诊断图表,ID:3083")
    @pytest.mark.smoking
    @pytest.mark.osm
    @pytest.mark.XIONGTING
    @pytest.mark.parametrize("testdata",[data])
    def test_mssql_per_picture_activesessions_get(self, testdata):
        with allure.step("更新query_filed内容"):
            testdata["query_filed"] = "activesessions"
        with allure.step("断言返回值"):
            res = osmapi.mssql_performance_picture_get(testdata)
            if len(res.get("result")) == 0:
                assert 1 != 1
            else:
                for datas in res.get("result"):
                    for data in datas.get("data"):
                        values = data.get("y")
                        for value in values:
                            assert value is not None


    @allure.story("MSSQL性能诊断")
    @allure.title("hardparse活动会话数")
    @allure.description("mssql性能诊断图表,ID:3083")
    @pytest.mark.smoking
    @pytest.mark.osm
    @pytest.mark.XIONGTING
    @pytest.mark.parametrize("testdata",[data])
    def test_mssql_per_picture_hardparse_get(self, testdata):
        with allure.step("更新query_filed内容"):
            testdata["query_filed"] = "hardparse"
        with allure.step("断言返回值"):
            res = osmapi.mssql_performance_picture_get(testdata)
            if len(res.get("result")) == 0:
                assert 1 != 1
            else:
                for datas in res.get("result"):
                    for data in datas.get("data"):
                        values = data.get("y")
                        for value in values:
                            assert value is not None


    @allure.story("MSSQL性能诊断")
    @allure.title("txlocks活动会话数")
    @allure.description("mssql性能诊断图表,ID:3083")
    @pytest.mark.smoking
    @pytest.mark.osm
    @pytest.mark.XIONGTING
    @pytest.mark.parametrize("testdata",[data])
    def test_mssql_per_picture_txlocks_get(self, testdata):
        with allure.step("更新query_filed内容"):
            testdata["query_filed"] = "txlocks"
        with allure.step("断言返回值"):
            res = osmapi.mssql_performance_picture_get(testdata)
            if len(res.get("result")) == 0:
                assert 1 != 1
            else:
                for datas in res.get("result"):
                    for data in datas.get("data"):
                        values = data.get("y")
                        for value in values:
                            assert value is not None



    @allure.story("MSSQL性能诊断")
    @allure.title("activetmptables活动会话数")
    @allure.description("mssql性能诊断图表,ID:3083")
    @pytest.mark.smoking
    @pytest.mark.osm
    @pytest.mark.XIONGTING
    @pytest.mark.parametrize("testdata",[data])
    def test_mssql_per_picture_activetmptables_get(self, testdata):
        with allure.step("更新query_filed内容"):
            testdata["query_filed"] = "activetmptables"
        with allure.step("断言返回值"):
            res = osmapi.mssql_performance_picture_get(testdata)
            if len(res.get("result")) ==0:
                assert  1 !=1
            else:
                for datas in res.get("result"):
                    for data in datas.get("data"):
                        values = data.get("y")
                        for value in values:
                            assert value is not None


    @allure.story("MSSQL性能诊断")
    @allure.title("activetmptables活动会话数")
    @allure.description("mssql性能诊断图表,ID:3083")
    @pytest.mark.smoking
    @pytest.mark.osm
    @pytest.mark.XIONGTING
    @pytest.mark.parametrize("testdata",[data])
    def test_mssql_per_picture_activetmptables_get(self, testdata):
        with allure.step("更新query_filed内容"):
            testdata["query_filed"] = "activetmptables"
        with allure.step("断言返回值"):
            res = osmapi.mssql_performance_picture_get(testdata)
            if len(res.get("result")) ==0:
                log.info("返回的result为空")
                assert  1 !=1
            else:
                for datas in res.get("result"):
                    for data in datas.get("data"):
                        values = data.get("y")
                        for value in values:
                            assert value is not None



    @allure.story("MSSQL性能诊断")
    @allure.title("mssql-硬解析次数-详情")
    @allure.description("mssql-硬解析次数-详情,ID:4843")
    @pytest.mark.smoking
    @pytest.mark.osm
    @pytest.mark.XIONGTING
    @pytest.mark.parametrize("testdata",[data])
    def test_performance_logins_detail_get(self, testdata):
        with allure.step("更新query_filed内容"):
            testdata["query_filed"] = "logins"
        with allure.step("获取response"):
            res = osmapi.mssql_performance_logins_detail_get(testdata)
        with allure.step("断言返回的内容都有值"):
            if len(res.get("result")) == 0:
                log.info("返回的result为空")
                assert 1 != 1
            else:
                for datas in res.get("result"):
                    for _,v in datas.items():
                        assert v is not None



    @allure.story("MSSQL性能诊断")
    @allure.title("mssql-tx锁-详情")
    @allure.description("mssql-tx锁-详情,ID:4849")
    @pytest.mark.smoking
    @pytest.mark.osm
    @pytest.mark.XIONGTING
    @pytest.mark.parametrize("testdata",[data])
    def test_mssql_performance_txlocks_detail_get(self, testdata):
        with allure.step("更新query_filed内容"):
            testdata["query_filed"] = "txlocks"
        with allure.step("获取response"):
            res = osmapi.mssql_performance_txlocks_detail_get(testdata)
        with allure.step("断言返回的内容都有值"):
            if len(res.get("result")) == 0:
                log.info("返回的result为空")
                assert 1 != 1
            else:
                for datas in res.get("result"):
                    for _,v in datas.items():
                        assert v is not None



    @allure.story("MSSQL性能诊断")
    @allure.title("mssql-临时表-详情")
    @allure.description("mssql-临时表-详情,ID:4855")
    @pytest.mark.smoking
    @pytest.mark.osm
    @pytest.mark.XIONGTING
    @pytest.mark.parametrize("testdata",[data])
    def test_mssql_performance_activetmptable_detail_get(self, testdata):
        with allure.step("更新query_filed内容"):
            testdata["query_filed"] = "activetmptables"
        with allure.step("获取response"):
            res = osmapi.mssql_performance_activetmptable_detail_get(testdata)
        with allure.step("断言返回的内容都有值"):
            if len(res.get("result")) == 0:
                log.info("返回的result为空")
                assert 1 != 1
            else:
                for datas in res.get("result"):
                    for _,v in datas.items():
                        assert v is not None




    @allure.story("MSSQL性能诊断")
    @allure.title("mssql-硬解析次数-详情")
    @allure.description("mssql-硬解析次数-详情,ID:3085")
    @pytest.mark.smoking
    @pytest.mark.osm
    @pytest.mark.XIONGTING
    @pytest.mark.parametrize("testdata",[data])
    def test_mssql_performance_hardparse_detail_get(self, testdata):
        with allure.step("更新query_filed内容"):
            testdata["query_filed"] = "hardparse"
        with allure.step("获取response"):
            res = osmapi.mssql_performance_hardparse_detail_get(testdata)
        with allure.step("断言返回的内容都有值"):
            if len(res.get("result")) == 0:
                log.info("返回的result为空")
                assert 1 != 1
            else:
                for datas in res.get("result"):
                    for _,v in datas.items():
                        assert v is not None


    @allure.story("MSSQL性能诊断")
    @allure.title("mssql-活动会话数-详情")
    @allure.description("mssql-活动会话数-详情,ID:3087")
    @pytest.mark.smoking
    @pytest.mark.osm
    @pytest.mark.XIONGTING
    @pytest.mark.parametrize("testdata",[data])
    def test_mssql_performance_activesessions_detail_get(self, testdata):
        with allure.step("更新query_filed内容"):
            testdata["query_filed"] = "activesessions"
        with allure.step("获取response"):
            res = osmapi.mssql_performance_activesessions_detail_get(testdata)
        with allure.step("断言返回的内容都有值"):
            if len(res.get("result")) == 0:
                log.info("返回的result为空")
                assert 1 != 1
            else:
                for datas in res.get("result"):
                    for _,v in datas.items():
                        assert v is not None



############################### Oracle 性能诊断相关case  ##################################
    @allure.story("Oracle性能诊断数据库资源")
    @allure.title("oracle性能诊断接口")
    @allure.description("oracle性能诊断接口——每秒新增连接数获取,ID:2759")
    @pytest.mark.smoking
    @pytest.mark.osm
    @pytest.mark.XIONGTING
    @pytest.mark.parametrize("testdata",[opdata])
    def test_oracle_performance_diagnosis_new_conn_per_sec_get(self, testdata):
        with allure.step("更新testdata里的query_filed信息"):
            testdata["query_filed"] = "new_conn_per_sec"
        with allure.step("获取response"):
            res = osmapi.oracle_performance_diagnosis_get(testdata)
        with allure.step("断言返回的内容都有值"):
            if len(res.get("result")) == 0:
                log.info("返回的result为空")
                assert 1 != 1
            else:
                for datas in res.get("result"):
                    for data in datas.get("data"):
                        values = data.get("y")
                        for value in values:
                            assert value is not None



    @allure.story("Oracle性能诊断数据库资源")
    @allure.title("oracle性能诊断接口")
    @allure.description("oracle性能诊断接口_活动会话数获取,ID:2759")
    @pytest.mark.smoking
    @pytest.mark.osm
    @pytest.mark.XIONGTING
    @pytest.mark.parametrize("testdata",[opdata])
    def test_oracle_performance_diagnosis_active_session_get(self, testdata):
        with allure.step("更新testdata里的query_filed信息"):
            testdata["query_filed"] = "active_session"
        with allure.step("获取response"):
            res = osmapi.oracle_performance_diagnosis_get(testdata)
        with allure.step("断言返回的内容都有值"):
            if len(res.get("result")) == 0:
                log.info("返回的result为空")
                assert 1 != 1
            else:
                for datas in res.get("result"):
                    for data in datas.get("data"):
                        values = data.get("y")
                        for value in values:
                            assert value is not None



    @allure.story("Oracle性能诊断数据库资源")
    @allure.title("oracle性能诊断接口")
    @allure.description("oracle性能诊断接口_数据库连接使用率获取,ID:2759")
    @pytest.mark.smoking
    @pytest.mark.osm
    @pytest.mark.XIONGTING
    @pytest.mark.parametrize("testdata",[opdata])
    def test_oracle_performance_diagnosis_conn_used_pct_get(self, testdata):
        with allure.step("更新testdata里的query_filed信息"):
            testdata["query_filed"] = "conn_used_pct"
        with allure.step("获取response"):
            res = osmapi.oracle_performance_diagnosis_get(testdata)
        with allure.step("断言返回的内容都有值"):
            if len(res.get("result")) == 0:
                log.info("返回的result为空")
                assert 1 != 1
            else:
                for datas in res.get("result"):
                    for data in datas.get("data"):
                        values = data.get("y")
                        for value in values:
                            assert value is not None



    @allure.story("Oracle性能诊断数据库资源")
    @allure.title("硬解析延迟占比")
    @allure.description("硬解析延迟占比,ID:2661")
    @pytest.mark.smoking
    @pytest.mark.osm
    @pytest.mark.XIONGTING
    @pytest.mark.parametrize("testdata",[opdata])
    def test_oracle_performance_hardparsetimepct_get(self, testdata):
        with allure.step("获取response"):
            res = osmapi.oracle_performance_hardparsetimepct_get(testdata)
        with allure.step("断言返回的内容都有值"):
            if len(res.get("result")) == 0:
                log.info("返回的result为空")
                assert 1 != 1
            else:
                for datas in res.get("result"):
                    for data in datas.get("data"):
                        values = data.get("y")
                        for value in values:
                            assert value is not None



    @allure.story("Oracle性能诊断数据库资源")
    @allure.title("资源冲突-并发延迟占比")
    @allure.description("资源冲突-并发延迟占比,ID:2655")
    @pytest.mark.smoking
    @pytest.mark.osm
    @pytest.mark.XIONGTING
    @pytest.mark.parametrize("testdata",[opdata])
    def test_oracle_performance_resource_conflict_concurrency_get(self, testdata):
        with allure.step("获取response"):
            res = osmapi.oracle_performance_loginfo_resource_conflict_concurrency_get(testdata)
        with allure.step("断言返回的内容都有值"):
            if len(res.get("result")) == 0:
                log.info("返回的result为空")
                assert 1 != 1
            else:
                for datas in res.get("result"):
                    for data in datas.get("data"):
                        values = data.get("y")
                        for value in values:
                            assert value is not None


    @allure.story("Oracle性能诊断数据库资源")
    @allure.title("每秒硬解析次数")
    @allure.description("每秒硬解析次数,ID:2667")
    @pytest.mark.smoking
    @pytest.mark.osm
    @pytest.mark.XIONGTING
    @pytest.mark.parametrize("testdata",[opdata])
    def test_oracle_performance_hardparsecountops_get(self, testdata):
        with allure.step("获取response"):
            res = osmapi.oracle_performance_hardparsecountops_get(testdata)
        with allure.step("断言返回的内容都有值"):
            if len(res.get("result")) == 0:
                log.info("返回的result为空")
                assert 1 != 1
            else:
                for datas in res.get("result"):
                    for data in datas.get("data"):
                        values = data.get("y")
                        for value in values:
                            assert value is not None



    @allure.story("Oracle性能诊断数据库资源")
    @allure.title("DBtime")
    @allure.description("DBtime,ID:2699")
    @pytest.mark.smoking
    @pytest.mark.osm
    @pytest.mark.XIONGTING
    @pytest.mark.parametrize("testdata",[opdata])
    def test_oracle_performance_dbtime_info_get(self, testdata):
        with allure.step("获取response"):
            res = osmapi.oracle_performance_dbtime_info_get(testdata)
        with allure.step("断言返回的内容都有值"):
            if len(res.get("result")) == 0:
                log.info("返回的result为空")
                assert 1 != 1
            else:
                for datas in res.get("result"):
                    for data in datas.get("data"):
                        values = data.get("y")
                        for value in values:
                            assert value is not None



    @allure.story("Oracle性能诊断数据库资源")
    @allure.title("登录延迟占比")
    @allure.description("登录延迟占比,ID:2665")
    @pytest.mark.smoking
    @pytest.mark.osm
    @pytest.mark.XIONGTING
    @pytest.mark.parametrize("testdata",[opdata])
    def test_oracle_performance_conntimepct_get(self, testdata):
        with allure.step("获取response"):
            res = osmapi.oracle_performance_conntimepct_get(testdata)
        with allure.step("断言返回的内容都有值"):
            if len(res.get("result")) == 0:
                log.info("返回的result为空")
                assert 1 != 1
            else:
                for datas in res.get("result"):
                    for data in datas.get("data"):
                        values = data.get("y")
                        for value in values:
                            assert value is not None




    @allure.story("Oracle性能诊断数据库资源")
    @allure.title("序列获取时间占比")
    @allure.description("序列获取时间占比,ID:2663")
    @pytest.mark.smoking
    @pytest.mark.osm
    @pytest.mark.XIONGTING
    @pytest.mark.parametrize("testdata",[opdata])
    def test_oracle_performance_seqloadtimepct_get(self, testdata):
        with allure.step("获取response"):
            res = osmapi.oracle_performance_seqloadtimepct_get(testdata)
        with allure.step("断言返回的内容都有值"):
            if len(res.get("result")) == 0:
                log.info("返回的result为空")
                assert 1 != 1
            else:
                for datas in res.get("result"):
                    for data in datas.get("data"):
                        values = data.get("y")
                        for value in values:
                            assert value is not None



    @allure.story("Oracle性能诊断数据库资源")
    @allure.title("锁信息")
    @allure.description("锁信息 ID:2631")
    @pytest.mark.smoking
    @pytest.mark.osm
    @pytest.mark.XIONGTING
    @pytest.mark.parametrize("testdata",[opdata])
    def test_oracle_performance_lock_info_get(self, testdata):
        with allure.step("获取response"):
            res = osmapi.oracle_performance_lock_info_get(testdata)
        with allure.step("断言返回的内容都有值"):
            if len(res.get("result")) == 0:
                log.info("返回的result为空")
                assert 1 != 1
            else:
                for datas in res.get("result"):
                    for data in datas.get("data"):
                        values = data.get("y")
                        for value in values:
                            assert value is not None



    @allure.story("Oracle性能诊断数据库资源")
    @allure.title("资源冲突-应用等待占比")
    @allure.description("资源冲突-应用等待占比 ID:2629")
    @pytest.mark.smoking
    @pytest.mark.osm
    @pytest.mark.XIONGTING
    @pytest.mark.parametrize("testdata",[opdata])
    def test_oracle_performance_resource_conflict_application_get(self, testdata):
        with allure.step("获取response"):
            res = osmapi.oracle_performance_resource_conflict_application_get(testdata)
        with allure.step("断言返回的内容都有值"):
            if len(res.get("result")) == 0:
                log.info("返回的result为空")
                assert 1 != 1
            else:
                for datas in res.get("result"):
                    for data in datas.get("data"):
                        values = data.get("y")
                        for value in values:
                            assert value is not None




    @allure.story("Oracle性能诊断数据库资源")
    @allure.title("资源冲突-配置延迟占比")
    @allure.description("资源冲突-配置延迟占比 ID:2653")
    @pytest.mark.smoking
    @pytest.mark.osm
    @pytest.mark.XIONGTING
    @pytest.mark.parametrize("testdata",[opdata])
    def test_oracle_performance_resource_conflict_coniguration_get(self, testdata):
        with allure.step("获取response"):
            res = osmapi.get_oracle_performance_resource_conflict_configuration(testdata)
        with allure.step("断言返回的内容都有值"):
            if len(res.get("result")) == 0:
                log.info("返回的result为空")
                assert 1 != 1
            else:
                for datas in res.get("result"):
                    for data in datas.get("data"):
                        values = data.get("y")
                        for value in values:
                            assert value is not None





#################################ORACLE 性能诊断二级详情  #########################################
    @allure.story("Oracle性能诊断数据库资源详情")
    @allure.title("数据库登录详情-详情")
    @allure.description("数据库登录详情，每秒新增连接数,ID:2641")
    @pytest.mark.smoking
    @pytest.mark.osm
    @pytest.mark.XIONGTING
    @pytest.mark.xfail
    @pytest.mark.parametrize("testdata",[opdata])
    def test_oracle_performance_login_info_sessions_get(self,testdata):
        with allure.step("传入获取time的query_filed"):
            testdata["query_filed"] = "new_conn_per_sec"
        with allure.step("获取response"):
            res = osmapi.oracle_performance_login_info_sessions_get(testdata)
        with allure.step("断言返回的内容都有值"):
            if len(res.get("result")) == 0:
                log.info("返回的result为空,请确认内容是否确正")
                assert 1 != 1
            else:
                for datas in res.get("result"):
                    for _,v in datas.items():
                         assert v is not None   #如果值是数字，刚判断是否为null


    @allure.story("Oracle性能诊断数据库资源详情")
    @allure.title("数据库会话数详情-详情")
    @allure.description("数据库会话数详情,ID：2643")
    @pytest.mark.smoking
    @pytest.mark.osm
    @pytest.mark.XIONGTING
    @pytest.mark.parametrize("testdata",[opdata])
    def test_oracle_performance_session_info_get(self,testdata):
        with allure.step("传入获取time的query_filed"):
            testdata["query_filed"] = "active_session"
        with allure.step("获取response"):
            res = osmapi.oracle_performance_session_info_get(testdata)
        with allure.step("断言返回的内容都有值"):
            if len(res.get("result")) == 0:
                log.info("返回的result为空")
                assert 1 != 1
            else:
                for datas in res.get("result"):
                    for _,v in datas.items():
                           assert v is not None   #如果值是数字，刚判断是否为null



    @allure.story("Oracle性能诊断数据库资源详情")
    @allure.title("数据库连接使用率-详情")
    @allure.description("oracle-数据库连接使用率-详情 ID：4345")
    @pytest.mark.smoking
    @pytest.mark.osm
    @pytest.mark.XIONGTING
    @pytest.mark.parametrize("testdata",[opdata])
    def test_oracle_performance_connuse_details_get(self, testdata):
        with allure.step("传入获取time的query_filed"):
            testdata["query_filed"] = "conn_used_pct"
        with allure.step("获取response"):
            res = osmapi.oracle_performance_connuse_details_get(testdata)
        with allure.step("断言返回的内容都有值"):
            if len(res.get("result")) == 0:
                log.info("返回的result为空")
                assert 1 != 1
            else:
                for datas in res.get("result"):
                    for _,v in datas.items():
                           assert v is not None   #如果值是数字，刚判断是否为null



    @allure.story("Oracle性能诊断数据库资源详情")
    @allure.title("应用锁等待延迟占比-详情")
    @allure.description("应用锁等待延迟占比-详情 ID：2633")
    @pytest.mark.smoking
    @pytest.mark.osm
    @pytest.mark.XIONGTING
    @pytest.mark.xfail
    @pytest.mark.parametrize("testdata",[opdata])
    def test_oracle_performance_application_events_get(self, testdata):
        with allure.step("获取response"):
            res = osmapi.oracle_performance_application_events_get(testdata)
        with allure.step("断言返回的内容都有值"):
            if len(res.get("result")) == 0:
                log.info("返回的result为空")
                assert 1 != 1
            else:
                for datas in res.get("result"):
                    for _,v in datas.items():
                           assert v is not None   #如果值是数字，刚判断是否为null



    @allure.story("Oracle性能诊断数据库资源详情")
    @allure.title("并发延迟占比-详情")
    @allure.description("并发延迟占比-详情 ID：2659")
    @pytest.mark.smoking
    @pytest.mark.osm
    @pytest.mark.XIONGTING
    @pytest.mark.xfail
    @pytest.mark.parametrize("testdata",[opdata])
    def test_oracle_performance_concurrency_events_get(self, testdata):
        with allure.step("获取response"):
            res = osmapi.oracle_performance_concurrency_events_get(testdata)
        with allure.step("断言返回的内容都有值"):
            if len(res.get("result")) == 0:
                log.info("返回的result为空")
                assert 1 != 1
            else:
                for datas in res.get("result"):
                    for _,v in datas.items():
                           assert v is not None   #如果值是数字，刚判断是否为null



    @allure.story("Oracle性能诊断数据库资源详情")
    @allure.title("配置延迟占比-详情")
    @allure.description("配置延迟占比-详情 ID：2657")
    @pytest.mark.smoking
    @pytest.mark.osm
    @pytest.mark.XIONGTING
    @pytest.mark.xfail
    @pytest.mark.parametrize("testdata",[opdata])
    def test_oracle_performance_configuration_events_get(self, testdata):
        with allure.step("获取response"):
            res = osmapi.oracle_performance_configuration_events_get(testdata)
        with allure.step("断言返回的内容都有值"):
            if len(res.get("result")) == 0:
                log.info("返回的result为空")
                assert 1 != 1
            else:
                for datas in res.get("result"):
                    for _,v in datas.items():
                           assert v is not None   #如果值是数字，刚判断是否为null



    @allure.story("Oracle性能诊断数据库资源详情")
    @allure.title("oracle每秒硬解析一级下钻-详情")
    @allure.description("oracle每秒硬解析一级下钻-详情 ID：5541")
    @pytest.mark.smoking
    @pytest.mark.osm
    @pytest.mark.XIONGTING
    @pytest.mark.parametrize("testdata",[opdata])
    def test_oracle_performance_hardparse_sqls_get(self, testdata):
        with allure.step("获取response"):
            res = osmapi.oracle_performance_hardparse_sqls_get(testdata)
        with allure.step("断言返回的内容都有值"):
            if len(res.get("result")) == 0:
                log.info("返回的result为空")
                assert 1 != 1
            else:
                for datas in res.get("result"):
                    for _,v in datas.items():
                           assert v is not None   #如果值是数字，刚判断是否为null




    @allure.story("Oracle性能诊断数据库资源详情")
    @allure.title("oracle每秒硬解析二级下钻-详情")
    @allure.description("oracle每秒硬解析二级下钻-详情 ID：5541")
    @pytest.mark.smoking
    @pytest.mark.osm
    @pytest.mark.XIONGTING
    @pytest.mark.parametrize("testdata", [opdata])
    def test_oracle_performance_hardparse_sqls_level_two_get(self, testdata):
        with allure.step("获取response"):
            res = osmapi.oracle_performance_hardparse_sqls_level_two(testdata)
        with allure.step("断言返回的内容都有值"):
            if len(res.get("result")) == 0:
                log.info("返回的result为空")
                assert 1 != 1
            else:
                for datas in res.get("result"):
                    for _, v in datas.items():
                        assert v is not None  # 如果值是数字，刚判断是否为null



    @allure.story("Oracle性能诊断数据库资源详情")
    @allure.title("锁信息详情")
    @allure.description("锁信息详情 ID：2635")
    @pytest.mark.smoking
    @pytest.mark.osm
    @pytest.mark.XIONGTING
    @pytest.mark.parametrize("testdata",[opdata])
    def test_oracle_performance_lock_sessions_get(self, testdata):
        with allure.step("获取response"):
            res = osmapi.oracle_performance_lock_sessions_get(testdata)
        with allure.step("断言返回的内容都有值"):
            if len(res.get("result")) == 0:
                log.info("返回的result为空")
                assert 1 != 1
            else:
                for datas in res.get("result"):
                    for _,v in datas.items():
                           assert v is not None   #如果值是数字，刚判断是否为null




    @allure.story("Oracle性能诊断数据库资源详情")
    @allure.title("oracle-dbtime-详情")
    @allure.description("oracle-dbtime-详情  ID：4339")
    @pytest.mark.smoking
    @pytest.mark.osm
    @pytest.mark.XIONGTING
    @pytest.mark.xfail
    @pytest.mark.parametrize("testdata",[opdata])
    def test_oracle_performance_dbtimedetails_get(self, testdata):
        with allure.step("获取response"):
            res = osmapi.oracle_performance_dbtimedetails_get(testdata)
        with allure.step("断言返回的内容都有值"):
            if len(res.get("result")) == 0:
                log.info("返回的result为空")
                assert 1 != 1
            else:
                for datas in res.get("result"):
                    for _,v in datas.items():
                           assert v is not None   #如果值是数字，刚判断是否为null



#################################Mysql 监控  #########################################
    @allure.story("Mysql性能诊断")
    @allure.title("每秒查询数")
    @allure.description("每秒查询数,ID:1131")
    @pytest.mark.smoking
    @pytest.mark.osm
    @pytest.mark.XIONGTING
    @pytest.mark.parametrize("testdata",[mysql_7_data])
    def test_mssql_per_picture_performance_qps_get(self, testdata):
        with allure.step("更新query_filed内容"):
            testdata["query_filed"] = "performance_qps"
        with allure.step("断言返回值"):
            res = osmapi.mysql_performance_picture_get(testdata)
            if len(res.get("result")) == 0:
                assert 1 != 1
            else:
                for datas in res.get("result"):
                    for data in datas.get("data"):
                        values = data.get("y")
                        for value in values:
                            assert value is not None



    @allure.story("Mysql性能诊断")
    @allure.title("数据库连接数")
    @allure.description("数据库连接数,ID:1131")
    @pytest.mark.smoking
    @pytest.mark.osm
    @pytest.mark.XIONGTING
    @pytest.mark.parametrize("testdata",[mysql_7_data])
    def test_mssql_per_picture_thread_connection_get(self, testdata):
        with allure.step("更新query_filed内容"):
            testdata["query_filed"] = "thread_connection"
        with allure.step("断言返回值"):
            res = osmapi.mysql_performance_picture_get(testdata)
            if len(res.get("result")) == 0:
                assert 1 != 1
            else:
                for datas in res.get("result"):
                    for data in datas.get("data"):
                        values = data.get("y")
                        for value in values:
                            assert value is not None



    @allure.story("Mysql性能诊断")
    @allure.title("数据库连接使用率")
    @allure.description("数据库连接使用率,ID:1131")
    @pytest.mark.smoking
    @pytest.mark.osm
    @pytest.mark.XIONGTING
    @pytest.mark.parametrize("testdata",[mysql_7_data])
    def test_mssql_per_picture_mysql_connection_use_rate_get(self, testdata):
        with allure.step("更新query_filed内容"):
            testdata["query_filed"] = "mysql_connection_use_rate"
        with allure.step("断言返回值"):
            res = osmapi.mysql_performance_picture_get(testdata)
            if len(res.get("result")) == 0:
                assert 1 != 1
            else:
                for datas in res.get("result"):
                    for data in datas.get("data"):
                        values = data.get("y")
                        for value in values:
                            assert value is not None



    @allure.story("Mysql性能诊断")
    @allure.title("每秒活动线程数")
    @allure.description("每秒活动线程数,ID:1131")
    @pytest.mark.smoking
    @pytest.mark.osm
    @pytest.mark.XIONGTING
    @pytest.mark.parametrize("testdata",[mysql_7_data])
    def test_mssql_per_picture_thread_info_get(self, testdata):
        with allure.step("更新query_filed内容"):
            testdata["query_filed"] = "thread_info"
        with allure.step("断言返回值"):
            res = osmapi.mysql_performance_picture_get(testdata)
            if len(res.get("result")) == 0:
                assert 1 != 1
            else:
                for datas in res.get("result"):
                    for data in datas.get("data"):
                        values = data.get("y")
                        for value in values:
                            assert value is not None



    @allure.story("Mysql性能诊断")
    @allure.title("数据库锁持续时间")
    @allure.description("数据库锁持续时间,ID:1131")
    @pytest.mark.smoking
    @pytest.mark.osm
    @pytest.mark.XIONGTING
    @pytest.mark.parametrize("testdata",[mysql_7_data])
    def test_mssql_per_picture_lock_time_get(self, testdata):
        with allure.step("更新query_filed内容"):
            testdata["query_filed"] = "lock_time"
        with allure.step("断言返回值"):
            res = osmapi.mysql_performance_picture_get(testdata)
            if len(res.get("result")) == 0:
                assert 1 != 1
            else:
                for datas in res.get("result"):
                    for data in datas.get("data"):
                        values = data.get("y")
                        for value in values:
                            assert value is not None



    @allure.story("Mysql性能诊断")
    @allure.title("慢日志条数")
    @allure.description("慢日志条数,ID:1131")
    @pytest.mark.smoking
    @pytest.mark.osm
    @pytest.mark.XIONGTING
    @pytest.mark.parametrize("testdata",[mysql_7_data])
    def test_mssql_per_picture_tps_get(self, testdata):
        with allure.step("更新query_filed内容"):
            testdata["query_filed"] = "tps"
        with allure.step("断言返回值"):
            res = osmapi.mysql_performance_picture_get(testdata)
            if len(res.get("result")) == 0:
                assert 1 != 1
            else:
                for datas in res.get("result"):
                    for data in datas.get("data"):
                        values = data.get("y")
                        for value in values:
                            assert value is not None


    @allure.story("Mysql性能诊断")
    @allure.title("TPS")
    @allure.description("TPS,ID:1131")
    @pytest.mark.smoking
    @pytest.mark.osm
    @pytest.mark.XIONGTING
    @pytest.mark.parametrize("testdata",[mysql_7_data])
    def test_mssql_per_picture_slow_log_get(self, testdata):
        with allure.step("更新query_filed内容"):
            testdata["query_filed"] = "slow_log"
        with allure.step("断言返回值"):
            res = osmapi.mysql_performance_picture_get(testdata)
            if len(res.get("result")) == 0:
                assert 1 != 1
            else:
                for datas in res.get("result"):
                    for data in datas.get("data"):
                        values = data.get("y")
                        for value in values:
                            assert value is not None


##########################Mysql 二级详情 ##################################
    @allure.story("mysql性能诊断")
    @allure.title("msyql-每秒查询数-详情")
    @allure.description("msyql-每秒查询数-详情,ID:2693")
    @pytest.mark.smoking
    @pytest.mark.osm
    @pytest.mark.XIONGTING
    @pytest.mark.parametrize("testdata",[mysql_7_data])
    def test_mysql_performance_qps_detail_get(self, testdata):
        with allure.step("更新query_filed内容"):
            testdata["query_filed"] = "performance_qps"
        with allure.step("获取response"):
            res = osmapi.mysql_performance_qps_detail_get(testdata)
        with allure.step("断言返回的内容都有值"):
            if len(res.get("result")) == 0:
                log.info("返回的result为空")
                assert 1 != 1
            else:
                for datas in res.get("result"):
                    for _,v in datas.items():
                        assert v is not None



    @allure.story("mysql性能诊断")
    @allure.title("msyql-数据库连接数-详情")
    @allure.description("msyql-数据库连接数-详情 ID:2711")
    @pytest.mark.smoking
    @pytest.mark.osm
    @pytest.mark.XIONGTING
    @pytest.mark.parametrize("testdata",[mysql_7_data])
    def test_mysql_performance_connection_detail_get(self, testdata):
        with allure.step("更新query_filed内容"):
            testdata["query_filed"] = "thread_connection"
        with allure.step("获取response"):
            res = osmapi.mysql_performance_connection_detail_get(testdata)
        with allure.step("断言返回的内容都有值"):
            if len(res.get("result")) == 0:
                log.info("返回的result为空")
                assert 1 != 1
            else:
                for datas in res.get("result"):
                    for _,v in datas.items():
                        assert v is not None



    @allure.story("mysql性能诊断")
    @allure.title("mysql数据库连接使用率_下钻")
    @allure.description("mysql数据库连接使用率_下钻 ID:5545")
    @pytest.mark.smoking
    @pytest.mark.osm
    @pytest.mark.XIONGTING
    @pytest.mark.parametrize("testdata",[mysql_7_data])
    def test_mysql_performance_connection_use_rate_detail_get(self, testdata):
        with allure.step("更新query_filed内容"):
            testdata["query_filed"] = "mysql_connection_use_rate"
        with allure.step("获取response"):
            res = osmapi.mysql_performance_connection_use_rate_detail_get(testdata)
        with allure.step("断言返回的内容都有值"):
            if len(res.get("result")) == 0:
                log.info("返回的result为空")
                assert 1 != 1
            else:
                for datas in res.get("result"):
                    for _,v in datas.items():
                        assert v is not None



    @allure.story("mysql性能诊断")
    @allure.title("mysql-每秒活动线程数-详情_下钻")
    @allure.description("mysql-每秒活动线程数-详情 ID:2705")
    @pytest.mark.smoking
    @pytest.mark.osm
    @pytest.mark.XIONGTING
    @pytest.mark.parametrize("testdata",[mysql_7_data])
    def test_mysql_performance_thread_detail_get(self, testdata):
        with allure.step("更新query_filed内容"):
            testdata["query_filed"] = "thread_info"
        with allure.step("获取response"):
            res = osmapi.mysql_performance_thread_detail_get(testdata)
        with allure.step("断言返回的内容都有值"):
            if len(res.get("result")) == 0:
                log.info("返回的result为空")
                assert 1 != 1
            else:
                for datas in res.get("result"):
                    for _,v in datas.items():
                        assert v is not None



    @allure.story("mysql性能诊断")
    @allure.title("mysql-数据库锁持续时间-详情")
    @allure.description("mysql-数据库锁持续时间-详情 ID:2709")
    @pytest.mark.smoking
    @pytest.mark.osm
    @pytest.mark.XIONGTING
    @pytest.mark.parametrize("testdata",[mysql_7_data])
    def test_mysql_performance_lock_time_detail_get(self, testdata):
        with allure.step("更新query_filed内容"):
            testdata["query_filed"] = "lock_time"
        with allure.step("获取response"):
            res = osmapi.mysql_performance_lock_time_detail_get(testdata)
        with allure.step("断言返回的内容都有值"):
            if len(res.get("result")) == 0:
                log.info("返回的result为空")
                assert 1 != 1
            else:
                for datas in res.get("result"):
                    for _,v in datas.items():
                        assert v is not None




