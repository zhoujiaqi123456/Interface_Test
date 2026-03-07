# -*- coding:utf-8 -*-
'''
@Time       : 2022/6/17 15:32
@Author     : xiongting
@FileName   : osm_monitor_mode.py
@Description:
'''

from mode.request_mode_osm import  BusinessSystemMode,AssertManagerMode
from public.logger import log
import sys
from datetime import datetime, timedelta



nowtime = datetime.now()


#单实例大屏
class MonitorMode(BusinessSystemMode):
    """
       监控模块脚本
    """
    ########################## 监控公共接口 ########################
    def get_host_base_info(self,args,**kwargs):
        """MSSQL单实例大屏基础信息获取,ID:1183
        """
        params = {
            "db_id": kwargs.get('db_id'),  #资产ID
            "item" : args.get('item'),   #信息类型：io,net,memory,cpu
            "os_type": args.get('os_type'),  # 信息类型：主机类型从，用例内传入,默认值为Linux主机
            "ip":args.get('ip')   #主机ip，从用例内传入
        }
        log.info(f"请求的最终{sys._getframe().f_code.co_name}:{params}")
        url = f"{self.osm_url}/api/monitor/v1/host"
        response = self.sget(url, params=params)
        assert response.status_code == 200, "请求返回码不正确"
        log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
        assert response.json().get("code") == 100000
        assert response.json().get("message") == '成功'
        return response.json()


    ########################## MSSQL单实例监控大屏 ########################
    def get_mssql_base_info(self,**kwargs):
        """MSSQL单实例大屏基础信息获取,ID:1183
        """
        params = {
            "db_id": kwargs.get('db_id')
        }
        log.info(f"请求的最终{sys._getframe().f_code.co_name}:{params}")
        url = f"{self.osm_url}/api/monitor/v1/mssql/basic_info"
        response = self.sget(url, params=params)
        assert response.status_code == 200, "请求返回码不正确"
        log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
        assert response.json().get("code") == 100000
        assert response.json().get("message") == '成功'
        return response.json()

    def get_mssql_lock_info(self,**kwargs):
        """MSSQL数据库锁信息,ID:1211
        """
        params = {
            "db_id": kwargs.get('db_id')
        }
        log.info(f"请求的最终{sys._getframe().f_code.co_name}:{params}")
        url = f"{self.osm_url}/api/monitor/v1/mssql/lock_info"
        response = self.sget(url, params=params)
        assert response.status_code == 200, "请求返回码不正确"
        log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
        assert response.json().get("code") == 100000
        assert response.json().get("message") == '成功'
        return response.json()

    def get_mssql_latch_info(self,**kwargs):
        """MSSQL数据库Latch,ID:1207
        """
        params = {
            "db_id": kwargs.get('db_id')
        }
        log.info(f"请求的最终{sys._getframe().f_code.co_name}:{params}")
        url = f"{self.osm_url}/api/monitor/v1/mssql/latch_info"
        response = self.sget(url, params=params)
        assert response.status_code == 200, "请求返回码不正确"
        log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
        assert response.json().get("code") == 100000
        assert response.json().get("message") == '成功'
        return response.json()

    def get_mssql_tempdb_info(self,**kwargs):
        """MSSQL数据库tempdb信息,ID:1199
        """
        params = {
            "db_id": kwargs.get('db_id')
        }
        log.info(f"请求的最终{sys._getframe().f_code.co_name}:{params}")
        url = f"{self.osm_url}/api/monitor/v1/mssql/tempdb_info"
        response = self.sget(url, params=params)
        assert response.status_code == 200, "请求返回码不正确"
        log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
        assert response.json().get("code") == 100000
        assert response.json().get("message") == '成功'
        return response.json()

    def get_mssql_sqlcommit_info(self,**kwargs):
        """MSSQL提交信息,ID:1227
        """
        params = {
            "db_id": kwargs.get('db_id')
        }
        log.info(f"请求的最终{sys._getframe().f_code.co_name}:{params}")
        url = f"{self.osm_url}/api/monitor/v1/mssql/sqlcommit_info"
        response = self.sget(url, params=params)
        assert response.status_code == 200, "请求返回码不正确"
        log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
        assert response.json().get("code") == 100000
        assert response.json().get("message") == '成功'
        return response.json()

    def get_mssql_sqlparse_info(self,**kwargs):
        """MSSQL数据库解析信息,ID:1235
        """
        params = {
            "db_id": kwargs.get('db_id')
        }
        log.info(f"请求的最终{sys._getframe().f_code.co_name}:{params}")
        url = f"{self.osm_url}/api/monitor/v1/mssql/sqlparse_info"
        response = self.sget(url, params=params)
        assert response.status_code == 200, "请求返回码不正确"
        log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
        assert response.json().get("code") == 100000
        assert response.json().get("message") == '成功'
        return response.json()

    def get_mssql_sqlexecute_info(self,**kwargs):
        """MSSQL数据库执行信息,ID:1231
        """
        params = {
            "db_id": kwargs.get('db_id')
        }
        log.info(f"请求的最终{sys._getframe().f_code.co_name}:{params}")
        url = f"{self.osm_url}/api/monitor/v1/mssql/sqlexecute_info"
        response = self.sget(url, params=params)
        assert response.status_code == 200, "请求返回码不正确"
        log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
        assert response.json().get("code") == 100000
        assert response.json().get("message") == '成功'
        return response.json()

    def get_mssql_net_info(self,**kwargs):
        """MSSQL数据库网络信息,ID:1223
        """
        params = {
            "db_id": kwargs.get('db_id')
        }
        log.info(f"请求的最终{sys._getframe().f_code.co_name}:{params}")
        url = f"{self.osm_url}/api/monitor/v1/mssql/net_info"
        response = self.sget(url, params=params)
        assert response.status_code == 200, "请求返回码不正确"
        log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
        assert response.json().get("code") == 100000
        assert response.json().get("message") == '成功'
        return response.json()

    def get_mssql_buffercache_info(self,**kwargs):
        """MSSQL buffercache 信息,ID:1303
        """
        params = {
            "db_id": kwargs.get('db_id')
        }
        log.info(f"请求的最终{sys._getframe().f_code.co_name}:{params}")
        url = f"{self.osm_url}/api/monitor/v1/mssql/buffercache_info"
        response = self.sget(url, params=params)
        assert response.status_code == 200, "请求返回码不正确"
        log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
        assert response.json().get("code") == 100000
        assert response.json().get("message") == '成功'
        return response.json()

    def get_mssql_session_info(self,**kwargs):
        """MSSQL数据库会话信息,ID:1195
        """
        params = {
            "db_id": kwargs.get('db_id')
        }
        log.info(f"请求的最终{sys._getframe().f_code.co_name}:{params}")
        url = f"{self.osm_url}/api/monitor/v1/mssql/session_info"
        response = self.sget(url, params=params)
        assert response.status_code == 200, "请求返回码不正确"
        log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
        assert response.json().get("code") == 100000
        assert response.json().get("message") == '成功'
        return response.json()

    def get_mssql_latchwait_info(self,**kwargs):
        """MSSQL-latchwait信息,ID:1291
        """
        params = {
            "db_id": kwargs.get('db_id')
        }
        log.info(f"请求的最终{sys._getframe().f_code.co_name}:{params}")
        url = f"{self.osm_url}/api/monitor/v1/mssql/latchwait_info"
        response = self.sget(url, params=params)
        assert response.status_code == 200, "请求返回码不正确"
        log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
        assert response.json().get("code") == 100000
        assert response.json().get("message") == '成功'
        return response.json()

    def get_mssql_plancache_info(self,**kwargs):
        """MSSQL-plancache信息,ID:1295
        """
        params = {
            "db_id": kwargs.get('db_id')
        }
        log.info(f"请求的最终{sys._getframe().f_code.co_name}:{params}")
        url = f"{self.osm_url}/api/monitor/v1/mssql/plancache_info"
        response = self.sget(url, params=params)
        assert response.status_code == 200, "请求返回码不正确"
        log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
        assert response.json().get("code") == 100000
        assert response.json().get("message") == '成功'
        return response.json()

    def get_mssql_logicalread_info(self,**kwargs):
        """MSSQL logicalread信息,ID:1299
        """
        params = {
            "db_id": kwargs.get('db_id')
        }
        log.info(f"请求的最终{sys._getframe().f_code.co_name}:{params}")
        url = f"{self.osm_url}/api/monitor/v1/mssql/logicalread_info"
        response = self.sget(url, params=params)
        assert response.status_code == 200, "请求返回码不正确"
        log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
        assert response.json().get("code") == 100000
        assert response.json().get("message") == '成功'
        return response.json()

    def get_mssql_logbuffer_info(self,**kwargs):
        """MSSQL logbuffer info信息,ID:1311
        """
        params = {
            "db_id": kwargs.get('db_id')
        }
        log.info(f"请求的最终{sys._getframe().f_code.co_name}:{params}")
        url = f"{self.osm_url}/api/monitor/v1/mssql/logbuffer_info"
        response = self.sget(url, params=params)
        assert response.status_code == 200, "请求返回码不正确"
        log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
        assert response.json().get("code") == 100000
        assert response.json().get("message") == '成功'
        return response.json()

    def get_mssql_logical_read(self,**kwargs):
        """逻辑读次数趋势图,ID:2231
        """
        params = {
            "db_id": kwargs.get('db_id')
        }
        log.info(f"请求的最终{sys._getframe().f_code.co_name}:{params}")
        url = f"{self.osm_url}/api/monitor/v1/mssql/logical_read"
        response = self.sget(url, params=params)
        assert response.status_code == 200, "请求返回码不正确"
        log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
        assert response.json().get("code") == 100000
        assert response.json().get("message") == '成功'
        return response.json()

    def get_mssql_logicalreadsrtt(self,**kwargs):
        """逻辑读时间趋势图,ID:2227
        """
        params = {
            "db_id": kwargs.get('db_id')
        }
        log.info(f"请求的最终{sys._getframe().f_code.co_name}:{params}")
        url = f"{self.osm_url}/api/monitor/v1/mssql/logicalreadsrtt"
        response = self.sget(url, params=params)
        assert response.status_code == 200, "请求返回码不正确"
        log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
        assert response.json().get("code") == 100000
        assert response.json().get("message") == '成功'
        return response.json()

    def get_mssql_login_info(self,**kwargs):
        """MSSQL数据库登录信息,ID:1191
        """
        params = {
            "db_id": kwargs.get('db_id')
        }
        log.info(f"请求的最终{sys._getframe().f_code.co_name}:{params}")
        url = f"{self.osm_url}/api/monitor/v1/mssql/login_info"
        response = self.sget(url, params=params)
        assert response.status_code == 200, "请求返回码不正确"
        log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
        assert response.json().get("code") == 100000
        assert response.json().get("message") == '成功'
        return response.json()


    ########################## Oracle单实例监控大屏 ########################
    def get_oracle_base_info(self,**kwargs):
        """oracle单实例大屏基础信息,ID:1239
        """
        params = {
            "db_id": kwargs.get('db_id')
        }
        log.info(f"请求的最终{sys._getframe().f_code.co_name}:{params}")
        url = f"{self.osm_url}/api/monitor/v1/oracle/basic_info"
        response = self.sget(url, params=params)
        assert response.status_code == 200, "请求返回码不正确"
        log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
        assert response.json().get("code") == 100000
        assert response.json().get("message") == '成功'
        return response.json()

    def get_oracle_login_info(self,**kwargs):
        """orcale登录图表信息,ID:1243
        """
        params = {
            "db_id": kwargs.get('db_id')
        }
        log.info(f"请求的最终{sys._getframe().f_code.co_name}:{params}")
        url = f"{self.osm_url}/api/monitor/v1/oracle/login_info"
        response = self.sget(url, params=params)
        assert response.status_code == 200, "请求返回码不正确"
        log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
        assert response.json().get("code") == 100000
        assert response.json().get("message") == '成功'
        return response.json()

    def get_oracle_session_info(self, **kwargs):
        """oracle数据库会话信息,ID:1247
        """
        params = {
            "db_id": kwargs.get('db_id')
        }
        log.info(f"请求的最终{sys._getframe().f_code.co_name}:{params}")
        url = f"{self.osm_url}/api/monitor/v1/oracle/session_info"
        response = self.sget(url, params=params)
        assert response.status_code == 200, "请求返回码不正确"
        log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
        assert response.json().get("code") == 100000
        assert response.json().get("message") == '成功'
        return response.json()

    def get_oracle_resource_info(self, **kwargs):
        """oracle资源使用率,ID:1251
        """
        params = {
            "db_id": kwargs.get('db_id')
        }
        log.info(f"请求的最终{sys._getframe().f_code.co_name}:{params}")
        url = f"{self.osm_url}/api/monitor/v1/oracle/resource"
        response = self.sget(url, params=params)
        assert response.status_code == 200, "请求返回码不正确"
        log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
        assert response.json().get("code") == 100000
        assert response.json().get("message") == '成功'
        return response.json()

    def get_oracle_mutex_info(self, **kwargs):
        """oracleMutex互斥锁,ID:1255
        """
        params = {
            "db_id": kwargs.get('db_id')
        }
        log.info(f"请求的最终{sys._getframe().f_code.co_name}:{params}")
        url = f"{self.osm_url}/api/monitor/v1/oracle/mutex"
        response = self.sget(url, params=params)
        assert response.status_code == 200, "请求返回码不正确"
        log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
        assert response.json().get("code") == 100000
        assert response.json().get("message") == '成功'
        return response.json()

    def get_oracle_latch_info(self, **kwargs):
        """oracle latch锁,ID:1259
        """
        params = {
            "db_id": kwargs.get('db_id')
        }
        log.info(f"请求的最终{sys._getframe().f_code.co_name}:{params}")
        url = f"{self.osm_url}/api/monitor/v1/oracle/latch"
        response = self.sget(url, params=params)
        assert response.status_code == 200, "请求返回码不正确"
        log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
        assert response.json().get("code") == 100000
        assert response.json().get("message") == '成功'
        return response.json()

    def get_oracle_lock_info(self,**kwargs):
        """oracle数据库锁信息,ID:1263
        """
        params = {
            "db_id": kwargs.get('db_id')
        }
        log.info(f"请求的最终{sys._getframe().f_code.co_name}:{params}")
        url = f"{self.osm_url}/api/monitor/v1/oracle/lock"
        response = self.sget(url, params=params)
        assert response.status_code == 200, "请求返回码不正确"
        log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
        assert response.json().get("code") == 100000
        assert response.json().get("message") == '成功'
        return response.json()

    def get_oracle_sqlparse_basic_info(self,**kwargs):
        """oracle SQL解析基础信息,ID:1267
        """
        params = {
            "db_id": kwargs.get('db_id')
        }
        log.info(f"请求的最终{sys._getframe().f_code.co_name}:{params}")
        url = f"{self.osm_url}/api/monitor/v1/oracle/parse/basic"
        response = self.sget(url, params=params)
        assert response.status_code == 200, "请求返回码不正确"
        log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
        assert response.json().get("code") == 100000
        assert response.json().get("message") == '成功'
        return response.json()

    def get_oracle_sqlparse_pic_info(self,**kwargs):
        """oracle SQL解析图片,ID:1279
        """
        params = {
            "db_id": kwargs.get('db_id')
        }
        log.info(f"请求的最终{sys._getframe().f_code.co_name}:{params}")
        url = f"{self.osm_url}/api/monitor/v1/oracle/parse/pic"
        response = self.sget(url, params=params)
        assert response.status_code == 200, "请求返回码不正确"
        log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
        assert response.json().get("code") == 100000
        assert response.json().get("message") == '成功'
        return response.json()


    def get_oracle_execute_basic_info(self,**kwargs):
        """oracle SQL执行基础信息,ID:1271
        """
        params = {
            "db_id": kwargs.get('db_id')
        }
        log.info(f"请求的最终{sys._getframe().f_code.co_name}:{params}")
        url = f"{self.osm_url}/api/monitor/v1/oracle/execute/basic"
        response = self.sget(url, params=params)
        assert response.status_code == 200, "请求返回码不正确"
        log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
        assert response.json().get("code") == 100000
        assert response.json().get("message") == '成功'
        return response.json()


    def get_oracle_execute_pic_info(self,**kwargs):
        """oracle SQL执行图片,ID:1283
        """
        params = {
            "db_id": kwargs.get('db_id')
        }
        log.info(f"请求的最终{sys._getframe().f_code.co_name}:{params}")
        url = f"{self.osm_url}/api/monitor/v1/oracle/execute/pic"
        response = self.sget(url, params=params)
        assert response.status_code == 200, "请求返回码不正确"
        log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
        assert response.json().get("code") == 100000
        assert response.json().get("message") == '成功'
        return response.json()

    def get_oracle_commit_basic_info(self,**kwargs):
        """oracle SQL提交基础信息,ID:1275
        """
        params = {
            "db_id": kwargs.get('db_id')
        }
        log.info(f"请求的最终{sys._getframe().f_code.co_name}:{params}")
        url = f"{self.osm_url}/api/monitor/v1/oracle/commit/basic"
        response = self.sget(url, params=params)
        assert response.status_code == 200, "请求返回码不正确"
        log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
        assert response.json().get("code") == 100000
        assert response.json().get("message") == '成功'
        return response.json()

    def get_oracle_commit_pic_info(self,**kwargs):
        """oracle SQL提交图片,ID:1287
        """
        params = {
            "db_id": kwargs.get('db_id')
        }
        log.info(f"请求的最终{sys._getframe().f_code.co_name}:{params}")
        url = f"{self.osm_url}/api/monitor/v1/oracle/commit/pic"
        response = self.sget(url, params=params)
        assert response.status_code == 200, "请求返回码不正确"
        log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
        assert response.json().get("code") == 100000
        assert response.json().get("message") == '成功'
        return response.json()

    def get_oracle_logicalreadsrtt(self,**kwargs):
        """oracle逻辑读时间趋势图,ID:2203
        """
        params = {
            "db_id": kwargs.get('db_id')
        }
        log.info(f"请求的最终{sys._getframe().f_code.co_name}:{params}")
        url = f"{self.osm_url}/api/monitor/v1/oracle/logicalreadsrtt"
        response = self.sget(url, params=params)
        assert response.status_code == 200, "请求返回码不正确"
        log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
        assert response.json().get("code") == 100000
        assert response.json().get("message") == '成功'
        return response.json()

    def get_oracle_logical_read(self,**kwargs):
        """逻辑读次数趋势图,ID:2207
        """
        params = {
            "db_id": kwargs.get('db_id')
        }
        log.info(f"请求的最终{sys._getframe().f_code.co_name}:{params}")
        url = f"{self.osm_url}/api/monitor/v1/oracle/logical_read"
        response = self.sget(url, params=params)
        assert response.status_code == 200, "请求返回码不正确"
        log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
        assert response.json().get("code") == 100000
        assert response.json().get("message") == '成功'
        return response.json()



##########################Mysql 单实例大屏监控############################
    def get_mysql_base_info(self,**kwargs):
        """MySQL数据库监控基础数据接口,ID:1131
        """
        params = {
            "db_id": kwargs.get('db_id')
        }
        log.info(f"请求的最终{sys._getframe().f_code.co_name}:{params}")
        url = f"{self.osm_url}/api/monitor/v1/mysqldb/basic_info"
        response = self.sget(url, params=params)
        assert response.status_code == 200, "请求返回码不正确"
        log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
        assert response.json().get("code") == 100000
        assert response.json().get("message") == '成功'
        return response.json()







#性能诊断--数据库资源
class PerformanceModeDB(AssertManagerMode):
    """性能诊断"""

    ############################ MSSQL性能诊断 ####################################
    def get_mssql_performance_picture(self,args,**kwargs):
        """
        mssql性能诊断图表,ID:3083
        :param args:
            {
             "db_id":数据库资产ID
             "query_filed":
                        logins 每秒登录数
                        activesessions 活动会话数
                        hardparse    硬解析次数
                        txlocks   tx锁数量
                        activetmptables   每秒活动临时表数
            }
        :return:
        """
        url = f"{self.osm_url}/api/monitor/v1/mssql/picture"
        params = {
            "db_id": kwargs.get("db_id"),
            "query_filed": args.get("query_filed"),
            "start_time": (nowtime + timedelta(days=-24)).strftime("%Y-%m-%d %H:%M:%S"), #默认读取24小内的数据
            "end_time": nowtime.strftime("%Y-%m-%d %H:%M:%S")
        }
        log.info(f"请求的最终{sys._getframe().f_code.co_name}:{params}")
        response = self.sget(url, params=params)
        assert response.status_code == 200, "请求返回码不正确"
        # log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
        assert response.json().get("code") == 100000
        assert response.json().get("message") == '成功'
        return response.json()



    def get_mssql_performance_logins_detail(self,**kwargs):
        """
        mssql-硬解析次数-详情，从图标内点击进去ID:4843
        :param args:
        :param kwargs: 从api层传入db_id
        :return:
        """
        url = f"{self.osm_url}/api/monitor/v1/mssql/logins_detail"
        params = {
            "db_id": kwargs.get("db_id"),
            "time":  kwargs.get("time"),
        }
        log.info(f"请求的最终参数{sys._getframe().f_code.co_name}:{params}")
        response = self.sget(url, params=params)
        assert response.status_code == 200, "请求返回码不正确"
        log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
        assert response.json().get("code") == 100000
        assert response.json().get("message") == '成功'
        return response.json()


    def get_mssql_performance_txlocks_detail(self,**kwargs):
        """
         mssql-tx锁-详情   ID:4849
        :param args:
        :param kwargs: 从api层传入db_id
        :return:
        """
        url = f"{self.osm_url}/api/monitor/v1/mssql/txlocks_detail"
        params = {
            "db_id": kwargs.get("db_id"),
            "time":  kwargs.get("time"),
        }
        log.info(f"请求的最终参数{sys._getframe().f_code.co_name}:{params}")
        response = self.sget(url, params=params)
        assert response.status_code == 200, "请求返回码不正确"
        log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
        assert response.json().get("code") == 100000
        assert response.json().get("message") == '成功'
        return response.json()


    def get_mssql_performance_activetmptable_detail(self,**kwargs):
        """
          mssql-临时表-详情   ID:4855
        :param args:
        :param kwargs: 从api层传入db_id
        :return:
        """
        url = f"{self.osm_url}/api/monitor/v1/mssql/activetmptable_detail"
        params = {
            "db_id": kwargs.get("db_id"),
            "time":  kwargs.get("time"),
        }
        log.info(f"请求的最终参数{sys._getframe().f_code.co_name}:{params}")
        response = self.sget(url, params=params)
        assert response.status_code == 200, "请求返回码不正确"
        log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
        assert response.json().get("code") == 100000
        assert response.json().get("message") == '成功'
        return response.json()


    def get_mssql_performance_hardparse_detail(self,**kwargs):
        """
          mssql-硬解析次数-详情   ID:3085
        :param args:
        :param kwargs: 从api层传入db_id
        :return:
        """
        url = f"{self.osm_url}/api/monitor/v1/mssql/hardparse_detail"
        params = {
            "db_id": kwargs.get("db_id"),
            "time":  kwargs.get("time"),
        }
        log.info(f"请求的最终参数{sys._getframe().f_code.co_name}:{params}")
        response = self.sget(url, params=params)
        assert response.status_code == 200, "请求返回码不正确"
        log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
        assert response.json().get("code") == 100000
        assert response.json().get("message") == '成功'
        return response.json()



    def get_mssql_performance_hactivesessions_detail(self,**kwargs):
        """
          mssql-活动会话数-详情   ID:3087
        :param args:
        :param kwargs: 从api层传入db_id
        :return:
        """
        url = f"{self.osm_url}/api/monitor/v1/mssql/activesessions_detail"
        params = {
            "db_id": kwargs.get("db_id"),
            "time":  kwargs.get("time"),
        }
        log.info(f"请求的最终参数{sys._getframe().f_code.co_name}:{params}")
        response = self.sget(url, params=params)
        assert response.status_code == 200, "请求返回码不正确"
        log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
        assert response.json().get("code") == 100000
        assert response.json().get("message") == '成功'
        return response.json()


    ############################ ORACLE 性能诊断 ####################################
    def get_oracle_performance_diagnosis(self,args,**kwargs):
        """
        oracle性能诊断接口，包括页面的每秒新增连接数、活动会话数、数据库连接使用率,ID:2759
        :param args:
            {
             "db_id":数据库资产ID
             "query_filed":
                   new_conn_per_sec   每秒新增连接数
                   conn_used_pct      数据库连接使用率
                   active_session     活动会话数
            }
        :return:
        """
        url = f"{self.osm_url}/api/monitor/v1/oracle/diagnosis"
        params = {
            "db_id": kwargs.get("db_id"),
            "query_filed": args.get("query_filed"),
            "start_time": (nowtime + timedelta(days=-24)).strftime("%Y-%m-%d %H:%M:%S"), #默认读取24小内的数据
            "end_time": nowtime.strftime("%Y-%m-%d %H:%M:%S")
        }
        log.info(f"请求的最终{sys._getframe().f_code.co_name}:{params}")
        response = self.sget(url, params=params)
        assert response.status_code == 200, "请求返回码不正确"
        #log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
        assert response.json().get("code") == 100000
        assert response.json().get("message") == '成功'
        return response.json()



    def get_oracle_performance_hardparsetimepct(self,**kwargs):
        """
        硬解析延迟占比 ID:2661
        :param args:
            {
             "db_id":数据库资产ID
            }
        :return:
        """
        url = f"{self.osm_url}/api/monitor/v1/oracle/hardparsetimepct"
        params = {
            "db_id": kwargs.get("db_id"),
            "start_time": (nowtime + timedelta(days=-24)).strftime("%Y-%m-%d %H:%M:%S"), #默认读取24小内的数据
            "end_time": nowtime.strftime("%Y-%m-%d %H:%M:%S")
        }
        log.info(f"请求的最终{sys._getframe().f_code.co_name}:{params}")
        response = self.sget(url, params=params)
        assert response.status_code == 200, "请求返回码不正确"
        log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
        assert response.json().get("code") == 100000
        assert response.json().get("message") == '成功'
        return response.json()


    def get_oracle_performance_resource_conflict_concurrency(self,**kwargs):
        """
        资源冲突-并发延迟占比 ID:2655
        :param args:
            {
             "db_id":数据库资产ID
            }
        :return:
        """
        url = f"{self.osm_url}/api/monitor/v1/oracle/resource_conflict/concurrency"
        params = {
            "db_id": kwargs.get("db_id"),
            "start_time": (nowtime + timedelta(days=-24)).strftime("%Y-%m-%d %H:%M:%S"), #默认读取24小内的数据
            "end_time": nowtime.strftime("%Y-%m-%d %H:%M:%S")
        }
        log.info(f"请求的最终{sys._getframe().f_code.co_name}:{params}")
        response = self.sget(url, params=params)
        assert response.status_code == 200, "请求返回码不正确"
        log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
        assert response.json().get("code") == 100000
        assert response.json().get("message") == '成功'
        return response.json()



    def get_oracle_performance_hardparsecountops(self,**kwargs):
        """
         每秒硬解析次数 ID:2667
        :param args:
            {
             "db_id":数据库资产ID
            }
        :return:
        """
        url = f"{self.osm_url}/api/monitor/v1/oracle/hardparsecountops"
        params = {
            "db_id": kwargs.get("db_id"),
            "start_time": (nowtime + timedelta(days=-24)).strftime("%Y-%m-%d %H:%M:%S"), #默认读取24小内的数据
            "end_time": nowtime.strftime("%Y-%m-%d %H:%M:%S")
        }
        log.info(f"请求的最终{sys._getframe().f_code.co_name}:{params}")
        response = self.sget(url, params=params)
        assert response.status_code == 200, "请求返回码不正确"
        log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
        assert response.json().get("code") == 100000
        assert response.json().get("message") == '成功'
        return response.json()


    def get_oracle_performance_dbtime_info(self,**kwargs):
        """
        DBtime ID:2699
        :param args:
            {
             "db_id":数据库资产ID
            }
        :return:
        """
        url = f"{self.osm_url}/api/monitor/v1/oracle/dbtime_info"
        params = {
            "db_id": kwargs.get("db_id"),
            "start_time": (nowtime + timedelta(days=-24)).strftime("%Y-%m-%d %H:%M:%S"), #默认读取24小内的数据
            "end_time": nowtime.strftime("%Y-%m-%d %H:%M:%S")
        }
        log.info(f"请求的最终{sys._getframe().f_code.co_name}:{params}")
        response = self.sget(url, params=params)
        assert response.status_code == 200, "请求返回码不正确"
        log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
        assert response.json().get("code") == 100000
        assert response.json().get("message") == '成功'
        return response.json()


    def get_oracle_performance_conntimepct(self,**kwargs):
        """
        登录延迟占比 ID:2665
        :param args:
            {
             "db_id":数据库资产ID
            }
        :return:
        """
        url = f"{self.osm_url}/api/monitor/v1/oracle/conntimepct"
        params = {
            "db_id": kwargs.get("db_id"),
            "start_time": (nowtime + timedelta(days=-24)).strftime("%Y-%m-%d %H:%M:%S"), #默认读取24小内的数据
            "end_time": nowtime.strftime("%Y-%m-%d %H:%M:%S")
        }
        log.info(f"请求的最终{sys._getframe().f_code.co_name}:{params}")
        response = self.sget(url, params=params)
        assert response.status_code == 200, "请求返回码不正确"
        log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
        assert response.json().get("code") == 100000
        assert response.json().get("message") == '成功'
        return response.json()


    def get_oracle_performance_seqloadtimepct(self,**kwargs):
        """
        序列获取时间占比 ID:2663
        :param args:
            {
             "db_id":数据库资产ID
            }
        :return:
        """
        url = f"{self.osm_url}/api/monitor/v1/oracle/seqloadtimepct"
        params = {
            "db_id": kwargs.get("db_id"),
            "start_time": (nowtime + timedelta(days=-24)).strftime("%Y-%m-%d %H:%M:%S"), #默认读取24小内的数据
            "end_time": nowtime.strftime("%Y-%m-%d %H:%M:%S")
        }
        log.info(f"请求的最终{sys._getframe().f_code.co_name}:{params}")
        response = self.sget(url, params=params)
        assert response.status_code == 200, "请求返回码不正确"
        log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
        assert response.json().get("code") == 100000
        assert response.json().get("message") == '成功'
        return response.json()


    def get_oracle_performance_lock_info(self,**kwargs):
        """
        锁信息 ID:2631
        :param args:
            {
             "db_id":数据库资产ID
            }
        :return:
        """
        url = f"{self.osm_url}/api/monitor/v1/oracle/lock_info"
        params = {
            "db_id": kwargs.get("db_id"),
            "start_time": (nowtime + timedelta(days=-24)).strftime("%Y-%m-%d %H:%M:%S"), #默认读取24小内的数据
            "end_time": nowtime.strftime("%Y-%m-%d %H:%M:%S")
        }
        log.info(f"请求的最终{sys._getframe().f_code.co_name}:{params}")
        response = self.sget(url, params=params)
        assert response.status_code == 200, "请求返回码不正确"
        log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
        assert response.json().get("code") == 100000
        assert response.json().get("message") == '成功'
        return response.json()


    def get_oracle_performance_resource_conflict_application(self,**kwargs):
        """
        资源冲突-应用等待占比 ID:2629
        :param args:
            {
             "db_id":数据库资产ID
            }
        :return:
        """
        url = f"{self.osm_url}/api/monitor/v1/oracle/resource_conflict/application"
        params = {
            "db_id": kwargs.get("db_id"),
            "start_time": (nowtime + timedelta(days=-24)).strftime("%Y-%m-%d %H:%M:%S"), #默认读取24小内的数据
            "end_time": nowtime.strftime("%Y-%m-%d %H:%M:%S")
        }
        log.info(f"请求的最终{sys._getframe().f_code.co_name}:{params}")
        response = self.sget(url, params=params)
        assert response.status_code == 200, "请求返回码不正确"
        log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
        assert response.json().get("code") == 100000
        assert response.json().get("message") == '成功'
        return response.json()




    def get_oracle_performance_resource_conflict_configuration(self,**kwargs):
        """
        资源冲突-配置延迟占比 ID:2653
        :param args:
            {
             "db_id":数据库资产ID
            }
        :return:
        """
        url = f"{self.osm_url}/api/monitor/v1/oracle/resource_conflict/configuration"
        params = {
            "db_id": kwargs.get("db_id"),
            "start_time": (nowtime + timedelta(days=-24)).strftime("%Y-%m-%d %H:%M:%S"), #默认读取24小内的数据
            "end_time": nowtime.strftime("%Y-%m-%d %H:%M:%S")
        }
        log.info(f"请求的最终{sys._getframe().f_code.co_name}:{params}")
        response = self.sget(url, params=params)
        assert response.status_code == 200, "请求返回码不正确"
        log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
        assert response.json().get("code") == 100000
        assert response.json().get("message") == '成功'
        return response.json()



    ################### oracle性能诊断 二级详情 #################################
    def get_oracle_performance_login_info_session(self,**kwargs):
        """
        数据库登录详情每秒新增连接数详情 ID：2641
        :param kwargs:
            {
                "db_id": 数据资源ID
                "time": 从oracle性能诊断接口获取，ID:2759
            }
        :return:
        """
        url = f"{self.osm_url}/api/monitor/v1/oracle/login_info/sessions"
        params = {
            "db_id": kwargs.get("db_id"),
            "time":  kwargs.get("time"),
        }
        log.info(f"请求的最终参数{sys._getframe().f_code.co_name}:{params}")
        response = self.sget(url, params=params)
        assert response.status_code == 200, "请求返回码不正确"
        log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
        assert response.json().get("code") == 100000
        assert response.json().get("message") == '成功'
        return response.json()


    def get_oracle_performance_session_info(self,**kwargs):
        """
        数据库会话数详情 ID：2643
        :param kwargs:
            {
                "db_id": 数据资源ID
                "time": 从oracle性能诊断接口获取，ID:2759
            }
        :return:
        """
        url = f"{self.osm_url}/api/monitor/v1/oracle/session_info/sessions"
        params = {
            "db_id": kwargs.get("db_id"),
            "time":  kwargs.get("time"),
        }
        log.info(f"请求的最终参数{sys._getframe().f_code.co_name}:{params}")
        response = self.sget(url, params=params)
        assert response.status_code == 200, "请求返回码不正确"
        log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
        assert response.json().get("code") == 100000
        assert response.json().get("message") == '成功'
        return response.json()


    def get_oracle_performance_connuse_details(self,**kwargs):
        """
        oracle-数据库连接使用率-详情 ID：4345
        :param kwargs:
            {
                "db_id": 数据资源ID
                "time": 从oracle性能诊断接口获取，ID:2629
            }
        :return:
        """
        url = f"{self.osm_url}/api/monitor/v1/oracle/connuse_details"
        params = {
            "db_id": kwargs.get("db_id"),
            "time":  kwargs.get("time"),
        }
        log.info(f"请求的最终参数{sys._getframe().f_code.co_name}:{params}")
        response = self.sget(url, params=params)
        assert response.status_code == 200, "请求返回码不正确"
        log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
        assert response.json().get("code") == 100000
        assert response.json().get("message") == '成功'
        return response.json()




    def get_oracle_performance_application_events(self,**kwargs):
        """
        应用锁等待延迟占比-详情 ID：2633
        :param kwargs:
            {
                "db_id": 数据资源ID
                "time": 从资源冲突-应用等待占比获取，ID:2629
            }
        :return:
        """
        url = f"{self.osm_url}/api/monitor/v1/oracle/resource_conflict/application/events"
        params = {
            "db_id": kwargs.get("db_id"),
            "time":  kwargs.get("time"),
        }
        log.info(f"请求的最终参数{sys._getframe().f_code.co_name}:{params}")
        response = self.sget(url, params=params)
        assert response.status_code == 200, "请求返回码不正确"
        log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
        assert response.json().get("code") == 100000
        assert response.json().get("message") == '成功'
        return response.json()



    def get_oracle_performance_configuration_events(self,**kwargs):
        """
        配置延迟占比-详情 ID：2657
        :param kwargs:
            {
                "db_id": 数据资源ID
                "time": 从资源冲突-配置延迟占比获取，ID:2653
            }
        :return:
        """
        url = f"{self.osm_url}/api/monitor/v1/oracle/resource_conflict/configuration/events"
        params = {
            "db_id": kwargs.get("db_id"),
            "time":  kwargs.get("time"),
        }
        log.info(f"请求的最终参数{sys._getframe().f_code.co_name}:{params}")
        response = self.sget(url, params=params)
        assert response.status_code == 200, "请求返回码不正确"
        log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
        assert response.json().get("code") == 100000
        assert response.json().get("message") == '成功'
        return response.json()



    def get_oracle_performance_concurrency_events(self,**kwargs):
        """
        并发延迟占比-详情 ID：2659
        :param kwargs:
            {
                "db_id": 数据资源ID
                "time": 从资源冲突-并发延迟占比获取，ID:2655
            }
        :return:
        """
        url = f"{self.osm_url}/api/monitor/v1/oracle/resource_conflict/concurrency/events"
        params = {
            "db_id": kwargs.get("db_id"),
            "time":  kwargs.get("time"),
        }
        log.info(f"请求的最终参数{sys._getframe().f_code.co_name}:{params}")
        response = self.sget(url, params=params)
        assert response.status_code == 200, "请求返回码不正确"
        log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
        assert response.json().get("code") == 100000
        assert response.json().get("message") == '成功'
        return response.json()



    def get_oracle_performance_hardparse_sqls(self,**kwargs):
        """
        oracle每秒硬解析次数一级下钻 ID：5541
        :param kwargs:
            {
                "db_id": 数据资源ID
                "time": 从每秒硬解析次数获取，ID:2667
            }
        :return:
        """
        url = f"{self.osm_url}/api/monitor/v1/oracle/hardparse/sqls"
        params = {
            "db_id": kwargs.get("db_id"),
            "time":  kwargs.get("time"),
        }
        log.info(f"请求的最终参数{sys._getframe().f_code.co_name}:{params}")
        response = self.sget(url, params=params)
        assert response.status_code == 200, "请求返回码不正确"
        log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
        assert response.json().get("code") == 100000
        assert response.json().get("message") == '成功'
        return response.json()



    def get_oracle_performance_hardparse_sqls_level_two(self,**kwargs):
        """
        oracle每秒硬解析次数二级下钻 ID：5549
        :param kwargs:
            {
                "db_id": 数据资源ID
                "time": 从每秒硬解析次数获取，ID:2667
                "signature":oracle每秒硬解析次数一级获取 ID：5541
            }
        :return:
        """
        url = f"{self.osm_url}/api/monitor/v1/oracle/hardparse/sqls/level_two"
        params = {
            "db_id": kwargs.get("db_id"),
            "time":  kwargs.get("time"),
            "signature": kwargs.get("signature"),
            "page": 1,
            "per_page":100
        }
        log.info(f"请求的最终参数{sys._getframe().f_code.co_name}:{params}")
        response = self.sget(url, params=params)
        assert response.status_code == 200, "请求返回码不正确"
        log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
        assert response.json().get("code") == 100000
        assert response.json().get("message") == '成功'
        return response.json()


    def get_oracle_performance_lock_sessions(self,**kwargs):
        """
        锁信息详情 ID：2635
        :param kwargs:
            {
                "db_id": 数据资源ID
                "time": 从锁信息获取，ID:2631
            }
        :return:
        """
        url = f"{self.osm_url}/api/monitor/v1/oracle/lock_info/lock_sessions"
        params = {
            "db_id": kwargs.get("db_id"),
            "time":  kwargs.get("time"),
        }
        log.info(f"请求的最终参数{sys._getframe().f_code.co_name}:{params}")
        response = self.sget(url, params=params)
        assert response.status_code == 200, "请求返回码不正确"
        log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
        assert response.json().get("code") == 100000
        assert response.json().get("message") == '成功'
        return response.json()



    def get_oracle_performance_dbtimedetails(self,**kwargs):
        """
        oracle-dbtime-详情  ID：4339
        :param kwargs:
            {
                "db_id": 数据资源ID
                "time": 从锁信息获取，ID:2699
            }
        :return:
        """
        url = f"{self.osm_url}/api/monitor/v1/oracle/dbtimedetails"
        params = {
            "db_id": kwargs.get("db_id"),
            "time":  kwargs.get("time"),
        }
        log.info(f"请求的最终参数{sys._getframe().f_code.co_name}:{params}")
        response = self.sget(url, params=params)
        assert response.status_code == 200, "请求返回码不正确"
        log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
        assert response.json().get("code") == 100000
        assert response.json().get("message") == '成功'
        return response.json()



################################ mysql性能诊断 ####################################
    #TODO 慢日志条数2211接口待补充，在慢日志查询里
    def get_mysql_performance_picture(self,args,**kwargs):
        """
        mssql性能诊断图表,ID:1131
        :param args:
            {
             "db_id":数据库资产ID
             "query_filed":
                     性能诊断：
                        performance_qps 每秒查询数
                        thread_connection  数据库连接数
                        mysql_connection_use_rate    数据库连接使用率
                        thread_info   每秒活动线程数
                        lock_time   数据库锁持续时间
                        tps   TPS
                        slow_log  慢日志条数
                    监控大屏:
                        cconnected 对应 数据库登录图表
                        innobufreadreq 逻辑读图表
                        questions SQL执行图表
                        commit SQL提交图表
                        qps    QPS图表
                        innodb_rw    Innodb 读写
                        txlock   LOCK 图表
                        binary_log   binlog数量
                        tpsqps         TPS 和 QPS在一张图表里 提供给主从实例
                        sqlquery 每秒查询数
                        tps  TPS
            }
        :return:
        """
        url = f"{self.osm_url}/api/monitor/v1/mysqldb/picture"
        params = {
            "db_id": kwargs.get("db_id"),
            "query_filed": args.get("query_filed"),
            "start_time": (nowtime + timedelta(days=-24)).strftime("%Y-%m-%d %H:%M:%S"), #默认读取24小内的数据
            "end_time": nowtime.strftime("%Y-%m-%d %H:%M:%S")
        }
        log.info(f"请求的最终{sys._getframe().f_code.co_name}:{params}")
        response = self.sget(url, params=params)
        assert response.status_code == 200, "请求返回码不正确"
        # log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
        assert response.json().get("code") == 100000
        assert response.json().get("message") == '成功'
        return response.json()



    def get_mysql_performance_qps_detail(self,**kwargs):
        """
        msyql-每秒查询数-详情，从图表内点击进去 ID:2693
        :param args:
        :param kwargs:
           {
             db_id: 数据库id
             time:从mssql性能诊断图表获取：ID：1131
           }
        :return:
        """
        url = f"{self.osm_url}/api/monitor/v1/mysqldb/qps_detail"
        params = {
            "db_id": kwargs.get("db_id"),
            "time":  kwargs.get("time"),
        }
        log.info(f"请求的最终参数{sys._getframe().f_code.co_name}:{params}")
        response = self.sget(url, params=params)
        assert response.status_code == 200, "请求返回码不正确"
        log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
        assert response.json().get("code") == 100000
        assert response.json().get("message") == '成功'
        return response.json()



    def get_mysql_performance_connection_detail(self,**kwargs):
        """
        msyql-数据库连接数-详情，从图表内点击进去 ID:2711
        :param args:
        :param kwargs:
           {
             db_id: 数据库id
             time:从mssql性能诊断图表获取：ID：1131
           }
        :return:
        """
        url = f"{self.osm_url}/api/monitor/v1/mysqldb/connection_detail"
        params = {
            "db_id": kwargs.get("db_id"),
            "time":  kwargs.get("time"),
        }
        log.info(f"请求的最终参数{sys._getframe().f_code.co_name}:{params}")
        response = self.sget(url, params=params)
        assert response.status_code == 200, "请求返回码不正确"
        log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
        assert response.json().get("code") == 100000
        assert response.json().get("message") == '成功'
        return response.json()



    def get_mysql_performance_connection_use_rate_detail(self,**kwargs):
        """
        mysql数据库连接使用率_下钻，从图表内点击进去 ID:5545
        :param args:
        :param kwargs:
           {
             db_id: 数据库id
             time:从mssql性能诊断图表获取：ID：1131
           }
        :return:
        """
        url = f"{self.osm_url}/api/monitor/v1/mysqldb/connection_use_rate_detail"
        params = {
            "db_id": kwargs.get("db_id"),
            "time":  kwargs.get("time"),
        }
        log.info(f"请求的最终参数{sys._getframe().f_code.co_name}:{params}")
        response = self.sget(url, params=params)
        assert response.status_code == 200, "请求返回码不正确"
        log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
        assert response.json().get("code") == 100000
        assert response.json().get("message") == '成功'
        return response.json()


    def get_mysql_performance_thread_detail_detail(self,**kwargs):
        """
        mysql-每秒活动线程数-详情，从图表内点击进去 ID:2705
        :param args:
        :param kwargs:
           {
             db_id: 数据库id
             time:从mssql性能诊断图表获取：ID：1131
           }
        :return:
        """
        url = f"{self.osm_url}/api/monitor/v1/mysqldb/thread_detail"
        params = {
            "db_id": kwargs.get("db_id"),
            "time":  kwargs.get("time"),
        }
        log.info(f"请求的最终参数{sys._getframe().f_code.co_name}:{params}")
        response = self.sget(url, params=params)
        assert response.status_code == 200, "请求返回码不正确"
        log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
        assert response.json().get("code") == 100000
        assert response.json().get("message") == '成功'
        return response.json()



    def get_mysql_performance_lock_time_detail(self,**kwargs):
        """
        mysql-数据库锁持续时间-详情，从图表内点击进去 ID:2709
        :param args:
        :param kwargs:
           {
             db_id: 数据库id
             time:从mssql性能诊断图表获取：ID：1131
           }
        :return:
        """
        url = f"{self.osm_url}/api/monitor/v1/mysqldb/lock_time_detail"
        params = {
            "db_id": kwargs.get("db_id"),
            "time":  kwargs.get("time"),
        }
        log.info(f"请求的最终参数{sys._getframe().f_code.co_name}:{params}")
        response = self.sget(url, params=params)
        assert response.status_code == 200, "请求返回码不正确"
        log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
        assert response.json().get("code") == 100000
        assert response.json().get("message") == '成功'
        return response.json()


