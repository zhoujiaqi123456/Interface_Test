# -*- coding:utf-8 -*-
'''
@Time       : 2022/3/31 15:59
@Author     : xiongitng
@FileName   : run.py
@Description:
'''
import pytest
import time
import datetime
import os
import shutil
import json


from conftest import PRJ_EXEC, proxy, ROOTDIR, key
from public.SendMsg import SendMsg

def fun(args):
    pytest.main(
        [args, "--alluredir=./allure_report/allure_raw", "--cache-clear"])




if __name__ == '__main__':
    try:
        starttime = datetime.datetime.now()
        begin_time = time.strftime("%Y-%m-%d %H:%M:%S",
                                   time.localtime(time.time()))
        new_time = time.strftime("%m.%d %H.%M.%S", time.localtime(time.time()))
        marks = "osm and smoking"
        #收集用例
        pytest.main(
            ["-m", marks, "--collect-only",
             "--alluredir=./allure_report/allure_raw", "--clean-alluredir",
             "--cache-clear"])
        #运行用例
        with open("mark_case.json", "r", encoding="utf-8") as load_f:
            load_dict = json.load(load_f)
        for case in load_dict["masrk_cases"]:
            fun(case)
        #收集报告
        os.system(
            rf"allure generate ./allure_report/allure_raw/ -o ./allure_result/sop/ --clean")
        os.system("allure open -h 127.0.0.1 -p 8884 ./allure_result/sop/")
        end_time = time.strftime("%Y-%m-%d %H:%M:%S",
                                 time.localtime(time.time()))
        endtime = datetime.datetime.now()



        # 单独发送到企业微信详细结果
        with open(os.path.join(ROOTDIR, "allure_result", "sop", "widgets",
                               "summary.json"),
                  encoding="utf-8") as f:
            data = json.load(f)
        statistic = data.get("statistic")

        with open(os.path.join(ROOTDIR, "allure_result", "sop", "widgets",
                               "suites.json"),
                  encoding="utf-8") as f:
            data = json.load(f)
        suites = data.get("items")
        ss = ""
        for i in suites:
            ss += f"""{i.get('name')}:总数：{i.get('statistic').get('total')} 成功：{i.get('statistic').get('passed')} 失败：{i.get('statistic').get('failed')} 故障：{i.get('statistic').get('broken')} 跳过：{i.get('statistic').get('skipped')}\n"""

        send_data = {
            "msgtype": "text",
            "text": {
                "content":
                    f"""总数：{statistic.get('total')} 成功：{statistic.get('passed')} 失败：{statistic.get('failed')} 故障：{statistic.get('broken')} 跳过：{statistic.get('skipped')}\n{ss}\n开始时间：{starttime.strftime("%Y-%m-%d %H:%M:%S")}\n结束时间：{endtime.strftime("%Y-%m-%d %H:%M:%S")}\n耗时：{int((endtime - starttime).total_seconds() / 60)} 分""",
                # "mentioned_list": ["xiongting"]
            }
        }
        import requests

        headers = {"Content-Type": "text/plain"}
        send_url = f"https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={key}"
        res = requests.post(url=send_url, headers=headers, json=send_data)
        print(res.text)

    #运行异常结果到企业微信
    except Exception as e:
        print(e)
        send_data = {
            "msgtype": "text",
            "text": {
                "content":
                    f"""运行失败通知，请相关同事及时处理！！！\n产品名称：{os.environ.get("app_sop", "本地运行未配置app_sop")}\n环境路径：https://{proxy}:18443/\n错误信息：{str(e)}\n当前时间：{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}""",
                # "mentioned_list": ["xiongting"]
            }
        }
        import requests

        headers = {"Content-Type": "text/plain"}
        send_url = f"https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={key}"
        res = requests.post(url=send_url, headers=headers, json=send_data)
        print(res.text)



