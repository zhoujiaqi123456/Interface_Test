# -*- coding:utf-8 -*-
"""
接口自动化框架运行脚本
"""
import sys
import os

# 添加项目路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from tools.getyapi import GetYapi
from tools.createcasefile import CreateCaseFile
from config.yapi_config import YapiConfig


def fetch_yapi():
    """从YAPI获取接口数据并生成YAML文件"""
    print("=" * 60)
    print("📥 步骤1: 从YAPI获取接口数据并生成YAML文件")
    print("=" * 60)
    
    yapi = GetYapi(
        project_id=YapiConfig.PROJECT_ID,
        base_url=YapiConfig.BASE_URL,
        cookie=YapiConfig.COOKIE,
        headers=YapiConfig.HEADERS
    )
    yapi.create_yaml_by_yapi()


def generate_code():
    """根据YAML文件生成API和测试代码"""
    print("\n" + "=" * 60)
    print("🔧 步骤2: 根据YAML生成API和测试代码")
    print("=" * 60)
    
    creator = CreateCaseFile(
        yaml_path=YapiConfig.YAML_DIR,
        api_path=YapiConfig.API_DIR,
        test_path=YapiConfig.TEST_DIR
    )
    creator.create_all()


def run_tests():
    """运行测试"""
    print("\n" + "=" * 60)
    print("🧪 步骤3: 运行测试")
    print("=" * 60)
    
    import pytest
    exit_code = pytest.main([
        "-v",
        "-s",
        "--tb=short",
        "--alluredir=./report"
    ])
    
    return exit_code


def main():
    """主函数"""
    print("🚀 接口自动化框架")
    print("=" * 60)
    
    # 检查参数
    if len(sys.argv) > 1:
        action = sys.argv[1]
    else:
        print("请选择操作:")
        print("  1. fetch    - 从YAPI获取接口数据")
        print("  2. generate - 生成API和测试代码")
        print("  3. test     - 运行测试")
        print("  4. all      - 执行所有步骤")
        print()
        action = input("请输入选项 (1/2/3/4): ").strip()
    
    try:
        if action == "1" or action == "fetch":
            fetch_yapi()
        elif action == "2" or action == "generate":
            generate_code()
        elif action == "3" or action == "test":
            run_tests()
        elif action == "4" or action == "all":
            fetch_yapi()
            generate_code()
            run_tests()
        else:
            print(f"❌ 未知操作: {action}")
            sys.exit(1)
        
        print("\n✅ 完成！")
    
    except KeyboardInterrupt:
        print("\n\n⚠️  用户中断")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ 错误: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
