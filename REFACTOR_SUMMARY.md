# 接口自动化框架改造总结

## 改造概述

本次改造主要针对 `tools/getyapi.py` 和 `tools/createcasefile.py` 两个核心文件，使其支持新的YAPI接口格式，并实现了完整的自动化流程。

## 改造内容

### 1. getyapi.py 改造

**改造前问题**：
- 使用旧的YAPI API格式
- 登录方式复杂
- YAML格式不规范

**改造后功能**：
- ✅ 支持新的YAPI接口地址格式
- ✅ 支持Cookie认证（无需登录）
- ✅ 自动解析接口分类和模块
- ✅ 生成规范的YAML文件
- ✅ 每个接口对应一个YAML文件
- ✅ YAML包含完整的接口信息（url, headers, params, data, json等）

**新增特性**：
```python
# 支持新的接口格式
yapi = GetYapi(
    project_id=309,
    base_url="http://yapi.u-breath.cn:9009",
    cookie="_yapi_token=xxx; _yapi_uid=xxx"
)
```

### 2. createcasefile.py 改造

**改造前问题**：
- 只生成测试文件，不生成API封装
- 不支持参数化测试
- 文件结构不清晰

**改造后功能**：
- ✅ 自动生成API模块文件（api.py）
- ✅ 自动生成测试文件（test_api.py）
- ✅ 一个模块对应一个api.py
- ✅ 一个YAML对应一个test_api.py
- ✅ 支持pytest参数化传递参数
- ✅ 支持在YAML中定义多个测试用例
- ✅ 支持在test_api.py中自定义参数

**文件结构**：
```
apimap/
└── api_模块名/
    └── 模块名.py          # API模块（包含多个接口方法）

testosmcase/
└── test_模块名/
    └── test_接口名_ID.py  # 测试文件（一个YAML对应一个）
```

## YAML文件格式

### 完整格式示例

```yaml
testinfo:
  interface_id: 28081
  title: 设置通用配置
  category: 设置模块
  description: 接口描述

request:
  url: /api/settings/setCommonSetting
  method: POST
  headers:
    Authorization: $token
    Content-Type: application/json
  params: {}
  data: ""
  json:
    key1: ""
    key2: ""
  files: ""
  timeout: 8

test_case:
  - case_name: 冒烟测试
    description: 基本功能测试
    mark: smoke
    skip: false
    extract: ""
    validate:
      status_code: 200
      contains: "success"
      json_path: "$.code"
      json_value: "0"
```

## 参数化测试

### 方式1: 修改YAML文件

在YAML中添加多个测试用例：

```yaml
test_case:
  - case_name: 冒烟测试
    mark: smoke
    # ... 其他配置

  - case_name: 边界测试
    mark: edge
    # ... 其他配置
```

### 方式2: 修改test_api.py

在生成的测试文件中，直接使用pytest参数化：

```python
# 添加测试参数
test_data = [
    {"json": {"param1": "value1"}},  # 测试1
    {"json": {"param1": "value2"}},  # 测试2
    {"json": {"param1": "value3"}},  # 测试3
]

@pytest.mark.parametrize("kwargs", test_data)
def test_something(self, api_client, kwargs):
    response = api_client._request(**kwargs)
    assert response.status_code == 200
```

## 使用流程

### 1. 配置YAPI

编辑 `config/yapi_config.py`：

```python
BASE_URL = "http://yapi.u-breath.cn:9009"
PROJECT_ID = "309"
COOKIE = "_yapi_token=xxx; _yapi_uid=xxx"
```

### 2. 获取接口数据

```bash
python run_framework.py fetch
# 或
python tools/getyapi.py
```

### 3. 生成代码

```bash
python run_framework.py generate
# 或
python tools/createcasefile.py
```

### 4. 运行测试

```bash
python run_framework.py test
# 或
pytest -v -s
```

### 5. 一键执行

```bash
python run_framework.py all
```

## 核心改进

### 1. 代码生成质量

- **API封装**：自动生成规范的API类，包含完整的文档字符串
- **测试用例**：自动生成pytest测试类，支持allure报告
- **参数化**：支持pytest.mark.parametrize，方便批量测试

### 2. 可维护性

- **模块化**：按模块组织代码，结构清晰
- **自动化**：从YAPI到测试全流程自动化
- **可扩展**：支持自定义参数和测试用例

### 3. 易用性

- **一键执行**：提供运行脚本，简化操作
- **文档完善**：提供详细的使用说明和示例
- **错误处理**：友好的错误提示和日志

## 新增文件

1. **config/yapi_config.py** - YAPI配置文件
2. **run_framework.py** - 主运行脚本
3. **README_FRAMEWORK.md** - 使用说明
4. **requirements_framework.txt** - 依赖列表

## 备份文件

原始文件已备份为：
- `tools/getyapi.py.bak`
- `tools/createcasefile.py.bak`

## 兼容性

- ✅ 新YAML格式完全兼容改造后的工具
- ⚠️ 旧YAML格式会被自动跳过，不影响新功能
- ✅ 支持Python 3.7+

## 测试结果

已测试功能：
- ✅ 从YAPI获取接口数据
- ✅ 生成规范的YAML文件
- ✅ 生成API模块文件
- ✅ 生成测试用例文件
- ✅ 支持多个测试用例
- ✅ 参数化测试功能

## 下一步建议

1. 集成CI/CD自动化
2. 添加数据驱动测试（从Excel/CSV读取）
3. 增加接口依赖处理（前置/后置条件）
4. 支持接口Mock
5. 添加性能测试

## 技术栈

- Python 3.7+
- pytest
- requests
- ruamel.yaml
- allure-pytest
- jsonpath

## 总结

本次改造成功实现了：
1. ✅ 支持新的YAPI接口格式
2. ✅ 自动生成YAML、API、测试文件
3. ✅ 支持参数化测试
4. ✅ 提供完整的使用文档和示例

框架已经可以投入使用，大幅提升了接口自动化测试的效率！
