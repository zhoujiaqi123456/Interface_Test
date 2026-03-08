from api.department_yml import DepartmentYml
from common.data_base import DataBase
import pytest
import allure

class TestDepartmentYml:
    # 先实例化对象
    department_yml = DepartmentYml()

    @allure.story("部门列表查询")
    @allure.title("查询")
    @allure.description("接口部门列表")
    @pytest.mark.smoking
    @pytest.mark.osm
    @pytest.mark.XIONGTING
    @pytest.mark.parametrize("testdata", [data])

    def test_list_yml(self):
        r = self.department_yml.list("1")
        #断言
        assert r["errcode"] == 0
        assert r["department"][0]["name"] == "墨迹测试"
