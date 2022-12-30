# 此文件供 9.4_导入类 使用
class Restaurant:
    """模拟餐厅的一些信息"""
    def __init__(self, restaurant_name, cuisine_type):
        """初始化属性restaurant_name和cuisine_type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """输出餐厅信息"""
        print("\nName of restaurant is " + self.restaurant_name + ".")
        print("Cuisine type is " + self.cuisine_type + ".")

    def open_restaurant(self):
        """指出餐厅正在营业"""
        print("\nThe restaurant named " + self.restaurant_name + " is open.")