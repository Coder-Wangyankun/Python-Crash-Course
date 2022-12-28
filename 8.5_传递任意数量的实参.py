# 练习
# 8-12


def make_sandwich(*toppings):
    """对顾客点的三明治进行概述"""
    print("\nMaking a sandwich with the following toppings: ")
    for topping in toppings:
        print("- " + topping)


make_sandwich('pepperoni')
make_sandwich('pepperoni', 'mushrooms')
make_sandwich('pepperoni', 'mushrooms', 'green peppers')

# 8-13


def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道油管用户的一切"""
    profile = dict()
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('albert', 'einstein', location='princeton', field='physics', age=30)
print(user_profile)

# 8-14


def make_car_info(manufacturer, model, **others):
    car_info = dict()
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    for key, value in others.items():
        car_info[key] = value
    return car_info


created_car_info = make_car_info('subaru', 'outback', color='blue', tow_package=True)
print(created_car_info)

