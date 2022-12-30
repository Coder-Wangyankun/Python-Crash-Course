# 此文件供 9.4_导入类 使用


class User:
    """管理用户信息"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        """打印用户的年龄"""
        print("\n " + self.first_name + " " + self.last_name + "'s age is " + str(self.age) + ".")

    def greet_user(self):
        """对用户的问候"""
        print("\nHello," + self.first_name + " " + self.last_name + ".")
