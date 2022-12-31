# 练习
# 10-6 加法运算：
# number1 = input("Please enter a number: ")
# number2 = input("Please enter another number: ")
# try:
#     number_sum = int(number1) + int(number2)
# except ValueError:
#     print("Sorry,Please enter num instead of string.")
# else:
#     print(number_sum)

# 10-7 加法计算器：
# while True:
#     number1 = input("\nPlease enter a number: ")
#     number2 = input("Please enter another number: ")
#     if number1 == 'q':
#         break
#
#     if number2 == 'q':
#         break
#
#     try:
#         number_sum = int(number1) + int(number2)
#     except ValueError:
#         # 用户输错后能继续输入
#         print("Sorry,Please enter num instead of string.")
#     else:
#         print(number_sum)

# 10-8 猫和狗：
# 10-9 沉默的猫和狗：

# def read_animals(filename):
#     try:
#         with open(filename) as f_obj:
#             contents = f_obj.read()
#
#     except FileNotFoundError:
#         # 文件找不到，给出提示
#         # msg = "Sorry, the file " + filename + " dose not exist."
#         # print(msg)
#         pass
#
#     else:
#         # 输出文件的内容
#         print(contents)
#
#
# filename_cats = 'cats_10_3.txt'
# filename_dogs = 'dogs_10_3.txt'
# read_animals(filename_cats)
# read_animals(filename_dogs)

# 10-10 常见单词：


def count_the(filename_book):
    """数文件中有多少the"""
    try:
        with open(filename_book, 'r', encoding='utf-8') as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        # 文件找不到，给出提示
        msg = "Sorry, the file " + filename + " dose not exist."
        print(msg)
    else:
        count = contents.lower().count('the')
        print(count)


filenames = ['A voice from Waterloo_10_3.txt']
for filename in filenames:
    count_the(filename)
