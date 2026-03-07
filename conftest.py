# -*- coding:utf-8 -*-
'''
@Time       : 2022/4/10 17:38
@Author     : xiongting
@FileName   : conftest.py
@Description:
'''

import json
import os

# 项目目录
ROOTDIR = os.path.dirname(__file__)


# 项目初始化需要用的jar包
JDBCINITFILES = [
    os.path.join(ROOTDIR, "jar_files", "connect_db-1.0-SNAPSHOT.jar"),
    os.path.join(ROOTDIR, "jar_files", "AES.jar")
]
#运行环境
proxy = os.environ.get("PRJ_IP", "192.168.51.146")  ###IPV4格式地址
ssoproxy = os.environ.get("PRJ_IP", "192.168.51.146")  ###IPV4格式地址


# 消息推送
key = os.environ.get("WXkey", "3c0d5616-62b6-4f0f-b98f-7e034105015a")

# 执行方式
PRJ_EXEC = os.environ.get("PRJ_EXEC", "jenkins_ci")


#业务系统名称
businessesname = "AUTOTEST"



def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的item的name和nodeid的中文显示在控制台上
    :return:
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        # print(item.nodeid)
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")




def pytest_collection_finish(session):
    load_dict = {"masrk_cases": []}
    for item in session.items:
        module = item.nodeid.replace(f'::{item.name}', "")
        if module not in load_dict["masrk_cases"]:
            load_dict["masrk_cases"].append(module)

    if "--collect-only" in session.config.invocation_params.args:
        print("====================collection start==================")
        with open("mark_case.json", 'w', encoding="utf-8") as write_f:
            json.dump(load_dict, write_f, indent=4, ensure_ascii=False)
