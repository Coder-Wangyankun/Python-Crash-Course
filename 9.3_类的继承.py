# 练习
# 9-6
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


class IceCreamStand(Restaurant):
    """继承Restaurant"""
    def __init__(self, restaurant_name, cuisine_type, flavors=[]):
        """初始化父类的属性，再初始化子类的属性"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def show_flavor(self):
        """打印flavors列表"""
        for flavor in self.flavors:
            print('\n' + flavor)


ice_cream = IceCreamStand('Sam', 'Moxico', ['ice', 'orange'])
ice_cream.show_flavor()

# 9-7


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


class Admin(User):
    """继承User"""
    def __init__(self, first_name, last_name, age):
        """初始化父类的属性，再初始化子类的属性"""
        super().__init__(first_name, last_name, age)
        """管理员的权限"""
        # self.privileges = ["can and post", "can delete post", "can ban user"]
        self.privilege = Privileges()

    # def show_privileges(self):
    #     """显示管理员的权限"""
    #     for privilege in self.privileges:
    #         print("\n" + privilege)


# admin = Admin('Brad', 'Pitt', 50)
# admin.show_privileges()

# 9-8


class Privileges:
    def __init__(self):
        self.privileges = ["can and post", "can delete post", "can ban user"]

    def show_privileges(self):
        """显示管理员的权限"""
        for privilege in self.privileges:
            print("\n" + privilege)


admin1 = Admin('Matt', 'Damon', 50)
admin1.privilege.show_privileges()

# 9-9


class Car:
    """一次模拟汽车的简单尝试"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()


class Battery:
    """一次模拟电动汽车点评的简单尝试"""
    def __init__(self, battery_size=70):
        """初始化电瓶的属性"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的信息"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """打印一条信息，指出电瓶的续航里程"""
        if self.battery_size == 70:
            battery_range = 240
        elif self.battery_size == 85:
            battery_range = 270

        message = "\nThis car can go approximately " + str(battery_range)
        message += " miles on a full charge."
        print(message)

    def upgrade_battery(self):
        """如果电瓶容量不是85，将其设置成85"""
        if self.battery_size != 85:
            self.battery_size = 85


class ElectricCar(Car):
    """电动车的独特之处"""
    def __init__(self, make, model, year):
        """初始化父类的属性，再初始化电动汽车特有的属性"""
        super().__init__(make, model, year)
        self.battery = Battery()


my_tesla = ElectricCar('tesla', 'model s', 2016)
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()





