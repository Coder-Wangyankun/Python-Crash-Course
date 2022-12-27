# responses = {}
# # 设置一个标志，指出调查是否继续
# polling_active = True
# while polling_active:
#     # 提示输入被调查者的名字和回答
#     name = input("\nWhat is your name? ")
#     response = input("Which mountain would you like to climb someday? ")
#
#     # 将答卷存储在字典中
#     responses[name] = response
#
#     # 看是否还有人要参与调查
#     repeat = input("Would you like to let another person respond? (yes/no) ")
#     if repeat == 'no':
#         polling_active = False
#
# # 调查结束，显示结果
# print("\n--- Roll Results ---")
# for name, response in responses.items():
#     print(name + " would like to climb " + response + ".")


# 练习
# # 7-8
# sandwich_orders = ['tuna sandwich', 'cheese sandwich', 'tomato sandwich']
# finished_sandwiches = []
# while sandwich_orders:
#     current_sandwich = sandwich_orders.pop()
#     print("I made your " + current_sandwich + ".")
#     finished_sandwiches.append(current_sandwich)
# print("\nAll sandwiched are finished:")
# for sandwich in finished_sandwiches:
#     print("\t" + sandwich)

# 7-9
# sandwich_orders = ['tuna sandwich', 'pastrami', 'cheese sandwich', 'pastrami', 'tomato sandwich', 'pastrami']
# finished_sandwiches = []
# print("The deli is out of pastrami")
# while 'pastrami' in sandwich_orders:
#     sandwich_orders.remove('pastrami')
# while sandwich_orders:
#     current_sandwich = sandwich_orders.pop()
#     print("I made your " + current_sandwich + ".")
#     finished_sandwiches.append(current_sandwich)
# print("\nAll sandwiched are finished:")
# for sandwich in finished_sandwiches:
#     print("\t" + sandwich)

# 7-10
holiday_resorts = {}
holiday_active = True
while holiday_active:
    name = input("\nWhat is your name? ")
    resort = input("If you could visit one place in the world, where would you go? ")

    holiday_resorts[name] = resort

    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        holiday_active = False

print("\n--- Roll Results ---")
for name, resort in holiday_resorts.items():
    print(name.title() + " wants to visit " + resort + ".")
