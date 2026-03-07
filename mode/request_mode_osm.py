# -*- coding:utf-8 -*-
'''
@Time       : 2022/3/31 16:37
@Author     : xiongting
@FileName   : request_mode_osm.py
@Description:  OSM的HTTP请求
'''
#自定义方法导入
from public.login import Login
from public.logger import log
import sys
from jsonpath import jsonpath



#业务系统
class BusinessSystemMode(Login):
       """业务系统"""
       def add_business_system(self, *args):
           """新增业务系统,ID:2435"""
           url = f"{self.osm_url}/api/businesses"
           body = {"name": args[0].get("name"),
                   "description": args[0].get("description")}
           log.info(f"请求的最终{sys._getframe().f_code.co_name}:{body}")
           response = self.spost(url, json=body)
           assert response.status_code == 200, "请求返回码不正确"
           log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
           assert response.json().get("code") == 100000
           assert response.json().get("message") == '成功'
           return response.json()


       def get_bussiness_list(self,args):
           """获取业务系统列表,ID:2441"""
           url = f"{self.osm_url}/api/businesses"
           params = {
               "name":args.get("name",''),
               "page": 1,
               "per_page":100,
               "module":args.get("module",''),              #不同模块加载不同数据
               "need_health":args.get("need_health",1)     #是否需要健康度等等统计信息，不传为不需要，传1为需要
           }
           log.info(f"请求的最终{sys._getframe().f_code.co_name}:{params}")
           response = self.sget(url, params=params)
           assert response.status_code == 200, "请求返回码不正确"
           log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
           assert response.json().get("code") == 100000
           assert response.json().get("message") == '成功'
           return response.json()


       def delete_bussiness_by_id(self, id):
           """通过业务系统ID删除业务系统,ID:2473"""
           url = f"{self.osm_url}/api/businesses/{id}"
           # 业务系统ID
           # log.info(f"请求的最终{sys._getframe().f_code.co_name}:{id}")
           response = self.sdelete(url)
           assert response.status_code == 200, "请求返回码不正确"
           log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
           assert response.json().get("code") == 100000
           assert response.json().get("message") == '成功'
           return response.json()


#资产配置
class AssertManagerMode(BusinessSystemMode):
       ###########################公共方法##################3
    def get_dbid(self,args):
        """
        获取资产id
        :param args:
        :return:
        """
        try:
            data = self.get_asset_info(args)
            db_id = jsonpath(data, "$.result.dbs[0].id")[0]
            log.info(f"获取的资产ID为：{db_id}")
            return db_id
        except TypeError:
            log.error("未获取到资产id")

    def get_bussiness_id(self, args):
        """
         todo：获取资产ID，待抽取
        :param args:
        :return:
        """
        pass



    ########################## 添加资产 ########################
    def dbs_connect_test(self,args):
        """数据库连接测试,ID:370
        port :用例内需传入os_port
        user:用例内需传入os_user
        pwd: 用例内需传入os_pwd
        """
        url = f"{self.osm_url}/api/dbs/connect_test"
        body = {
            "conn_type": args.get("conn_type"),
            "ip": args.get("ip"),
            "instance": args.get("instance"),
            "port": args.get("port"),
            "user": args.get("user"),
            "pwd": args.get("pwd")
        }
        log.info(f"请求的最终{sys._getframe().f_code.co_name}:{body}")
        response = self.spost(url, json=body)
        assert response.status_code == 200, "请求返回码不正确"
        log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
        assert response.json().get("code") == 100000
        assert response.json().get("message") == '成功'
        return response.json()


    def hosts_connect_test(self,*args):
        """主机连接测试,ID:376
        """
        url = f"{self.osm_url}/api/hosts/connect_test"
        body = {
            "conn_type": args[0].get("conn_type"),
            "ip": args[0].get("ip"),
            "port": args[0].get("port"),
            "user": args[0].get("user"),
            "pwd": args[0].get("pwd")
        }
        log.info(f"请求的最终{sys._getframe().f_code.co_name}:{body}")
        response = self.spost(url, json=body)
        assert response.status_code == 200, "请求返回码不正确"
        log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
        assert response.json().get("code") == 100000
        assert response.json().get("message") == '成功'
        return response.json()


    def get_is_cdb(self,*args):
        """查询oracle数据库是否为cdb,ID:3367
        """
        url = f"{self.osm_url}/api/dbs/is_cdb"
        params = {
            "ip": args[0].get("ip"),
            "port": args[0].get("port"),
            "instance": args[0].get("instance"),
            "sys_password": args[0].get("sys_password"),
            "user": args[0].get("user"),
            "password": args[0].get("password")
        }
        log.info(f"请求的最终{sys._getframe().f_code.co_name}:{params}")
        response = self.sget(url, params=params)
        assert response.status_code == 200, "请求返回码不正确"
        log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
        assert response.json().get("code") == 100000
        assert response.json().get("message") == '成功'
        return response.json()


    def add_db_users(self,*args):
        """创建数据库用户,ID:3365  目前仅支持oracle数据库
        """
        url = f"{self.osm_url}/api/db_users"
        body = {
            "ip": args[0].get("ip"),
            "port": args[0].get("port"),
            "instance": args[0].get("instance"),
            "sys_password": args[0].get("sys_password"),
            "user": args[0].get("user"),
            "password": args[0].get("password"),
            "os_type": args[0].get("os_type"),   #操作系统类型
            "type": args[0].get("type"),     #数据库类型
            "backup": args[0].get("type")    #是否备份

        }
        log.info(f"请求的最终{sys._getframe().f_code.co_name}:{body}")
        response = self.sget(url, json=body)
        assert response.status_code == 200, "请求返回码不正确"
        log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
        assert response.json().get("code") == 100000
        assert response.json().get("message") == '成功'
        return response.json()



    def get_is_pdbs(self,*args):
        """查询pdb列表,ID:3425
        """
        url = f"{self.osm_url}/api/dbs/pdbs"
        params = {
            "ip": args[0].get("ip"),
            "port": args[0].get("port"),
            "sys_password": args[0].get("sys_password"),
            "user": args[0].get("user"),
            "password": args[0].get("password"),
            "db_id": args[0].get("db_id")            #资产ID,如果传了资产id，即可不传上面几个字段，通用接口，其它模块是否使用？
        }
        log.info(f"请求的最终{sys._getframe().f_code.co_name}:{params}")
        response = self.sget(url, params=params)
        assert response.status_code == 200, "请求返回码不正确"
        log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
        assert response.json().get("code") == 100000
        assert response.json().get("message") == '成功'
        return response.json()



    def add_dbs(self,*args):
        """添加数据库对象,ID:54"""
        url = f"{self.osm_url}/api/dbs"
        body = {
            "business_id": args[0].get("business_id"),
            "os_type": args[0].get("os_type"),
            "ip": args[0].get("ip"),
            "os_user": args[0].get("os_user"),
            "os_pwd": args[0].get("os_pwd"),
            "os_port": args[0].get("os_port"),
            "db_type": args[0].get("db_type"),
            "name": args[0].get("name"),         #资产名称
            "instance": args[0].get("instance"),
            "db_port": args[0].get("db_port"),
            "db_user": args[0].get("db_user"),
            "db_pwd": args[0].get("db_pwd"),
            "is_open": args[0].get("is_open"),   #自动巡检是否打开,0为关闭，1为打开
            "weekday": args[0].get("weekday"),   #自动巡检每周配置
            "clock_on_duty": args[0].get("clock_on_duty"),    #上班巡检时间
            "clock_off_duty": args[0].get("clock_off_duty"),  #下班巡检时间
            "retention_date": args[0].get("retention_date"),
            "proxy_id": args[0].get("proxy_id"),              #tdsql代理id，当数据库类型为tdsql时添加
            "os_conn_type": args[0].get("os_conn_type"),
            "pdbs": args[0].get("pdbs")              #传入列表pdb列表，从get_is_pdbs获取列表信息
        }
        log.info(f"请求的最终{sys._getframe().f_code.co_name}:{body}")
        response = self.spost(url, json=body)
        assert response.status_code == 200, "请求返回码不正确"
        log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
        assert response.json().get("code") == 100000
        assert response.json().get("message") == '成功'
        return response.json()

    ########################## 配置 ########################

    def get_single_db_info(self,*args):
        """单个数据库对象信息,ID:1088"""
        url = f"{self.osm_url}/api/dbs/%s" % args[0].get("db_id")
        params = {
            "ip": args[0].get("ip"),
            "port": args[0].get("port"),
            "sys_password": args[0].get("sys_password"),
            "user": args[0].get("user"),
            "password": args[0].get("password"),
            "db_id": args[0].get("db_id")            #资产ID,如果传了资产id，即可不传上面几个字段，通用接口，其它模块是否使用？
        }
        log.info(f"请求的最终{sys._getframe().f_code.co_name}:{params}")
        response = self.sget(url, params=params)
        assert response.status_code == 200, "请求返回码不正确"
        log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
        assert response.json().get("code") == 100000
        assert response.json().get("message") == '成功'
        return response.json()


    def get_db_users_all(self,*args):
        """查询所有数据库用户,ID:6082"""
        url = f"{self.osm_url}/api/db_users"
        params = {
            "page": 1,
            "per_page": 100,
            "db_type": args[0].get("db_type"),
            "business_ids": args[0].get("business_ids"),
            "ip": args[0].get("ip"),
            "db_id": args[0].get("db_id")            #资产ID
        }
        log.info(f"请求的最终{sys._getframe().f_code.co_name}:{params}")
        response = self.sget(url, params=params)
        assert response.status_code == 200, "请求返回码不正确"
        log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
        assert response.json().get("code") == 100000
        assert response.json().get("message") == '成功'
        return response.json()


    def get_dbusers_by_dbid(self,*args):
        """通过资资产ID查询数据库用户列表,ID:2525"""
        url = f"{self.osm_url}/api/db_users/%s" % args[0].get("db_id")
        params = {
            "page": 1,
            "per_page": 100,
            "user_name": args[0].get("user_name"),
            "user_status": args[0].get("user_status"),
            "password_status": args[0].get("password_status"),
            "query_type": args[0].get("query_type"),
            "pdb_id": args[0].get("pdb_id"),
            "business_ids": args[0].get("business_ids")            #资产ID
        }
        log.info(f"请求的最终{sys._getframe().f_code.co_name}:{params}")
        response = self.sget(url, params=params)
        assert response.status_code == 200, "请求返回码不正确"
        log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
        assert response.json().get("code") == 100000
        assert response.json().get("message") == '成功'
        return response.json()

    def asset_detection(self, db_id):
        """开始资产检测,ID:2299"""
        url = f"{self.osm_url}/api/dbs/{db_id}/asset_detection"
        log.info(f"请求的最终{sys._getframe().f_code.co_name}")
        response = self.spost(url)
        assert response.status_code == 200, "请求返回码不正确"
        log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
        assert response.json().get("code") == 100000
        assert response.json().get("message") == '成功'
        return response.json()

    def get_asset_detection(self, db_id):
           """获取资产检测结果,ID:2467"""
           url = f"{self.osm_url}/api/dbs/{db_id}/asset_detection"
           log.info(f"请求的最终{sys._getframe().f_code.co_name}")
           response = self.sget(url)
           assert response.status_code == 200, "请求返回码不正确"
           log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
           assert response.json().get("code") == 100000
           assert response.json().get("message") == '成功'
           return response.json()

    def get_dbs_associate_list(self, db_id):
           """可关联数据库列表,ID:236"""
           url = f"{self.osm_url}/api/dbs/associate_list"
           param = {
               "id":db_id
           }
           log.info(f"请求的最终{sys._getframe().f_code.co_name}")
           response = self.sget(url,params=param)
           assert response.status_code == 200, "请求返回码不正确"
           log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
           assert response.json().get("code") == 100000
           assert response.json().get("message") == '成功'
           return response.json()

    def dbs_associate(self,args):
           """关联数据库对象,ID:244"""
           url = f"{self.osm_url}/api/dbs/associate"
           body = {
               "type":args.get('type'), # 关联类型-枚举备注: RAC，DG，OGG，Alwayson， MasterSlave，Cluster（暂不支持），DoubleMaster
               "id": args.get('db_id'), # 数据库对象id
               "other_ids": args.get("other_ids"), # 被关联数据库对象id列表
               "ogg_dirs": args.get("ogg_dirs")  #ogg目录（第一个是源端目录）
           }
           log.info(f"请求的最终{sys._getframe().f_code.co_name}")
           response = self.spost(url, json=body)
           assert response.status_code == 200, "请求返回码不正确"
           log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
           assert response.json().get("code") == 100000
           assert response.json().get("message") == '成功'
           return response.json()

    def cluster_detection(self, db_id):
           """集群一键检测,ID:2477"""
           url = f"{self.osm_url}/api/dbs/{db_id}/cluster_detection"
           log.info(f"请求的最终{sys._getframe().f_code.co_name}")
           response = self.spost(url)
           assert response.status_code == 200, "请求返回码不正确"
           log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
           assert response.json().get("code") == 100000
           assert response.json().get("message") == '成功'
           return response.json()

    def get_cluster_detection(self, db_id):
           """查询集群关系,ID:2481"""
           url = f"{self.osm_url}/api/dbs/{db_id}/cluster_detection"
           log.info(f"请求的最终{sys._getframe().f_code.co_name}")
           response = self.sget(url)
           assert response.status_code == 200, "请求返回码不正确"
           log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
           assert response.json().get("code") == 100000
           assert response.json().get("message") == '成功'
           return response.json()

    def disaster_recovery_detection(self, db_id,args):
           """容灾关系一键检测,ID:2479"""
           url = f"{self.osm_url}/api/dbs/{db_id}/disaster_recovery_detection"
           body = {
               "type": args.get("type"), # 容灾类型DG OGG 还有其他接入的容灾产品名称
               "source_dir": args.get("source_dir"), # 源端目录（容灾类型为OGG时需要填写）
               "target_dir": args.get("target_dir") # 目标端目录（容灾类型为OGG时需要填写）
           }
           log.info(f"请求的最终{sys._getframe().f_code.co_name}")
           response = self.spost(url,json=body)
           assert response.status_code == 200, "请求返回码不正确"
           log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
           assert response.json().get("code") == 100000
           assert response.json().get("message") == '成功'
           return response.json()

    def get_disaster_recovery_detection(self, db_id):
           """查询容灾关系,ID:2483"""
           url = f"{self.osm_url}/api/dbs/{db_id}/disaster_recovery_detection"
           log.info(f"请求的最终{sys._getframe().f_code.co_name}")
           response = self.sget(url)
           assert response.status_code == 200, "请求返回码不正确"
           log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
           assert response.json().get("code") == 100000
           assert response.json().get("message") == '成功'
           return response.json()

    ########################## 列表页接口 ########################

    def delete_dbs_by_id(self,id):
        """通过资资产ID删除资产,ID:未在yapi上维护"""
        url = f"{self.osm_url}/api/dbs"
        params = {
            "id" : id
        }
                #资产ID
        log.info(f"请求的最终{sys._getframe().f_code.co_name}:{params}")
        response = self.sdelete(url,params=params)
        assert response.status_code == 200, "请求返回码不正确"
        log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
        assert response.json().get("code") == 100000
        assert response.json().get("message") == '成功'
        return response.json()


    def get_asset_info(self,args):
        """查询资产接口,ID:2445"""
        url = f"{self.osm_url}/api/assets"
        params = {
            "page": args.get("page",1),
            "per_page": args.get("per_page",100),
            "business_ids[]": args.get("business_ids[]",None),   #业务ID列表
            "os_types[]": args.get("os_types[]",None),  # 业务系统类型
            "db_types[]": args.get("db_types[]",None),  # 数据库类型
            "db_id": args.get("db_id",None),  # 数据库ID
            "name": args.get("name",""),  # 数据库名称
            "ip": args.get("ip",""),       #资产IP
            "module": args.get("module",""),   #模块名，不填代表获取所有资产
            "severity": args.get("severity",None), # 当模块名为error_log时有效，不传或None代表显示错误日志的全部资产
            # "reverse": args.get("reverse",'asc'),  #排序，升序asc   降序desc
            # "sort_key": args.get("sort_key"),  # 关键字
            "asset_status": args.get("asset_status",0)  # 默认0全部 1可用资产 2不可用资产 3隔离资产
        }
        log.info(f"请求的最终{sys._getframe().f_code.co_name}:{params}")
        response = self.sget(url, params=params)
        assert response.status_code == 200, "请求返回码不正确"
        log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
        assert response.json().get("code") == 100000
        assert response.json().get("message") == '成功'
        return response.json()

    def get_single_db(self, db_id):
           """获取单个数据库对象，id：1088"""
           url = f"{self.osm_url}//api/dbs/{db_id}"
           params = {
               "id": db_id
           }
           # 资产ID
           log.info(f"请求的最终{sys._getframe().f_code.co_name}:{params}")
           response = self.sget(url, params=params)
           assert response.status_code == 200, "请求返回码不正确"
           log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
           assert response.json().get("code") == 100000
           assert response.json().get("message") == '成功'
           return response.json()

    def get_all_dbs(self, **kwargs):
           """数据库对象列表，id：45"""
           url = f"{self.osm_url}//api/dbs"
           params = {
               "search": kwargs.get("search"),
               "module":kwargs.get("module"),
               "db_type":kwargs.get("db_type")
           }
           # 资产ID
           log.info(f"请求的最终{sys._getframe().f_code.co_name}:{params}")
           response = self.sget(url, params=params)
           assert response.status_code == 200, "请求返回码不正确"
           log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
           assert response.json().get("code") == 100000
           assert response.json().get("message") == '成功'
           return response.json()

    def get_dbuser_asset(self):
        """查询数据库账户资产列表（含pdb） 5551"""
        url = f"{self.osm_url}/api/db_users/asset_names"
        response = self.sget(url)
        assert response.status_code == 200, "请求返回码不正确"
        log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
        assert response.json().get("code") == 100000
        assert response.json().get("message") == '成功'
        return response.json()

    def get_schema_table_auth(self,args):
        """获取schema的表格权限 5553 """
        url = f"{self.osm_url}/api/db_users/one/schema"
        params = {
            "db_id": args.get("db_id",""), #不为空
            "pdb_id": args.get("pdb_id",""), #可为空,oracle pdb 赋权需要传
            "schema": args.get("schema",""), #不为空
            "user_name": args.get("user_name",""), #不为空
            "db_name" :args.get("db_name","") #可为空，sqlserver 数据库赋权需要传
        }
        log.info(f"请求的最终{sys._getframe().f_code.co_name}:{params}")
        response = self.sget(url, params=params)
        assert response.status_code == 200, "请求返回码不正确"
        log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
        assert response.json().get("code") == 100000
        assert response.json().get("message") == '成功'
        return response.json()

    def get_sqlserver_dbs(self,db_id):
        """获取sqlserver实例下的数据库5559"""
        url = f"{self.osm_url}/api/db_users/db_names"
        params = {
            "db_id": db_id #不为空
        }
        response = self.sget(url,params=params)
        assert response.status_code == 200, "请求返回码不正确"
        log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
        assert response.json().get("code") == 100000
        assert response.json().get("message") == '成功'
        return response.json()

    def add_db_user(self,args1,args2):
        """创建数据库用户（new）5523"""
        url = f"{self.osm_url}/api/db_users/create_user"
        params = {
            "db_id": args1.get("db_id",""),#不为空
            "user_name": args1.get("user_name",""),
            "password": args1.get("password",""),
            "sys_password": args1.get("sys_password","")
        }
        body = {
            "db_id": args2.get("db_id", ""),
            "user_name":args2.get("user_name",""),
            "password": args2.get("password", ""),
            "sys_password": args2.get("sys_password", ""),
            "db_names": args2.get("db_names",""),
            "pdb_id": args2.get("pdb_id","")
        }
        response = self.sget(url,params=params,json=body)
        assert response.status_code == 200, "请求返回码不正确"
        log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
        assert response.json().get("code") == 100000
        assert response.json().get("message") == '成功'
        return response.json()




    def put_onekey_dbs_privilege(self,args):
        """
         资产检测内的一键赋权,ID:6487
         涉及的表格为：user_tab_privs、user_sys_privs、user_role_privs
        :param args:
            {
            "db_id" : 数据库ID
            "pspd" : sys密码
            "privs": 权限列表
        }
        :return:
        """
        url = f"{self.osm_url}/api/db_users/{args.get('db_id')}"
        data = {
            "db_id" : args.get("db_id"),
            "pswd" : args.get("pswd","Mcoracle2019"),
            "privs": args.get("privs")
        }
                #资产ID
        log.info(f"请求的最终{sys._getframe().f_code.co_name}:{data}")
        response = self.sput(url,json=data)
        assert response.status_code == 200, "请求返回码不正确"
        log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
        assert response.json().get("code") == 100000
        assert response.json().get("message") == '成功'
        return response.json()



