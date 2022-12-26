# 1.转换大小写
name = "ada lovelace"
print(name.title())  # 首字母大写
print(name.upper())  # 转换成大写
print(name.lower())  # 转换成小写

# 2.字符串拼接
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)
print("Hello, " + full_name.title() + "!")
message = "Hello, " + full_name.title() + "!"
print(message)

# 3.制表符\t、换行符\n
print("\tPython")
print("    Python")
print("Languages:\n\tPython\n\tC\n\tJavaScript")

# 4.删除空白
favorite_language = " python "
print(favorite_language.rstrip())  # rstrip删除末尾空白 right
print(favorite_language.lstrip())  # lstrip删除开头空白 left
print(favorite_language.strip())  # strip删除两头空白

# 练习
# 2-3
my_name = "Nelson"
print("Hello " + my_name + ",would you like to learn Python today?")
# 2-4
print(my_name.upper())
print(my_name.lower())
print(my_name.title())
# 2-5 2-6
famous_person = "Albert Einstein"
famous_message = "A person who never made a mistake never tried anything new."
print(famous_person + "once said," + famous_message)
# 2-7
rich_man = "\tBill Gates"
print(rich_man)
print(rich_man.lstrip())
print(rich_man.rstrip() + '\n')
print(rich_man.strip())
