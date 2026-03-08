# createcasefile.py 使用说明

## 功能说明

`createcasefile.py` 是一个自动化生成工具，用于根据 `update` 文件夹下的 YAML 文件生成 API 模块和测试用例文件。

## 主要功能

1. **扫描 update 文件夹**：遍历 `update` 文件夹的所有子目录和 YAML 文件
2. **生成 API 模块**：在 `apimap` 文件夹下创建相同的层级结构，生成 API 模块文件
3. **生成测试用例**：在 `testosmcase` 文件夹下创建相同的层级结构，为每个 YAML 生成测试文件

## 目录结构

```
Interface_Test/
├── update/                    # YAML 文件源目录
│   └── 轻量化肺功能/
│       ├── 账号相关/
│       ├── 设备控制/
│       ├── 设置/
│       └── ...
├── apimap/                    # API 模块生成目录
│   └── 轻量化肺功能/
│       ├── 账号相关/
│       │   └── 账号相关Api.py
│       ├── 设备控制/
│       │   └── 设备控制Api.py
│       └── ...
└── testosmcase/               # 测试用例生成目录
    └── 轻量化肺功能/
        ├── 账号相关/
        │   ├── login28294_test.py
        │   └── ...
        ├── 设备控制/
        │   ├── startTest28060_test.py
        │   └── ...
        └── ...
```

## API 模块格式

生成的 API 模块文件包含以下格式的方法：

```python
def post_login28294(self):
    """
    登录
    请求方法: POST
    请求URL: /pf-lite/api/account/login
    """
    self.json_data = self.request('login28294_test.yaml')
    print(self.verbose(self.json_data))
    return self.json_data
```

## 测试用例格式

生成的测试用例文件格式：

```python
import pytest
import allure
from apimap.轻量化肺功能.账号相关.账号相关Api import 账号相关Api


@allure.feature("账号相关")
class Test账号相关:
    """账号相关 接口测试"""
    
    @pytest.fixture(scope="class")
    def api_client(self):
        """API客户端"""
        return 账号相关Api()
    
    @allure.story("登录 /pf-lite/api/account/login")
    def test_case_0(self, api_client):
        """
        登录
        请求方法: POST
        请求URL: /pf-lite/api/account/login
        """
        # 调用API方法
        if hasattr(api_client, 'post_login28294'):
            response = getattr(api_client, 'post_login28294')()
            assert response is not None, "响应为空"
        else:
            pytest.skip(f"方法 post_login28294 不存在")
```

## 使用方法

### 1. 基本使用

```bash
cd /path/to/Interface_Test
python3 tools/createcasefile.py
```

### 2. 自定义路径

```python
from tools.createcasefile import CreateCaseFile

# 创建生成器实例
creator = CreateCaseFile(
    update_path="./update",
    api_path="./apimap",
    test_path="./testosmcase"
)

# 生成所有文件
creator.create_all()
```

## 统计信息

根据当前 `update` 文件夹：

- **YAML 文件总数**: 52 个
- **API 模块目录**: 5 个
- **API 模块文件**: 5 个（每个目录一个）
- **测试文件**: 52 个（每个 YAML 一个）

## 生成的文件列表

### API 模块文件

1. `apimap/轻量化肺功能/导出/导出Api.py`
2. `apimap/轻量化肺功能/设备控制/设备控制Api.py`
3. `apimap/轻量化肺功能/账号相关/账号相关Api.py`
4. `apimap/轻量化肺功能/设置/设置Api.py`
5. `apimap/轻量化肺功能/外部申请模块 - his模块/外部申请模块His模块Api.py`

### 测试文件

每个 YAML 文件对应一个测试文件，例如：

- `testosmcase/轻量化肺功能/账号相关/login28294_test.py`
- `testosmcase/轻量化肺功能/设备控制/startTest28060_test.py`
- `testosmcase/轻量化肺功能/设置/getCommonSetting28082_test.py`
- ...

## 依赖项

- Python 3.x
- PyYAML

## 注意事项

1. 确保 `update` 文件夹下有有效的 YAML 文件
2. YAML 文件必须包含 `testinfo` 和 `test_case` 字段
3. 生成的 API 方法会根据 YAML 文件名自动生成方法名
4. 测试文件默认会跳过（使用 `@pytest.mark.skip`），需要手动移除或修改标记

## 更新日志

### 2026-03-08

- 初始版本
- 支持扫描 update 文件夹
- 支持生成 API 模块和测试用例
- 保持层级结构一致性
