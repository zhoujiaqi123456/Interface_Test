# -*- coding:utf-8 -*-
'''
@Time       : 2022/4/12 15:45
@Author     : xiongting
@FileName   : ApiMapGather.py
@Description:
'''

from apimap.osm.api_01_businesssystem.BusinessSystem import BussinessSystemApi
from apimap.osm.api_02_assetmanager.assetconfig import AssetConfigApi
from apimap.osm.api_03_monitor.MSSQL_sigle_monitor import MSSQlSingleMonitorApi
from apimap.osm.api_03_monitor.oracle_single_monitor import OracleSingleMonitorApi
from apimap.osm.api_03_monitor.Mysql_monitor import MysqlMonitorApi
from apimap.osm.api_03_monitor.public_monitor import PublicInfoMonitorApi

class OSMMap(BussinessSystemApi,AssetConfigApi,MSSQlSingleMonitorApi,OracleSingleMonitorApi,MysqlMonitorApi,PublicInfoMonitorApi):
    """将所有的api类继承到一个类内"""
    pass



osmapi = OSMMap()

