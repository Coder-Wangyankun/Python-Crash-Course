# 此文件供 9.4_导入类 使用
from user_9_4 import User


class Admin(User):
    """继承User"""
    def __init__(self, first_name, last_name, age):
        """初始化父类的属性，再初始化子类的属性"""
        super().__init__(first_name, last_name, age)
        """管理员的权限"""
        # self.privileges = ["can and post", "can delete post", "can ban user"]
        self.privilege = Privileges()

# 9-8


class Privileges:
    def __init__(self):
        self.privileges = ["can and post", "can delete post", "can ban user"]

    def show_privileges(self):
        """显示管理员的权限"""
        for privilege in self.privileges:
            print("\n" + privilege)