
from api.wework import WeWork
from common.base_classes import BaseClasses


class DepartmentYml(BaseClasses,Login):
    def list(self, id):
        self.json_data = self.request("api.yml", { "id": id})
        print(self.verbose(self.json_data))
        return self.json_data
