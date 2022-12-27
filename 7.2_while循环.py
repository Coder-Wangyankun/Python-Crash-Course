prompt = "\nTell me something, and I will repeat it back to you"
prompt += "\nEnter 'quit' to end the program."

# message = ""
# while message != 'quit':
#     message = input(prompt)
#     if message != 'quit':
#         print(message)

# 优化：使用flag
# active = True
# while active:
#     message = input(prompt)
#     if message == 'quit':
#         active = False
#         break
#     else:
#         print(message)

# continue
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

# 练习
# 7-4
pizza_message = "\nEnter some pizza ingredients."
pizza_active = True
while pizza_active:
    ingredient = input(pizza_message)
    if ingredient == 'quit':
        pizza_active = False
        break
    print("We will add " + ingredient + " to the pizza.")

# 7-5
age_message = "\nHow old are you?"
age_active = True
while age_active:
    age = input(age_message)
    if age == 'quit' or int(age) <= 0:
        age_active = False
        break
    if int(age) < 3:
        print("free")
    elif int(age) <= 12:
        print("$10")
    else:
        print("$15")

# 7-6 略
# 7-7 略
