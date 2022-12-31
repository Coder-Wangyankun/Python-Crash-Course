# 练习
# 10-3 访客：
# 提示用户输入名字，写入到文件guest_10_2.txt中
user_name = input('Please enter your name: ')
user_name_filename = 'guest_10_2.txt'

with open(user_name_filename, 'w') as file_object:
    file_object.write(str(user_name))

# 10-4 访客名单：
# 提示用户输入名字，打印一句问候语，并写入到guest_book_10_2中

with open('guest_book_10_2', 'a') as file_object:
    while True:
        user_name = input('Please enter your name: ')
        print("Hello," + user_name + ".\n")
        if user_name == 'q':
            break
        file_object.write("Hello," + user_name + ".\n")

# 10-5 关于编程的调查：
# 询问用户为什么喜欢编程，写入到reasons_10_2中
with open('reasons_10_2', 'a') as file_object:
    while True:
        reason = input('Why do you like programming: ')
        if reason == 'q':
            break
        file_object.write(reason + "\n")











