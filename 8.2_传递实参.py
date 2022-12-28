def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


# 位置实参
describe_pet('hamster', 'harry')
# 关键字实参
describe_pet(animal_type='hamster', pet_name='harry')

# 练习
# 8-3


def make_shirt(size, caption):
    """制作T恤"""
    print("\nThe size of T-shirt is " + size + ".")
    print("The caption of T-shirt is " + caption + ".")


# 位置实参
make_shirt('large', 'fashion')
# 关键字实参
make_shirt(caption='more fashion', size='small')

# 8-4


def make_shirt_new(size, caption='I love Python'):
    """制作T恤"""
    print("\nThe size of T-shirt is " + size + ".")
    print("The caption of T-shirt is " + caption + ".")


make_shirt_new('large')
make_shirt_new('middle')
make_shirt_new('small', 'very fashion')

# 8-5


def describe_city(city, country="China"):
    print("\n" + city.title() + " is in " + country + ".")


describe_city('hangzhou')
describe_city('kunming')
describe_city('Reykjavik', 'Iceland')
