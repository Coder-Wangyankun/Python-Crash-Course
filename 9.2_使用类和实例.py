# 练习
# 9-4
class Restaurant:
    """模拟餐厅的一些信息"""
    def __init__(self, restaurant_name, cuisine_type):
        """初始化属性"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def set_number_served(self, number):
        """设置就餐人数"""
        self.number_served = number

    def increment_number_served(self, incremental_number):
        """递增就餐人数"""
        self.number_served += incremental_number

    def describe_restaurant(self):
        """输出餐厅信息"""
        print("\nName of restaurant is " + self.restaurant_name + ".")
        print("Cuisine type is " + self.cuisine_type + ".")

    def open_restaurant(self):
        """指出餐厅正在营业"""
        print("\nThe restaurant named " + self.restaurant_name + " is open.")


restaurant = Restaurant('Sam', 'Mexico')
print(str(restaurant.number_served) + " people have dined in this restaurant.")
restaurant.number_served = 10
print(str(restaurant.number_served) + " people have dined in this restaurant.")

restaurant.set_number_served(100)
print(str(restaurant.number_served) + " people have dined in this restaurant.")

restaurant.increment_number_served(200)
print(str(restaurant.number_served) + " people have dined in this restaurant.")

# 9-5


class User:
    """管理用户信息"""
    def __init__(self, first_name, last_name, age):
        """初始化属性"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 1

    def increment_login_attempts(self):
        """login_attempts++"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """reset login_attempts"""
        self.login_attempts = 0

    def describe_user(self):    
        """打印用户的年龄"""
        print("\n " + self.first_name + " " + self.last_name + "'s age is " + str(self.age) + ".")

    def greet_user(self):
        """对用户的问候"""
        print("\nHello," + self.first_name + " " + self.last_name + ".")


user = User('Brad', 'Pitt', 50)
print("\n")
print(user.login_attempts)
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(user.login_attempts)
user.reset_login_attempts()
print(user.login_attempts)

