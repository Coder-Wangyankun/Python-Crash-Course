# 练习
# 9-1
# 创建类，加不加括号()都行
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


restaurant = Restaurant('Sam', 'chuancai')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

# 9-2

restaurant_america = Restaurant('Mack', 'America')
restaurant_england = Restaurant('Jack', "England")
restaurant_america.describe_restaurant()
restaurant_england.describe_restaurant()

# 9-3


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


user1 = User('Cristiano ', 'Ronaldo', 30)
user1.describe_user()
user1.greet_user()

user2 = User('Kylian', 'Mbappé', 40)
user2.describe_user()
user2.greet_user()

user3 = User('Emiliano', 'Martínez', 50)
user3.describe_user()
user3.greet_user()
