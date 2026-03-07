# -*- coding: utf-8 -*-
import requests

from conftest import key


class SendMsg():
    def __init__(self):
        # self.key = "83ca1fe4-e906-4e0a-b779-f42b2874c975"
        # self.key = "4e108d29-453c-41ab-870b-ae794b1f330c"  # 每日构建群 -自动化小弟
        # self.key = "bdc2c2a4-7b0e-4955-b39b-deae2bc916c3"  # 大群 -自动化小弟
        self.key = key  # 大群 -自动化小弟
        self.wx_url = f'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={self.key}'

    def file_upload(self, flie):
        id_url = f'https://qyapi.weixin.qq.com/cgi-bin/webhook/upload_media?key={self.key}&type=file'  # 上传文件接口地址
        data = {'file': open(flie, 'rb')}  # post jason
        response = requests.post(url=id_url, files=data)  # post 请求上传文件
        json_res = response.json()  # 返回转为json
        self.media_id = json_res['media_id']  # 提取返回ID
        data = {"msgtype": "file",
                "file": {"media_id": self.media_id}}  # post json
        r = requests.post(url=self.wx_url, json=data)  # post请求消息
        assert r.json().get("errmsg") == "ok"
        assert r.json().get("errcode") == 0

    def msg_send(self, msg):
        # content = f"""<font color="Blue">加固版本Acunetix扫描结束：</font>\n
        #                 ><font color="comment">环境版本：{msg.get("url")}</font>\n
        #                 ><font color="comment">环境路径：{msg.get("ip")}</font>\n
        #                 ><font color="comment">环境用户：{msg.get("user")}</font>\n
        #                 ><font color="comment">环境密码：{msg.get("pwd")}</font>\n
        #                 """
        data = {
            "msgtype": "markdown",
            "markdown": {
                "content": msg
            }
        }

        response = requests.post(self.wx_url, json=data,
                                 auth=('Content-Type', 'application/json'))
        assert response.json().get("errcode") == 0
        assert response.json().get("errmsg") == "ok"


if __name__ == '__main__':
    import time

    proxy = "192.168.51.234"
    new_day = time.strftime("%Y%m%d", time.localtime(time.time()))
    new_time = time.strftime("%m.%d %H.%M.%S", time.localtime(time.time()))

    content = f"""<font color="red">【请阅】每日自动化-加固版本：</font>\n
                    ><font color="comment">环境路径：[{proxy}](https://{proxy}/)</font>\n
                    ><font color="comment">环境用户：{"security"}</font>\n
                    ><font color="comment">环境密码：{"admin123"}</font>\n
                    ><font color="comment">版本：{"admin123"}</font>\n
                    ><font color="comment">报告地址：[ronghe_{new_time}](http://192.168.240.88:1234/Jiagu_DeployIpcReport/{new_day}/ronghe_{new_time})</font>\n
                    """
    smsg = SendMsg()
    smsg.msg_send(content)
