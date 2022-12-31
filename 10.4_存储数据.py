# 练习
# 10-11 喜欢的数字：
import json

# favorite_number = input('Input your favorite number: ')
# with open('favorite_10_4.json', 'w') as f_obj:
#     json.dump(favorite_number, f_obj)
#
# with open('favorite_10_4.json') as f_obj:
#     number = json.load(f_obj)
#     print("'I know your favorite number! It's " + str(number) + ".")

# 10-12 记住喜欢的数字：
# filename = 'favorite_10_4.json'
# try:
#     with open(filename) as f_obj:
#         favorite_number = json.load(f_obj)
# except FileNotFoundError:
#     favorite_number = input('Input your favorite number: ')
#     with open('favorite_10_4.json', 'w') as f_obj:
#         json.dump(favorite_number, f_obj)
# else:
#     print("'I know your favorite number! It's " + str(favorite_number) + ".")

# 10-13 验证用户：


def get_stored_username():
    """如果存储了用户名，就获取它"""
    filename = 'username_10_4.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """提示用户输入用户名"""
    username = input("What is your name?")
    filename = 'username_10_4.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username


def greet_user():
    """问候用户，并指出其名字"""
    username = get_stored_username()
    if username:
        is_username = input("Is username right?")
        if is_username == 'yes':
            print("Welcome back, " + username + "!")
        else:
            get_new_username()
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")


greet_user()
