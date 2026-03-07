# -*- coding:utf-8 -*-
"""
快速开始示例
"""
import sys
import os

# 添加项目路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from tools.getyapi import GetYapi
from tools.createcasefile import CreateCaseFile


def example_1_fetch_yapi():
    """示例1: 从YAPI获取接口数据"""
    print("=" * 60)
    print("示例1: 从YAPI获取接口数据")
    print("=" * 60)
    
    # 配置YAPI信息
    yapi = GetYapi(
        project_id=309,
        base_url="http://yapi.u-breath.cn:9009",
        cookie="_yapi_token=xxx; _yapi_uid=xxx"  # 替换为你的cookie
    )
    
    # 获取接口数据并生成YAML
    yapi.create_yaml_by_yapi()


def example_2_generate_code():
    """示例2: 生成API和测试代码"""
    print("\n" + "=" * 60)
    print("示例2: 生成API和测试代码")
    print("=" * 60)
    
    # 创建代码生成器
    creator = CreateCaseFile()
    
    # 生成所有文件
    creator.create_all()


def example_3_custom_test_data():
    """示例3: 自定义测试数据"""
    print("\n" + "=" * 60)
    print("示例3: 在test_api.py中添加自定义测试数据")
    print("=" * 60)
    
    example_code = '''
# 在test_api.py中添加测试数据
test_data = [
    {"json": {"username": "user1", "password": "123456"}},  # 正常用户
    {"json": {"username": "admin", "password": "123456"}},    # 管理员
    {"json": {"username": "", "password": "123456"}},          # 空用户名
    {"json": {"username": "test", "password": ""}},           # 空密码
]

@pytest.mark.parametrize("kwargs", test_data)
def test_add_user(self, api_client, kwargs):
    """添加用户测试 - 参数化"""
    response = api_client._request(**kwargs)
    assert response.status_code == 200
'''
    
    print("示例代码:")
    print(example_code)


def example_4_run_tests():
    """示例4: 运行测试"""
    print("\n" + "=" * 60)
    print("示例4: 运行测试")
    print("=" * 60)
    
    print("运行所有测试:")
    print("  pytest -v -s")
    print()
    print("运行指定模块:")
    print("  pytest testosmcase/test_模块名/ -v")
    print()
    print("运行指定测试文件:")
    print("  pytest testosmcase/test_模块名/test_接口名.py -v")
    print()
    print("运行冒烟测试:")
    print("  pytest -m smoke -v")
    print()
    print("生成Allure报告:")
    print("  pytest --alluredir=./report")
    print("  allure serve report")


def main():
    """主函数"""
    print("🚀 接口自动化框架 - 快速开始示例")
    print("=" * 60)
    
    print("\n请选择示例:")
    print("  1. 从YAPI获取接口数据")
    print("  2. 生成API和测试代码")
    print("  3. 查看自定义测试数据示例")
    print("  4. 查看运行测试示例")
    print("  5. 运行所有步骤")
    print()
    
    choice = input("请输入选项 (1/2/3/4/5): ").strip()
    
    if choice == "1":
        example_1_fetch_yapi()
    elif choice == "2":
        example_2_generate_code()
    elif choice == "3":
        example_3_custom_test_data()
    elif choice == "4":
        example_4_run_tests()
    elif choice == "5":
        example_1_fetch_yapi()
        example_2_generate_code()
        print("\n✅ 示例执行完成！")
        print("\n下一步:")
        print("  1. 查看生成的YAML文件: ./testdata/")
        print("  2. 查看生成的API文件: ./apimap/")
        print("  3. 查看生成的测试文件: ./testosmcase/")
        print("  4. 修改YAML中的测试参数")
        print("  5. 运行测试: pytest -v")
    else:
        print("❌ 无效选项")


if __name__ == '__main__':
    main()
