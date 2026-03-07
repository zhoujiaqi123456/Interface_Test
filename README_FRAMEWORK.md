# 接口自动化框架使用说明

## 框架概述

本框架是一个基于YAPI的接口自动化测试框架，支持：
- 从YAPI自动爬取接口文档
- 自动生成YAML配置文件
- 根据YAML自动生成API封装代码
- 根据YAML自动生成测试用例代码
- 支持pytest参数化测试

## 框架结构

```
Interface_Test/
├── config/              # 配置文件
│   └── yapi_config.py  # YAPI配置
├── tools/              # 工具脚本
│   ├── getyapi.py     # 从YAPI获取数据
│   └── createcasefile.py  # 生成API和测试代码
├── testdata/           # YAML配置文件目录
│   └── 模块名/        # 按模块分类
│       └── 接口名_ID.yaml
├── apimap/            # API封装代码目录
│   └── api_模块名/
│       └── 模块名.py
├── testosmcase/       # 测试用例目录
│   └── test_模块名/
│       └── test_接口名_ID.py
└── run_framework.py    # 主运行脚本
```

## 快速开始

### 1. 配置YAPI

编辑 `config/yapi_config.py`，修改以下配置：

```python
# YAPI服务地址
BASE_URL = "http://yapi.u-breath.cn:9009"

# 项目ID
PROJECT_ID = "309"

# 登录Cookie
COOKIE = "_yapi_token=xxx; _yapi_uid=xxx"
```

### 2. 运行框架

使用交互式菜单：

```bash
python run_framework.py
```

或直接指定操作：

```bash
# 从YAPI获取接口数据
python run_framework.py fetch

# 生成API和测试代码
python run_framework.py generate

# 运行测试
python run_framework.py test

# 执行所有步骤
python run_framework.py all
```

### 3. 单独使用工具

#### 从YAPI获取数据

```python
from tools.getyapi import GetYapi

yapi = GetYapi(
    project_id=309,
    base_url="http://yapi.u-breath.cn:9009",
    cookie="_yapi_token=xxx; _yapi_uid=xxx"
)
yapi.create_yaml_by_yapi()
```

#### 生成代码

```python
from tools.createcasefile import CreateCaseFile

creator = CreateCaseFile()
creator.create_all()
```

## YAML文件格式

YAML文件包含接口的所有配置信息：

```yaml
testinfo:
  interface_id: 28081  # 接口ID
  title: 设置通用配置   # 接口标题
  category: 设置模块   # 所属分类
  description: 接口描述

request:
  url: /api/settings/setCommonSetting  # 接口地址
  method: POST                          # 请求方法
  headers:                              # 请求头
    Authorization: $token
    Content-Type: application/json
  params: {}                            # URL参数
  data: ""                              # 表单数据
  json:                                 # JSON数据
    key1: ""
    key2: ""
  files: ""                             # 文件上传
  timeout: 8                            # 超时时间

test_case:
  - case_name: 冒烟测试                 # 测试用例名称
    description: 基本功能测试             # 描述
    mark: smoke                          # 标记
    skip: false                          # 是否跳过
    extract: ""                          # 数据提取
    validate:                            # 验证规则
      status_code: 200
      contains: ""
      json_path: ""
      json_value: ""
```

## 参数化测试

### 方法1: 修改YAML

在YAML文件中添加多个测试用例：

```yaml
test_case:
  - case_name: 冒烟测试
    description: 基本功能测试
    mark: smoke
    skip: false
    # ... 验证规则

  - case_name: 边界测试
    description: 参数边界测试
    mark: edge
    skip: false
    # ... 验证规则
```

### 方法2: 修改test_api.py

在生成的测试文件中，可以直接使用pytest参数化：

```python
# 添加测试参数
test_data = [
    {"url": "/api/xxx", "json": {"param1": "value1"}},  # 测试1
    {"url": "/api/xxx", "json": {"param1": "value2"}},  # 测试2
]

@pytest.mark.parametrize("kwargs", test_data)
def test_something(self, api_client, kwargs):
    response = api_client._request(**kwargs)
    assert response.status_code == 200
```

## 运行测试

### 运行所有测试

```bash
pytest -v -s
```

### 运行指定模块

```bash
pytest testosmcase/test_模块名/ -v
```

### 运行指定测试文件

```bash
pytest testosmcase/test_模块名/test_接口名.py -v
```

### 运行指定标记的测试

```bash
pytest -m smoke -v  # 运行冒烟测试
pytest -m edge -v   # 运行边界测试
```

### 生成Allure报告

```bash
pytest --alluredir=./report
allure serve report
```

## 常见问题

### Q: 如何获取YAPI的Cookie？

A: 
1. 打开浏览器，访问YAPI
2. 按F12打开开发者工具
3. 在Network标签中查看请求头
4. 复制Cookie中的 `_yapi_token` 和 `_yapi_uid`

### Q: 如何修改测试数据？

A: 有两种方式：
1. 直接修改YAML文件中的参数
2. 在test_api.py中使用pytest参数化添加测试数据

### Q: 如何添加新的测试用例？

A: 在YAML文件的 `test_case` 节点添加新的测试用例配置，然后重新运行 `python run_framework.py generate`

### Q: 如何处理需要登录的接口？

A: 在API类初始化时传入token：

```python
api_client = ModuleNameApi(base_url="http://xxx", token="your_token")
```

## 技术栈

- Python 3.7+
- pytest
- requests
- ruamel.yaml
- allure-pytest
- jsonpath

## 依赖安装

```bash
pip install -r requirements.txt
```

## 许可证

MIT License
