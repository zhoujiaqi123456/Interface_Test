# -*- coding:utf-8 -*-
"""
从 YAPI 爬取接口信息并生成 YAML 文件
使用 googletrans 将中文翻译成英文下划线命名
"""
import requests
import time
import os
import sys
from ruamel.yaml import YAML
import json
import logging

# 添加项目根目录到路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from public.translator import Translator


class GetYapi(object):

    def __init__(self, userapi, passwdapi, group_id):
        """
        初始化
        :param userapi: YAPI 用户邮箱
        :param passwdapi: YAPI 密码
        :param group_id: YAPI 项目组 ID
        """
        # 初始化日志
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        self.logs = logging.getLogger(__name__)

        self.data = {'email': userapi,
                     'password': passwdapi}
        self.pwd = passwdapi
        self.group_id = group_id
        self.session = requests.session()
        self.apiurl = "http://yapi.u-breath.cn:9009"
        self.pathdicts = {}  # 存取单个从 yaml 内抓去的数据
        self.count = 0  # 统计接口总数
        self.filecount = 0  # 统计 yaml 总数
        self.root_dir = os.path.dirname(os.path.dirname(os.path.abspath(".")))
        self.yaml_dir = ""  # 写入 yaml 的路径
        self.pathid = ""  # 用于写入总文件内的 ID
        self.total_file = os.path.join(self.root_dir, "yaml", "total_iface_info.yaml")
        self.id_list = set()
        self.total_data = {}  # 存总的接口数据
        self.project_id = None  # 项目 ID
        self.translator = Translator()  # 翻译器
        
        # 读取总接口信息文件，用于判断新增接口
        yml = YAML(typ='rt')
        yml.preserve_quotes = True
        if os.path.exists(self.total_file):
            with open(self.total_file, encoding='utf-8') as cf:
                data = yml.load(cf)
                if data:
                    for key in data.keys():
                        self.id_list.add(key)
        loginheader = {'Content-Type': 'application/json;charset=utf-8'}
        # 登录
        res = self.session.post(url=self.apiurl + "/api/user/login", json=self.data, verify=False, headers=loginheader)
        self.logs.info("登录 yapi 结果：{}".format(res.json().get("errmsg")))

    def create_yaml_by_yapi(self):
        """创建 yaml 文件"""
        self.__get_project_id()

    def __get_project_id(self):
        """
        第一个接口：获取 project 信息，根据产品 id(group_id) 获取对应的模块列表
        找到"轻量化肺功能"对应的 _id=309
        """
        getid = {'group_id': self.group_id, 'page': '1', 'limit': '500000'}
        res = self.session.get(url=self.apiurl + "/api/project/list", verify=False, params=getid)
        self.logs.info("获取项目列表结果：{}".format(res.json().get("errmsg")))
        
        # 获取模块列表
        ids = res.json().get("data").get("list")
        for i in range(len(ids)):
            self.pathmodulename = ids[i].get("name")
            if self.pathmodulename == "轻量化肺功能":
                self.project_id = ids[i].get("_id")
                self.basepath = ids[i].get("basepath")  # 获取基地址，用于路径拼接
                self.logs.info("找到模块【{}】, project_id={}, basepath={}".format(
                    self.pathmodulename, self.project_id, self.basepath))
                
                # 创建根目录
                yaml_path = os.path.join(self.root_dir, "yaml", self.pathmodulename)
                if os.path.exists(yaml_path) is False:
                    os.makedirs(yaml_path)
                
                # 调用第二个接口，获取分类和接口列表
                self.__get_interface_list_by_project_id(self.project_id, yaml_path)
                break
        
        if not self.project_id:
            self.logs.error("未找到模块【轻量化肺功能】")

    def __get_interface_list_by_project_id(self, project_id, yaml_path):
        """
        第二个接口：根据 project_id 获取所有分类和接口列表
        http://yapi.u-breath.cn:9009/api/interface/list_menu?project_id=309
        :param project_id: 项目 ID
        :param yaml_path: yaml 文件存储路径
        """
        params = {'project_id': project_id}
        details = self.session.get(self.apiurl + "/api/interface/list_menu", params=params, verify=False).json()
        self.logs.info("获取接口分类列表结果：{}".format(details.get("errmsg")))
        
        if len(details.get("data")) > 0:
            for category in details.get("data"):
                cat_id = category.get("_id")
                cat_name = category.get("name")
                interface_list = category.get("list", [])
                
                # 翻译分类名称
                cat_name_en = self.translator.translate_filename(cat_name)
                
                self.logs.info("处理分类【{}】(ID: {}), 包含 {} 个接口".format(cat_name, cat_id, len(interface_list)))
                
                # 创建分类文件夹（使用英文命名）
                category_dir = os.path.join(yaml_path, cat_name_en)
                if not os.path.exists(category_dir):
                    os.makedirs(category_dir)
                    self.logs.info("创建分类文件夹：{}".format(category_dir))
                
                self.yaml_dir = category_dir
                
                # 遍历该分类下的所有接口
                for interface in interface_list:
                    pathid = interface.get("_id")
                    title = interface.get("title")
                    self.logs.info("  处理接口：{} (ID: {})".format(title, pathid))
                    
                    # 调用第三个接口，获取接口详细信息
                    self.__get_pathdata_by_pathid(pathid)

    def __get_pathdata_by_pathid(self, pathid):
        """
        第三个接口：根据 pathid 获取每个接口的详细信息
        http://yapi.u-breath.cn:9009/api/interface/get?id=28060
        :param pathid: 接口 id
        """
        data_dict = {}
        res = self.session.get(url=self.apiurl + "/api/interface/get?id=%s" % pathid, verify=False).json()
        pathdata = res.get("data")
        
        if not pathdata:
            self.logs.error("接口 ID {} 获取数据失败".format(pathid))
            return
        
        data_dict["module_name"] = self.pathmodulename  # 接口所属模块名称
        
        # 接口 case_suite（使用英文命名）
        name = pathdata.get("query_path").get("path").split('/')
        base_name = name[-1].lstrip(':')
        
        # 翻译接口名称
        base_name_en = self.translator.translate_method_name(base_name)
        case_suite = base_name_en + str(pathid) + "_test"
        
        # 处理要写入 yaml 的数据
        data_dict["case_suite"] = case_suite  # yaml 文件名
        data_dict["description"] = pathdata.get("title")  # 接口名称（中文）
        data_dict["module_class"] = "Test" + str(pathid)  # 接口名称
        data_dict["url"] = self.basepath + pathdata.get("path")  # 接口地址
        data_dict["method"] = pathdata.get("method")  # 接口请求方法
        
        # 处理请求头
        headers_dict = {"Authorization": '$token'}
        if pathdata.get("req_headers"):
            for header in pathdata.get("req_headers"):
                if header.get("name") and header.get("value"):
                    headers_dict[header.get("name")] = header.get("value")
        data_dict["headers"] = headers_dict
        
        # 处理 query 参数
        params_data = {}
        if pathdata.get("req_query"):
            for requestdata in pathdata.get("req_query"):
                # 如果是必填参数，使用 {{param}} 格式
                param_name = requestdata.get("name")
                if requestdata.get("required") == "1":
                    params_data[param_name] = f'{{{{{param_name}}}}}'
                else:
                    params_data[param_name] = ""
        data_dict['params'] = params_data
        
        # 处理 form 表单数据 (req_body_form)
        form_data = {}
        if pathdata.get("req_body_form"):
            for form_item in pathdata.get("req_body_form"):
                param_name = form_item.get("name")
                if form_item.get("required") == "1":
                    form_data[param_name] = f'{{{{{param_name}}}}}'
                else:
                    form_data[param_name] = ""
        data_dict['data'] = form_data if form_data else ""
        
        # 处理 JSON 数据 (优先处理 req_body_other 和 req_body_is_json_schema)
        key_value_dict = {}
        if pathdata.get("req_body_type") == "json" and pathdata.get("req_body_other"):
            try:
                json_data = json.loads(pathdata.get("req_body_other"))
                self.logs.info("获取出来的 json 参数为{}".format(json_data))
                
                # 如果是 JSON Schema 格式，解析 properties
                if json_data.get("properties"):
                    for k, v in json_data.get("properties").items():
                        # 检查是否必填
                        is_required = False
                        if "required" in json_data:
                            is_required = k in json_data.get("required", [])
                        
                        if is_required:
                            key_value_dict[k] = f'{{{{{k}}}}}'
                        else:
                            key_value_dict[k] = ""
                # 如果是普通 JSON 对象
                elif isinstance(json_data, dict):
                    for k in json_data.keys():
                        key_value_dict[k] = f'{{{{{k}}}}}'
            except json.JSONDecodeError:
                self.logs.warning("JSON 解析失败：{}".format(pathdata.get("req_body_other")))
        
        data_dict["json"] = key_value_dict if key_value_dict else ""
        
        # 处理文件上传
        data_dict["files"] = ""
        
        # 处理时间
        data_dict["up_time"] = time.strftime("%Y-%m-%d %H:%M:%S",
                                                time.localtime(int(pathdata.get("up_time"))))  # 接口变更时间
        data_dict["add_time"] = time.strftime("%Y-%m-%d %H:%M:%S",
                                              time.localtime(int(pathdata.get("add_time"))))  # 接口添加时间
        data_dict["path_creat_user"] = pathdata.get("username")  # 接口创建者
        self.pathdicts = data_dict
        self.pathid = pathid  # 设置当前接口 ID
        
        # 将数据写入 totalyaml
        if self.pathid not in self.id_list or not self.id_list:
            # 创建总用例文件
            self.__create_total_file()
            # 创建 yaml 用例文件
            self.__create_yaml_file()
        
        self.count += 1
        self.logs.info(("第{}个接口{}的数据已经爬取完毕").format(self.count, data_dict["url"]))

    def __create_total_file(self):
        """创建总接口信息文件，用于过滤已经生成过文件的接口"""
        self.total_data = {}
        self.total_data[self.pathid] = self.pathdicts.get("description")
        yml = YAML(typ='rt')
        yml.preserve_quotes = True
        with open(self.total_file, 'a', encoding='utf-8') as s:
            yml.dump(self.total_data, s)

    def __create_yaml_file(self):
        """创建 yaml 文件"""
        self.logs.info("接口获取的数据为{}".format(self.pathdicts))
        yaml_data = {}  # 整个文档
        testinfo = {}  # 存入 test_info
        testinfo["case_suite"] = self.pathdicts.get("case_suite")
        testinfo["description"] = self.pathdicts.get("description")
        testinfo["module_class"] = self.pathdicts.get("module_class")
        yaml_data["testinfo"] = testinfo

        yaml_data["premise"] = ""
        yaml_data["set_up"] = ""
        yaml_data["tear_down"] = ""
        # 加入 case 文件
        case_list = []
        case_data = {}
        case_data["test_name"] = ""
        case_data["info"] = self.pathdicts.get("description")
        case_data["mark"] = ""
        case_data["method"] = self.pathdicts.get("method")
        case_data["url"] = self.pathdicts.get("url")
        case_data["headers"] = self.pathdicts.get("headers")
        case_data["timeout"] = 8
        case_data["params"] = self.pathdicts.get("params")
        case_data["data"] = self.pathdicts.get("data")
        case_data["files"] = self.pathdicts.get("files")
        case_data["json"] = self.pathdicts.get("json")
        case_data["status"] = ""
        case_data["extract"] = ""
        case_data["expects"] = ""
        case_list.append(case_data)
        # 加入 case
        yaml_data["test_case"] = case_list

        # 装写入的配置文件写入到 yaml
        yaml_file_name = self.pathdicts.get("case_suite") + ".yaml"
        yaml_data_file = os.path.join(self.yaml_dir, yaml_file_name)
        self.filecount += 1
        self.logs.info("创建第{}个文件：{}".format(self.filecount, yaml_file_name))
        yml = YAML(typ='rt')
        yml.preserve_quotes = True
        with open(yaml_data_file, 'w', encoding='utf-8') as s:
            yml.dump(yaml_data, s)


if __name__ == '__main__':
    data = GetYapi(userapi="jiaqi.zhou@e-linkcare.com", passwdapi="elk@123456", group_id="19")
    data.create_yaml_by_yapi()
