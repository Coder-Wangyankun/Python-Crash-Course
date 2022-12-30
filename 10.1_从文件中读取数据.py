# 练习
# 10-1
# with open('learning_python_10_1.txt') as file_object:
#     # 学习的Python知识
#     # 第一次打印，读取整个文件
#     contents = file_object.read()
#     print(contents.strip() + '\n')
#
# with open('learning_python_10_1.txt') as file_object:
#     # 学习的Python知识
#     # 第二次打印，遍历文件对象
#     for line in file_object:
#         print(line.strip() + '\n')
#
# with open('learning_python_10_1.txt') as file_object:
#     # 学习的Python知识
#     # 第三次打印，各行存储在一个列表中，在with外打印
#     lines = file_object.readlines()
#
# line_string = ''
# for line in lines:
#     line_string += line.rstrip()
#
# print(line_string)

# 10-2
with open('learning_python_10_1.txt') as file_object:
    # 学习的Python知识
    lines = file_object.readlines()
    for line in lines:
        print(line.rstrip().replace('Python', 'C'))
