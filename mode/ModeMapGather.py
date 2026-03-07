# -*- coding:utf-8 -*-
'''
@Time       : 2022/6/17 17:58
@Author     : xiongting
@FileName   : ModeMapGather.py
@Description:  将所有的mode继承到一个集合类内，API层直接调用osmmode
'''

from mode.osm_monitor_mode import PerformanceModeDB
from mode.osm_monitor_mode import MonitorMode
from conftest import proxy,ssoproxy



# 自定义
class BaseServer(PerformanceModeDB,MonitorMode):
        pass


#mode集合类初始化
osmmode = BaseServer(ssoproxy,proxy)



if __name__ == '__main__':
    osm = BaseServer("192.168.51.146")
    res = osm.add_business_system(name="929490",description="020040")
    print(res)