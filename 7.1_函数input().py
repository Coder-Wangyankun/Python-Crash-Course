# 练习
# 7-1
car_message = input("What kind of car do you want to rend?")
print("Let me see if I can find you a " + car_message + ".")

# 7-2
dinner_numbers = input("How many people have dinner?")
dinner_numbers = int(dinner_numbers)
if dinner_numbers > 8:
    print("No table available.")
else:
    print("A table is available.")

# 7-3
num = input("Enter a number, and I'll tell you if it is integer multiple of 10.")
num = int(num)
if num % 10 == 0:
    print("It is integer multiple of 10.")
else:
    print("It is not integer multiple of 10.")
