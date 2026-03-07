# -*- coding: utf-8 -*-
import os

from conftest import JDBCINITFILES, ROOTDIR
from public import python_jdbc
from public.logger import log


class DbConnect():
    def __init__(self, dbtype, ip, port, user, password, db, *args, **kwargs):
        self.dbtype = dbtype.lower()
        self.ip = ip
        self.port = port
        self.user = user
        self.password = password
        self.db = db
        self.login_time_out = kwargs.get("login_time_out", 5)
        self.jar_file = kwargs.get("jar_file")
        self.iskrbs = kwargs.get("iskrbs")
        self.kerberos_config = kwargs.get("kerberos_config")
        self.dirver = kwargs.get("dirver")
        self.url = kwargs.get("url")

        # self.connect_db()

    def connect_db(self):
        self._conn = None

        connect_jar_path = JDBCINITFILES
        base_jdbc_path = os.path.join(ROOTDIR, "jar_files", )
        try:
            if self.dbtype in ["mysql", "mariadb", "rdsmysql"]:
                dirver = self.dirver if self.dirver else "com.mysql.cj.jdbc.Driver"
                url = self.url if self.url else f"jdbc:mysql://{self.ip}:{self.port}/{self.db}?useSSL=false&useUnicode=true&characterEncoding=utf-8&serverTimezone=Asia/Shanghai"
                jar_file = self.jar_file if self.jar_file else os.path.join(
                    base_jdbc_path,
                    "mysql-connector-java-8.0.21.jar")
                self._conn = python_jdbc.connect(connect_jar_path, url=url,
                                                 user=self.user,
                                                 password=self.password,
                                                 jar_path=jar_file,
                                                 driver_name=dirver,
                                                 login_time_out=self.login_time_out)
            elif self.dbtype == "oracle":
                dirver = self.dirver if self.dirver else "oracle.jdbc.OracleDriver"
                url = self.url if self.url else f"jdbc:oracle:thin://@{self.ip}:{self.port}/{self.db}"
                print("url:", url)
                jar_file = self.jar_file if self.jar_file else os.path.join(
                    base_jdbc_path, "ojdbc6.jar")
                self._conn = python_jdbc.connect(connect_jar_path, url=url,
                                                 user=self.user,
                                                 password=self.password,
                                                 jar_path=jar_file,
                                                 driver_name=dirver,
                                                 login_time_out=self.login_time_out)
            elif self.dbtype in ["sqlserver", "mssql"]:
                dirver = self.dirver if self.dirver else "com.microsoft.sqlserver.jdbc.SQLServerDriver"
                url = self.url if self.url else f"jdbc:sqlserver://{self.ip}:{self.port};DatabaseName={self.db};socketTimeout=2000"
                jar_file = self.jar_file if self.jar_file else os.path.join(
                    base_jdbc_path, "mssql-jdbc-6.4.0.jre8.jar")
                self._conn = python_jdbc.connect(connect_jar_path, url=url,
                                                 user=self.user,
                                                 password=self.password,
                                                 jar_path=jar_file,
                                                 driver_name=dirver,
                                                 login_time_out=self.login_time_out)
            elif self.dbtype == "db2":
                dirver = self.dirver if self.dirver else "com.ibm.db2.jcc.DB2Driver"
                url = self.url if self.url else f"jdbc:db2://{self.ip}:{self.port}/{self.db}"
                jar_file = self.jar_file if self.jar_file else os.path.join(
                    base_jdbc_path, "db2jcc4.jar")
                self._conn = python_jdbc.connect(connect_jar_path, url=url,
                                                 user=self.user,
                                                 password=self.password,
                                                 jar_path=jar_file,
                                                 driver_name=dirver,
                                                 login_time_out=self.login_time_out)
            elif self.dbtype == "sybase":
                dirver = self.dirver if self.dirver else "net.sourceforge.jtds.jdbc.Driver"
                url = self.url if self.url else f"jdbc:jtds:sybase://{self.ip}:{self.port}/{self.db}"
                jar_file = self.jar_file if self.jar_file else os.path.join(
                    base_jdbc_path, "sybase.jar")
                self._conn = python_jdbc.connect(connect_jar_path, url=url,
                                                 user=self.user,
                                                 password=self.password,
                                                 jar_path=jar_file,
                                                 driver_name=dirver,
                                                 login_time_out=self.login_time_out)
            elif self.dbtype in ["pgsql", "uxdb", "greenplum", "rdspgsql"]:
                dirver = self.dirver if self.dirver else "org.postgresql.Driver"
                url = self.url if self.url else f"jdbc:postgresql://{self.ip}:{self.port}/{self.db}"
                jar_file = self.jar_file if self.jar_file else os.path.join(
                    base_jdbc_path, "postgresql-42.2.2.jar")
                self._conn = python_jdbc.connect(connect_jar_path, url=url,
                                                 user=self.user,
                                                 password=self.password,
                                                 jar_path=jar_file,
                                                 driver_name=dirver,
                                                 login_time_out=self.login_time_out)
            elif self.dbtype == "gbase":  # gabse83
                dirver = self.dirver if self.dirver else "com.gbasedbt.jdbc.IfxDriver"
                url = self.url if self.url else f"jdbc:gbasedbt-sqli://{self.ip}:{self.port}/{self.db}:INFORMIXSERVER={''}"
                jar_file = self.jar_file if self.jar_file else os.path.join(
                    base_jdbc_path, "gbase.jar")
                self._conn = python_jdbc.connect(connect_jar_path, url=url,
                                                 user=self.user,
                                                 password=self.password,
                                                 jar_path=jar_file,
                                                 driver_name=dirver,
                                                 login_time_out=self.login_time_out)
            elif self.dbtype == "dm":  # dm7
                dirver = self.dirver if self.dirver else "dm.jdbc.driver.DmDriver"
                url = self.url if self.url else f"jdbc:dm://{self.ip}:{self.port}/{self.db}"
                jar_file = self.jar_file if self.jar_file else os.path.join(
                    base_jdbc_path, "Dm7JdbcDriver17.jar")
                self._conn = python_jdbc.connect(connect_jar_path, url=url,
                                                 user=self.user,
                                                 password=self.password,
                                                 jar_path=jar_file,
                                                 driver_name=dirver,
                                                 login_time_out=self.login_time_out)
            elif self.dbtype == "kingbase_v7":  # kingbase v7
                dirver = self.dirver if self.dirver else "com.kingbase.Driver"
                url = self.url if self.url else f"jdbc:kingbase://{self.ip}:{self.port}/{self.db}"
                jar_file = self.jar_file if self.jar_file else os.path.join(
                    base_jdbc_path, "kingbasejdbc4.jar")
                self._conn = python_jdbc.connect(connect_jar_path, url=url,
                                                 user=self.user,
                                                 password=self.password,
                                                 jar_path=jar_file,
                                                 driver_name=dirver,
                                                 login_time_out=self.login_time_out)
            elif self.dbtype == "kingbase_v8":  # kingbase v8
                dirver = self.dirver if self.dirver else "com.kingbase8.Driver"
                url = self.url if self.url else f"jdbc:kingbase8://{self.ip}:{self.port}/{self.db}"
                jar_file = self.jar_file if self.jar_file else os.path.join(
                    base_jdbc_path, "kingbase8-8.2.0.jar")
                self._conn = python_jdbc.connect(connect_jar_path, url=url,
                                                 user=self.user,
                                                 password=self.password,
                                                 jar_path=jar_file,
                                                 driver_name=dirver,
                                                 login_time_out=self.login_time_out)
            elif self.dbtype == "informix":
                dirver = self.dirver if self.dirver else "com.informix.jdbc.IfxDriver"
                url = self.url if self.url else f"jdbc:informix-sqli://{self.ip}:{self.port}/{self.db}:INFORMIXSERVER=demoserver"
                print("url:",url)
                jar_file = self.jar_file if self.jar_file else os.path.join(
                    base_jdbc_path, "Infomix-jdbc-4.10.8.1.jar")
                self._conn = python_jdbc.connect(connect_jar_path, url=url,
                                                 user=self.user,
                                                 password=self.password,
                                                 jar_path=jar_file,
                                                 driver_name=dirver,
                                                 login_time_out=self.login_time_out)
            elif self.dbtype == "gbase87":
                dirver = self.dirver if self.dirver else "com.gbasedbt.jdbc.IfxDriver"
                url = self.url if self.url else f"jdbc:gbasedbt-sqli://{self.ip}:{self.port}/{self.db}"
                jar_file = self.jar_file if self.jar_file else os.path.join(
                    base_jdbc_path, "gbase87.jar")
                self._conn = python_jdbc.connect(connect_jar_path, url=url,
                                                 user=self.user,
                                                 password=self.password,
                                                 jar_path=jar_file,
                                                 driver_name=dirver,
                                                 login_time_out=self.login_time_out)
            elif self.dbtype == "hive":
                dirver = self.dirver if self.dirver else "org.apache.hive.jdbc.HiveDriver"
                url = self.url if self.url else f"jdbc:hive2://{self.ip}:{self.port}/{self.db}"
                jar_file = self.jar_file if self.jar_file else os.path.join(
                    base_jdbc_path,
                    "hive-jdbc-2.3.2-standalone.jar")
                self._conn = python_jdbc.connect(connect_jar_path, url=url,
                                                 user=self.user,
                                                 password=self.password,
                                                 jar_path=jar_file,
                                                 driver_name=dirver,
                                                 login_time_out=self.login_time_out)
            elif self.dbtype == "hana":
                dirver = self.dirver if self.dirver else "com.sap.db.jdbc.Driver"
                url = self.url if self.url else f"jdbc:sap://{self.ip}:{self.port}/{self.db}"
                jar_file = self.jar_file if self.jar_file else os.path.join(
                    base_jdbc_path, "hana.jar")
                self._conn = python_jdbc.connect(connect_jar_path, url=url,
                                                 user=self.user,
                                                 password=self.password,
                                                 jar_path=jar_file,
                                                 driver_name=dirver,
                                                 login_time_out=self.login_time_out)
            elif self.dbtype == "shengtong":
                dirver = self.dirver if self.dirver else "com.oscar.Driver"
                url = self.url if self.url else f"jdbc:oscar://{self.ip}:{self.port}/{self.db}"
                jar_file = self.jar_file if self.jar_file else os.path.join(
                    base_jdbc_path, "st.jar")
                self._conn = python_jdbc.connect(connect_jar_path, url=url,
                                                 user=self.user,
                                                 password=self.password,
                                                 jar_path=jar_file,
                                                 driver_name=dirver,
                                                 login_time_out=self.login_time_out)
            elif self.dbtype == "maxcompute":
                dirver = self.dirver if self.dirver else "com.aliyun.odps.jdbc.OdpsDriver"
                url = self.url if self.url else f"jdbc:odps:{self.ip}/api?project={self.db}"
                jar_file = self.jar_file if self.jar_file else os.path.join(
                    base_jdbc_path,
                    "odps-jdbc-3.0.1-jar-with-dependencies.jar")
                self._conn = python_jdbc.connect(connect_jar_path, url=url,
                                                 user=self.user,
                                                 password=self.password,
                                                 jar_path=jar_file,
                                                 driver_name=dirver,
                                                 login_time_out=self.login_time_out)

            elif self.dbtype == "vertica":
                dirver = self.dirver if self.dirver else "com.vertica.jdbc.Driver"
                url = self.url if self.url else f"jdbc:vertica://{self.ip}:{self.port}/{self.db}"
                jar_file = self.jar_file if self.jar_file else os.path.join(
                    base_jdbc_path, "vertica-jdbc-10.0.1-0.jar")
                self._conn = python_jdbc.connect(connect_jar_path, url=url,
                                                 user=self.user,
                                                 password=self.password,
                                                 jar_path=jar_file,
                                                 driver_name=dirver,
                                                 login_time_out=self.login_time_out)
            elif self.dbtype == "presto":
                dirver = self.dirver if self.dirver else "com.facebook.presto.jdbc.PrestoDriver"
                url = self.url if self.url else f"jdbc:presto://{self.ip}:{self.port}/system/runtime"
                jar_file = self.jar_file if self.jar_file else os.path.join(
                    base_jdbc_path, "presto-jdbc-0.240.jar")
                self._conn = python_jdbc.connect(connect_jar_path, url=url,
                                                 user=self.user,
                                                 password=self.password,
                                                 jar_path=jar_file,
                                                 driver_name=dirver,
                                                 login_time_out=self.login_time_out)
            elif self.dbtype == "kdb":
                dirver = self.dirver if self.dirver else "com.inspur.jdbc.KdDriver"
                url = self.url if self.url else f"jdbc:inspur:thin:@{self.ip}:{self.port}:{self.db}"
                jar_file = self.jar_file if self.jar_file else os.path.join(
                    base_jdbc_path, "kdb_inspur11-jdbc.jar")
                self._conn = python_jdbc.connect(connect_jar_path, url=url,
                                                 user=self.user,
                                                 password=self.password,
                                                 jar_path=jar_file,
                                                 driver_name=dirver,
                                                 login_time_out=self.login_time_out)
            elif self.dbtype == "impala":
                if self.iskrbs:
                    dirver = self.dirver if self.dirver else "com.cloudera.impala.jdbc41.Driver"
                    url = self.url if self.url else f"jdbc:impala://{self.ip}:{self.port}/{self.db}"
                    jar_file = self.jar_file if self.jar_file else os.path.join(
                        base_jdbc_path, "ImpalaJDBC41.jar")
                    self._conn = python_jdbc.connect(
                        connect_jar_path,
                        url=url,
                        ImpalaFQDN=self.kerberos_config.get("ImpalaFQDN"),
                        KrbRealm=self.kerberos_config.get("KrbRealm"),
                        KrbServiceName=self.kerberos_config.get(
                            "KrbServiceName"),
                        KrbsKey=self.kerberos_config.get("KrbsKey"),
                        KrbsConfPath=self.kerberos_config.get("KrbsConfPath"),
                        KeytabPath=self.kerberos_config.get("KeytabPath"),
                        jar_path=jar_file,
                        driver_name=dirver,
                        login_time_out=self.login_time_out,
                        iskrbs=self.iskrbs
                    )
                else:
                    dirver = self.dirver if self.dirver else "com.cloudera.impala.jdbc41.Driver"
                    url = self.url if self.url else f"jdbc:impala://{self.ip}:{self.port}/{self.db};AuthMech=3"
                    jar_file = self.jar_file if self.jar_file else os.path.join(
                        base_jdbc_path, "ImpalaJDBC41.jar")
                    self._conn = python_jdbc.connect(connect_jar_path, url=url,
                                                     user=self.user,
                                                     password=self.password,
                                                     jar_path=jar_file,
                                                     driver_name=dirver,
                                                     login_time_out=self.login_time_out)

                    # raise KeyError("暂不支持impala不带krbs~")

            else:
                raise KeyError("暂不支持~")
        except Exception as e:
            log.info(f'{self.dbtype} connection was faile')
            raise e

    def query_sql(self, sql, query_time_out=None):
        """prepareStatement会先初始化SQL，先把这个SQL提交到数据库中进行预处理，多次使用可提高效率。"""
        if self._conn:
            with self._conn.cursor() as cur:
                try:
                    sql = sql.strip()
                    if sql.endswith(";"):
                        sql = sql[:-1]
                    log.info(f"sql:{sql}")
                    cur.execute("""%s""" % sql,
                                query_time_out=query_time_out)  # 执行sql语句
                    rs = cur.fetchall()  # 一次性返回所有结果集
                    count = len(rs)
                    description = cur.description
                    log.info(f"查询到了{count}条~~")
                    return rs, count, description
                except Exception as e:
                    log.info(str(e))
                    log.info("执行error")
                    raise e
        else:
            log.info('connection was faile')

    def query_sql_by_createStatement(self, sql, query_time_out=None):
        """createStatement不会初始化，没有预处理，每次都是从0开始执行SQL。"""
        if self._conn:
            with self._conn.cursor() as cur:
                try:
                    sql = sql.strip()
                    if sql.endswith(";"):
                        sql = sql[:-1]
                    log.info(f"sql:{sql}")
                    cur.execute_by_createStatement("""%s""" % sql,
                                                   query_time_out=query_time_out)  # 执行sql语句
                    rs = cur.fetchall()  # 一次性返回所有结果集
                    count = len(rs)
                    description = cur.description
                    log.info(f"查询到了{count}条~~")
                    return rs, count, description
                except Exception as e:
                    log.info(str(e))
                    log.info("执行error")
                    raise e
        else:
            log.info('connection was faile')

    def fix_sql(self, sql, query_time_out=None, *args, **kwargs):
        if self._conn:
            if kwargs.get("dsType") in ["Informix"]:
                pass
                #self._conn.setautocommit()

            else:
                self._conn.setautocommit()
            with self._conn.cursor() as cur:
                try:
                    log.info(f"sql:{sql}")
                    cur.execute("""%s""" % sql,
                                query_time_out=query_time_out)  # 执行sql语句executeUpdate,execute

                    #self._conn.commit()
                    return '执行成功!!!!'
                except Exception as e:
                    log.info(str(e))
                    log.info("执行error")
                    return str(e)
        else:
            log.info('connection was faile')

    def close(self):
        try:
            self._conn.close()
        except:
            pass

    def __del__(self):
        self.close()


def test_connect_telnet(ip, port, timeout=180):
    from telnetlib import Telnet
    try:
        telnet = Telnet(host=ip, port=port, timeout=timeout)
        log.info(f"telnet成功:{ip} {port}")
        return 1
    except:
        log.info(f"telnet失败:{ip} {port}")
        return 0


if __name__ == '__main__':
    # print("*" * 80)
    # print("mysql")
    # db = DbConnect("Dm", "192.168.51.222", 6667, "SYSDBA", "Hzmc4321$", "test")
    # db.connect_db()
     #db.query_sql("select * from yunwei_mask.testa")

    db2 = DbConnect("Pgsql", "192.168.51.222",6674, "postgres", "postgres","uxdb")
    db2.connect_db()
    print(db2.query_sql('select * from  gongdan."public".quick'))#insert into yunwei_mask.testa values(1)
    #db2.query_sql("select * from yunwei_mask.testa")
    db2.close()
    #
    # print("*" * 80)
    # print("oracle")
    # db2 = DbConnect("oracle", "192.168.202.2", 1521, "product_mask", "123456", "orcl")
    # db2 = DbConnect("Oracle", "192.168.51.149", 8880, "sh", "sh",
    #                 "PDB_TEST_FSB")
    # db2.connect_db()
    # print("*" * 80)
    # print("sqlserver")
    # db2 = DbConnect("sqlserver", "192.168.202.7", 1433, "sa", "hzmc321#", "test")
    # db2.query_sql("SELECT * FROM product_mask.dbo.[中文表1]")
    # db2.close()
    #
    # print("*" * 80)
    # print("db2")
    # db2 = DbConnect("db2", "192.168.239.111", 50001, "db2inst2", "db2inst2", "test")
    # db2.query_sql("SELECT * FROM DB2INST1.COMMIT_ROLLBACK_TABLE")
    # db2.close()
    #
    # print("*" * 80)
    # print("sybase")
    # db2 = DbConnect("sybase", "192.168.202.53", 7000, "sa", "hzmcdba", "test")
    # db2.query_sql("SELECT * from mask_test.dbo.ABCDEFabcdefghijklmnopqrstuvwx")
    # db2.close()
    #
    # print("*" * 80)
    # print("postgresql")
    # db2 = DbConnect("postgresql", "192.168.239.66", 5432, "postgres", "postgres", "postgres")
    # db2.query_sql("select * from testdb.commit_rollback_table")
    # db2.close()
    #
    # print("*" * 80)
    # print("gbase")  # gabse83
    # db2 = DbConnect("gbase", "192.168.240.62", 12263, "gbasedbt", "gbasedbt", "gbase8s")
    # db2.query_sql("select * from company")
    # db2.close()
    #
    # print("*" * 80)
    # print("dm")  # dm7
    # db2 = DbConnect("dm", "192.168.238.43", 5236, "sysdba", "hzmc4321$", "YUNWEI_MASK")
    # db2.query_sql("SELECT * FROM YUNWEI_MASK.中文表")
    # db2.close()
    #
    # print("*" * 80)
    # print("开始测试kingbase v8  v7 没有可用 informix gbase87 没可用")
    # db2 = DbConnect("kingbase_v8", "192.168.240.147", 54321, "SYSTEM", "system", "TEST")
    # db2.query_sql('select * from "SYS_HM"."CHECK_PARAM"')
    # db2.close()
    #
    # print("*" * 80)
    # print("mariadb")
    # db2 = DbConnect("mariadb", "192.168.202.128", 3306, "root", "hzmcdba", "test")
    # db2.query_sql('select * from 100wdata', 1000)
    # db2.close()
    #
    # print("*" * 80)
    # print("hive")
    # # db2 = DbConnect("hive", "192.168.238.82", 10000, "root", "hzmcdba", "test", login_time_out=1)
    # db2 = DbConnect("hive", "192.168.238.84", 10000, "root", "hzmcdba", "test", login_time_out=50)
    # db2.query_sql('select * from test.a', 1000)
    # db2.close()
    #
    # print("*" * 80)
    # print("uxdb cache 没环境   开始测试hana ")
    # db2 = DbConnect("hana", "192.168.239.238", 30015, "system", "Hana0oracle", "", login_time_out=1000)
    # db2.query_sql('SELECT * FROM C1', 1000)
    # db2.close()
    #
    # print("*" * 80)
    # print("greenplum")
    # db2 = DbConnect("greenplum", "192.168.239.111", 5432, "gpadmin", "gpadmin", "gpadminDB", login_time_out=1000)
    # db2.query_sql('select * from testzn.test_alltypes', 1000)
    # db2.close()
    #
    # print("*" * 80)
    # print("shengtong")  # 192.168.238.213:2003/OSRDB
    # db2 = DbConnect("shengtong", "192.168.238.213", 2003, "SYSDBA", "szoscar55", "OSRDB", login_time_out=1000)
    # db2.query_sql('SELECT * FROM WANGZQ.中文表', 1000)
    # db2.close()

    # # # informix
    # db2 = DbConnect("informix", "192.168.202.45", 1528, "test", "test1234",
    #                 "test2")
    # db2.connect_db()
    # print(db2.query_sql("select * from test"))
    # db2.close()
    #
    # # # impala
    # data = {
    #     "iskrbs": 1,
    #     "kerberos_config": {
    #         "ImpalaFQDN": "cdh6-s2",
    #         "KrbRealm": "CDH6.COM",
    #         "KrbServiceName": "impala",
    #         "KrbsKey": "impala/cdh6-m@CDH6.COM",
    #         "KrbsConfPath": os.path.join(ROOTDIR, "config", "impala_kerberos",
    #                                      "krb5.conf"),
    #         "KeytabPath": os.path.join(ROOTDIR, "config", "impala_kerberos",
    #                                    "impala.keytab")
    #     }
    # }
    # db2 = DbConnect("impala", "192.168.239.213", 21050, "", "",
    #                 "default", **data)
    # db2.connect_db()
    # print(db2.query_sql_by_createStatement("select * from test_ddl.t1"))
    # db2.close()


   # impala ldap
   #  db2 = DbConnect("impala", "192.168.51.33", 21051, "impala", "impala123",
   #                  "default")
   #  try:
   #      db2.connect_db()
   #  except:
   #      print("!")
   #  print(db2.query_sql("select * from joytest.t1 where id1=-14 union select * from joytest.t2 where id1=-124;"))
    # for i in range(1, 10000):
    #     # db2.query_sql("insert into joytest.bigsize_table values (3,'col_2_char','col_3_varchar','col_4_string','2019-05-08 15:33:00');")
    #     db2.fix_sql("insert into joytest.bigsize_table values (2,'wangzq','wzq','wangzhiqiang','2019-05-09 15:33:00');")
    #     db2.fix_sql("insert into joytest.bigsize_table values (3,'ronghe','fangshuiba','fanghuoqiang','2018-05-08 15:33:00');")
    #     db2.fix_sql("insert into joytest.bigsize_table values (4,'col_2_char','col_3_varchar','col_4_string','2019-05-08 15:33:00');")
    #     db2.fix_sql("insert into joytest.bigsize_table values (5,'wangzq','wzq','wangzhiqiang','2019-05-09 15:33:00');")
    #     db2.fix_sql("insert into joytest.bigsize_table values (6,'ronghe','fangshuiba','fanghuoqiang','2018-05-08 15:33:00');")
    # db2.close()


