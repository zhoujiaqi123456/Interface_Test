# 接口自动化框架使用说明

## 框架结构

```
Interface_Test/
├── update/                      # YAML文件源目录
│   └── 轻量化肺功能/
│       └── 账号相关/
│           ├── login28294_test.yaml
│           └── get_user_by_id28299_test.yaml  # 包含占位符的示例
├── apimap/                      # API模块目录
│   └── 轻量化肺功能/
│       └── 账号相关/
│           └── 账号相关_yml.py   # 自动生成的API模块
├── testosmcase/                 # 测试用例目录
│   └── 轻量化肺功能/
│       └── 账号相关/
│           ├── login28294_test.py
│           └── get_user_by_id28299_test.py
├── public/
│   ├── base.py                  # 基础类（请求方法、YAML解析）
│   └── login.py                 # 登录类
└── tools/
    └── createcasefile.py        # 代码生成工具
```

## 核心功能

### 1. BaseAPI 基础类

位置：`public/base.py`

**功能：**
- 提供统一的请求方法 `request(file_name, context)`
- 支持YAML文件读取和解析
- 支持参数替换（`{{key}}`格式）

**使用示例：**

```python
from public.base import BaseAPI

class MyAPI(BaseAPI):
    def __init__(self):
        super().__init__(base_url="http://example.com", token="your_token")
    
    def get_user(self):
        # 不需要参数
        return self.request('get_user.yaml')
    
    def get_user_by_id(self, user_id):
        # 需要参数替换
        context = {"userId": user_id}
        return self.request('get_user_by_id.yaml', context=context)
```

### 2. YAML 参数替换

#### 格式说明

YAML文件中的参数支持两种格式：

1. **固定值**：`id: 1` - 直接使用固定值
2. **占位符**：`id: '{{userId}}'` - 需要从外部传入参数替换

#### 示例YAML文件

```yaml
testinfo:
  case_suite: get_user_by_id28299_test
  descrpiton: 根据ID获取用户信息
  module_class: Test28299
test_case:
- test_name: test_get_user_by_id
  info: 根据ID获取用户信息
  method: POST
  url: /pf-lite/api/account/getUserById
  headers:
    Authorization: $token
    Content-Type: application/json
  timeout: 8
  params: {}
  json:
    userId: '{{userId}}'  # 占位符，需要替换
    username: ''
```

#### 参数替换示例

```python
# 方式1：调用时传递参数
api = 账号相关API()
context = {"userId": 123}
result = api.post_get_user_by_id28299(context=context)

# 方式2：在测试用例中传递参数
def test_get_user_by_id(self, api_client):
    context = {"userId": 123}
    response = api_client.post_get_user_by_id28299(context=context)
    assert response is not None
```

### 3. API 模块自动生成

#### 生成命令

```bash
cd /path/to/Interface_Test
python3 tools/createcasefile.py
```

#### 生成的文件格式

**API模块（department_yml.py）:**

```python
# -*- coding:utf-8 -*-
"""
账号相关 模块API
自动生成于 2026-03-08 16:14:59
"""
from public.base import BaseAPI
from public.login import Login


class 账号相关API(BaseAPI):
    """账号相关 接口"""
    
    def __init__(self, base_url=None, token=None, sso_ip=None, url_ip=None):
        """
        初始化
        :param base_url: 基础URL
        :param token: 认证token
        :param sso_ip: SSO服务器IP
        :param url_ip: API服务器IP
        """
        super().__init__(base_url, token)
        self.login = Login(sso_ip, url_ip) if sso_ip and url_ip else None
    
    def post_login28294(self):
        """登录接口"""
        self.json_data = self.request('login28294_test.yaml')
        print(self.verbose(self.json_data))
        return self.json_data
    
    def post_get_user_by_id28299(self, context=None):
        """
        根据ID获取用户信息
        
        :param context: 要替换的参数，格式: {"userId": 123}
        :return: 响应数据
        """
        self.json_data = self.request('get_user_by_id28299_test.yaml', context=context)
        print(self.verbose(self.json_data))
        return self.json_data
```

#### 特点

1. **继承关系**：
   - `账号相关API` 继承 `BaseAPI`
   - 拥有 `Login` 实例用于登录获取 token

2. **方法命名**：
   - 格式：`{method}_{interface_name}`
   - 例如：`post_login28294`、`get_user_by_id28299`

3. **参数处理**：
   - 自动检测 YAML 中是否有占位符
   - 有占位符的方法自动添加 `context` 参数

### 4. 测试用例自动生成

#### 测试文件格式

```python
# -*- coding:utf-8 -*-
"""
账号相关 测试用例
自动生成于 2026-03-08 16:14:59
YAML文件: get_user_by_id28299_test.yaml
"""

import pytest
import allure
from apimap.轻量化肺功能.账号相关.账号相关_yml import 账号相关API


@allure.feature("账号相关")
class Test账号相关:
    """账号相关 接口测试"""
    
    @pytest.fixture(scope="class")
    def api_client(self):
        """API客户端"""
        return 账号相关API()
    
    @allure.story("根据ID获取用户信息 /pf-lite/api/account/getUserById")
    def test_test_get_user_by_id(self, api_client):
        """
        根据ID获取用户信息
        """
        # 调用API方法，传递参数
        context = {"userId": 123}  # 根据实际情况修改参数
        if hasattr(api_client, 'post_get_user_by_id28299'):
            response = getattr(api_client, 'post_get_user_by_id28299')(context=context)
            assert response is not None, "响应为空"
```

## 使用流程

### 1. 编写YAML文件

在 `update` 文件夹下创建YAML文件：

```bash
mkdir -p update/轻量化肺功能/账号相关
touch update/轻量化肺功能/账号相关/get_user_by_id28299_test.yaml
```

### 2. 编辑YAML内容

```yaml
testinfo:
  case_suite: get_user_by_id28299_test
  descrpiton: 根据ID获取用户信息
  module_class: Test28299
test_case:
- test_name: test_get_user_by_id
  info: 根据ID获取用户信息
  method: POST
  url: /pf-lite/api/account/getUserById
  headers:
    Authorization: $token
    Content-Type: application/json
  timeout: 8
  json:
    userId: '{{userId}}'  # 占位符
```

### 3. 运行生成工具

```bash
python3 tools/createcasefile.py
```

### 4. 运行测试

```bash
# 运行所有测试
pytest testosmcase/ -v

# 运行特定测试文件
pytest testosmcase/轻量化肺功能/账号相关/get_user_by_id28299_test.py -v

# 生成allure报告
pytest testosmcase/ --alluredir=./report
allure serve report
```

## 高级用法

### 1. 自定义BaseURL

```python
from apimap.轻量化肺功能.账号相关.账号相关_yml import 账号相关API

api = 账号相关API(
    base_url="http://your-api-server.com",
    token="your_token_here"
)
result = api.post_login28294()
```

### 2. 使用Login获取Token

```python
api = 账号相关API(sso_ip="sso.example.com", url_ip="api.example.com")

# 使用login实例登录
if api.login:
    token = api.login.login("username", "password")
    api.token = token

# 发送请求
result = api.post_login28294()
```

### 3. 参数化测试

```python
import pytest

@pytest.mark.parametrize("user_id, username", [
    (1, "admin"),
    (2, "user1"),
    (3, "user2"),
])
def test_get_user_by_id_parametrize(self, api_client, user_id, username):
    """参数化测试"""
    context = {"userId": user_id}
    response = api_client.post_get_user_by_id28299(context=context)
    assert response["data"]["username"] == username
```

## 注意事项

1. **YAML文件位置**：必须放在 `update` 文件夹下
2. **占位符格式**：使用 `{{key}}` 格式，注意是双层大括号
3. **参数命名**：API方法名会自动提取YAML文件名的关键部分
4. **文件编码**：所有YAML文件使用 UTF-8 编码
5. **Token替换**：`$token` 会自动替换为实际的 token 值

## 常见问题

### Q1: 如何添加新的YAML文件？

A: 直接在 `update` 文件夹下创建YAML文件，然后运行 `python3 tools/createcasefile.py`

### Q2: 如何修改已有的API方法？

A: 修改对应的YAML文件，然后重新运行生成工具

### Q3: 如何处理文件上传？

A: 在YAML文件中使用 `files` 字段，支持eval表达式

### Q4: 参数替换不生效？

A: 检查占位符格式是否正确，应该是 `{{key}}` 而不是 `{key}`

## 更新日志

### 2026-03-08

- 重构 `createcasefile.py`，生成 `department_yml.py` 格式
- 新增 `BaseAPI` 基础类
- 支持参数替换（`{{key}}`格式）
- 继承 `Login` 类支持自动登录
- 生成 `test_department_yml.py` 格式的测试文件
