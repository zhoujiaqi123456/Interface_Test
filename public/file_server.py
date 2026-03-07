# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup


class IpcJava():
    """
    获取每日构建包
    """

    def __init__(self, url=None):
        # self.url = "http://file.mchz.com.cn/projects/capaa/Data_Security_ICP"
        # self.url = "http://file.mchz.com.cn/projects/capaa/Data_Security_ICP/DataSecurity_OneTrunk/"
        # self.url = "http://file.mchz.com.cn/projects/capaa/Data_Security_ICP/DataSecurity_Refactor/"
        self.url = "http://file.mchz.com.cn/projects/capaa/Data_Security_ICP/DataSecurity_Refactor/x86_64/" if not url else url
        self.get_ipc_days()

    def get_ipc_days(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, 'html.parser')
        ipc_days = soup.find_all("a")
        self.ipc_days = [i.attrs["href"] for i in ipc_days]

    def get_day_package_info(self):
        flag = 0
        for day_str in self.ipc_days[::-1]:
            if "202" not in day_str:
                continue
            flag = 1
            url = f"{self.url}/{day_str}"
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            ipc_day_file = soup.find_all("a")
            ipc_day_files = [i.attrs["href"] for i in ipc_day_file]
            is_end = 0
            package_name = None
            for i in ipc_day_files[::-1]:
                if i.endswith(".tar.gz"):
                    package_name = i
                    is_end = 1
                    break
            if is_end:
                self.package_url = f"{url}{package_name}"
                print(f"新包地址：{self.package_url}")
                return self.package_url
            else:
                print(f"{url}路径下没有找到.gpg文件")

        if flag == 0:
            raise TimeoutError("没有找到2021年的ipc包，请检查")


if __name__ == '__main__':
    ulrs = IpcJava(
        "http://file.mchz.com.cn/projects/capaa/Data_Security_ICP/DataSecurity_Refactor/x86_64/patch/")
    ulrs.get_day_package_info()
