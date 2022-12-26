# 练习
# 4-10
lists = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("The first three items in the list are:")
print(lists[:3])
print("Three items from the middle of the list are:")
print(lists[3:6])
print("The last three items in the list are:")
print(lists[6:])
# 4-11
pizza_list = ["meat", "onion", "orange"]
firend_pizzas = pizza_list[:]
pizza_list.append("apple")
firend_pizzas.append("watermelon")
print("My favorite pizzas are:")
for pizza in pizza_list:
    print(pizza)
print("My friend's favorite pizzas are:")
for pizza in firend_pizzas:
    print(pizza)

