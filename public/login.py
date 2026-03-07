# -*- coding: utf-8 -*-
import base64
import hashlib
import os
import re
import sys
import time
import warnings
from functools import wraps

import jpype

from conftest import JDBCINITFILES

warnings.filterwarnings('ignore')
import requests

from public.logger import log


def wait_cookie(login, delay=0.01):
    def deco_func(func):
        @wraps(func)
        def wrapper(*args, **kwargs):

            response = func(*args, **kwargs)
            try:
                # if response.json().get("message") == "not login":
                if response.status_code != 200:
                    # time.sleep(120)
                    login(args[0],"qaadmin", "hzmc12345678")#登录默认

                    # headers = {"Content-Type": "text/plain"}
                    # send_url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=3c0d5616-62b6-4f0f-b98f-7e034105015a"
                    # send_data = {
                    #     "msgtype": "text",
                    #     "text": {
                    #         "content": f"""当前时间：{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))} args:{args} kwargs:{kwargs} response:{response.json()}""",
                    #         # "mentioned_list": ["zhangqian", "@all"]
                    #         "mentioned_list": ["xiongting"]
                    #     }
                    # }
                    # res = requests.post(url=send_url, headers=headers,
                    #                     json=send_data,verify=False)
                    # print(res.json())
                    response = func(*args, **kwargs)
            except Exception as e:
                print(f"{str(e)}:{response.text[:200]}")
            return response

        return wrapper

    return deco_func


# 登录
class Login():

    def __init__(self, sso_ip,url_ip):
        self.headers = {"Content-Type": "application/json;charset=UTF-8"}
        self.get_headers = {}
        self.osm_url = f"https://{url_ip}:8088"
        self.identity_url = f"https://{sso_ip}:18020"
        # 初始化
        self.ss = requests.Session()
        # self.order_url = f"http://{url_ip}:18021"

    def login(self, username, password):
        flag = 1
        # self.health_mgrs()
        while flag < 8:
            try:
                self.login_here_bug(username, password)
                log.info(f"登录成功")
                break
            except Exception as e:
                print(f"login_here_bug_flag_{flag}:{e}")
                time.sleep(5)
                flag += 1


    @wait_cookie(login)
    def spost(self, url, *args, **kwargs):
        headers = kwargs.pop("headers") if kwargs.get(
            "headers") else self.headers
        log.info(f"url:{sys._getframe().f_code.co_name}:{url}")
        log.info(f"headers:{sys._getframe().f_code.co_name}:{headers}")
        log.info(f"kwargs:{sys._getframe().f_code.co_name}:{kwargs}")
        res = self.ss.post(url, headers=headers, verify=False, *args,
                           **kwargs)
        log.info(
            f"response len:{len(res.content)}")
        if len(res.content) < 10000:
            log.info(
                f"response:{sys._getframe().f_code.co_name}:{res.status_code} {res.json()}")
        return res

    @wait_cookie(login)
    def sget(self, url, *args, **kwargs):
        if "18020" in url:
            headers = kwargs.pop("headers") if kwargs.get(
                "headers") else self.headers
        else:
            headers = self.get_headers           #OSM get不能传content-type
        log.info(f"url:{sys._getframe().f_code.co_name}:{url}")
        log.info(f"headers:{sys._getframe().f_code.co_name}:{headers}")
        log.info(f"cookie:{sys._getframe().f_code.co_name}:{self.ss.cookies}")
        log.info(f"kwargs:{sys._getframe().f_code.co_name}:{kwargs}")
        res = self.ss.get(url, headers=headers, verify=False, *args,
                         **kwargs)
        #判断reponse返回字节大小，如果小于10000打印到日志
        log.info(
            f"response len:{len(res.content)}")
        if len(res.content) < 10000:
            log.info(
                f"response:{sys._getframe().f_code.co_name}:{res.status_code} {res.json()}")
        return res

    @wait_cookie(login)
    def sdelete(self, url, *args, **kwargs):
        headers = kwargs.pop("headers") if kwargs.get(
            "headers") else self.headers
        log.info(f"url:{sys._getframe().f_code.co_name}:{url}")
        log.info(f"headers:{sys._getframe().f_code.co_name}:{headers}")
        log.info(f"kwargs:{sys._getframe().f_code.co_name}:{kwargs}")
        res = self.ss.delete(url, headers=headers, verify=False, *args,
                             **kwargs)
        log.info(
            f"response len:{len(res.content)}")
        if len(res.content) < 10000:
            log.info(
                f"response:{sys._getframe().f_code.co_name}:{res.status_code} {res.json()}")
        return res

    @wait_cookie(login)
    def sput(self, url, *args, **kwargs):
        headers = kwargs.pop("headers") if kwargs.get(
            "headers") else self.headers
        log.info(f"url:{sys._getframe().f_code.co_name}:{url}")
        log.info(f"headers:{sys._getframe().f_code.co_name}:{headers}")
        log.info(f"kwargs:{sys._getframe().f_code.co_name}:{kwargs}")
        res = self.ss.put(url, headers=headers, verify=False, *args,
                          **kwargs)
        log.info(
            f"response len:{len(res.content)}")
        if len(res.content) < 10000:
            log.info(
                f"response:{sys._getframe().f_code.co_name}:{res.status_code} {res.json()}")
        return res



    def logout(self):
        url = f"{self.osm_url}/sign/logout"
        data = {
            "type": "ALL"
        }
        response = self.ss.post(url, json=data, allow_redirects=False)
        assert response.status_code == 200
        assert response.json().get("success") == True
        assert response.json().get("code") == 200
        assert response.json().get("msg") == '操作成功'

    # def health_mgrs(self):
    #     url = f"{self.osm_url}/ping/mgrs"
    #     response = requests.get(url, verify=False)
    #     log.info(f"{sys._getframe().f_code.co_name}:{url}{response.content}")
    #     max_time = 300
    #     while max_time:
    #         if response.status_code == 200 and response.json().get(
    #                 "code") == 0 and response.json().get(
    #             "success") is True and response.json().get("data").get(
    #             "active") is True:
    #             log.info(f"mgrs 启动成功，用时：{1800 - max_time}S")
    #             break
    #         else:
    #             log.info(f"mgrs 启动中，用时：{1800 - max_time}S")
    #             time.sleep(10)
    #             max_time -= 10
    #             response = requests.get(url, verify=False)
    #             log.info(
    #                 f"{sys._getframe().f_code.co_name}:{url}{response.content}")
    #     if max_time <= 0:
    #         raise RuntimeError("mgrs 启动失败")

    def login_here_bug(self, username, password):
        if hasattr(self, "ss"):
            print("logout")
            try:
                self.logout()
                time.sleep(3)
            except:
                print("logout error")

        # 获取验证码
        response = self.sget(url=f"{self.identity_url}/sign/imageCode")
        log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
        assert response.json().get("success") == True
        assert response.json().get("code") == 200
        assert response.json().get("msg") == '操作成功'
        imageId = response.json()["data"]["imageId"]
        params = {"imageId": imageId}
        rs = self.sget(url=f"{self.identity_url}/auto/loginCode", params=params)
        imageCode = str(rs.text)

        # 登录 统一身份
        user = {}
        user["imageId"], user["imageCode"], user["account"], user[
            "password"] = imageId, imageCode, self.AESEncrypt(
            username), self.AESEncrypt(password)
        response = self.spost(url=f"{self.identity_url}/sign/login", json=user)
        log.info(f"统一身份登录响应:{response.json()}")
        log.info(f"统一身份登录响应:{response.headers}")
        assert response.json().get("success") == True
        assert response.json().get("code") == 200
        assert response.json().get("msg") == '操作成功'
        ssotoken = response.json().get("data").get("token")
        cookies = re.split(';', response.headers["Set-Cookie"])[0]  #统一身份cookies
        log.info(f"Cookie:{cookies}")
        log.info(f"ssotoken:{ssotoken}")
        #self.headers["Authorization"] = ssotoken

        # 登录产品,返回最终token
        response = self.sget(
            url=f"{self.identity_url}/auth/apps/ordered?orderBase=FREQUENCY")
        assert response.status_code == 200
        assert response.json().get("code") == 200
        assert response.json().get("success") == True
        assert response.json().get("msg") == '操作成功'
        apps = response.json()["data"]
        appid = ""
        apptype= ""
        for app in apps:
            apptype = app.get("appType")
            appIndexUrl = app.get("appIndexUrl")
            try:
                if self.osm_url in appIndexUrl:
                    if apptype in ['美创灾备集中管控平台','美创数据库运行安全管理平台','美创全业务容灾','数据复制系统']:
                         appid = app.get('appId')
                         break
            except:
                raise SystemError("没有找到appId~~~,请检查环境。")
        log.info(f"产品为:{apptype}")
        sop_token = self.get_token(appid, ssotoken,
                                     cookies,apptype)
        log.info(f"最终token:{sop_token}")
        return sop_token

    def get_token(self, appid, ssotoken, cookies,apptype):
        """
        获取跳转的cookie
        :param appid: 要跳转的appID
        :param ssotoken: 统一身份的token （因为由同统一身份跳转）
        :param cookies: 要拼接的cookie （涉及多个产品，cookie放一起）
        :return:
        """
        redirection = f"{self.identity_url}/app/redirection"  # 获取token
        params = {
            "appId": appid,
            "token": ssotoken
        }
        headers = {
            "Cookie": cookies,
            "Referer": f"{self.identity_url}/sso.html?appId={appid}",
        }
        res1 = requests.get(redirection, params=params, headers=headers,
                            verify=False, allow_redirects=False, timeout=30)
        if apptype == "美创灾备集中管控平台":
            token = "DRCC " + res1.headers.get("location").split("token=")[1]
        elif apptype == "美创数据库运行安全管理平台":
            token = "OSM " + res1.headers.get("location").split("token=")[1]
        else:
            token = ssotoken
        self.headers["Authorization"] = token
        self.get_headers["Authorization"] = token
        return token

    def AESEncrypt(self, content):
        jvmPath = jpype.getDefaultJVMPath()

        if not jpype.isJVMStarted():
            jpype.startJVM(jvmPath, "-ea",
                           "-Djava.class.path=%s" % os.path.pathsep.join(
                               JDBCINITFILES))
        JDClass = jpype.JClass("com.hzmc.test.AESForNodejs")
        aesHandler = JDClass()
        test = str(aesHandler.encrypt(content))
        return test

    def RSAEncrypt(self, key):
        m = hashlib.md5()
        m.update(key.encode('utf-8'))
        a_md5 = m.hexdigest()
        return a_md5



if __name__ == '__main__':
    capaa = Login("192.168.52.233","192.168.51.233")
    capaa.login("liujj", "hzmc12345")
    # url = f"{capaa.osm_url}/businesses"
    # body = {"name": "a业务2",
    #         "dsName": "a业务2"}
    # response = capaa.spost(url, json=body)
    # assert response.status_code == 200, "请求返回码不正确"
    # log.info(f"{sys._getframe().f_code.co_name}:{response.json()}")
    # print(response)