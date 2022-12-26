squares = [value**2 for value in range(1, 11)]
print(squares)
# 练习
# 4-3
for num in range(1, 21):
    print(num)
# 4-4
big_num_list = []
for num in range(1, 1000001):
    # print(num)
    big_num_list.append(num)
# 4-5
print(min(big_num_list))
print(max(big_num_list))
print(sum(big_num_list))
# 4-6
odd_num_list = []
for num in range(1,20,2):
    odd_num_list.append(num)
    print(num)
print(odd_num_list)
# 4-7
three_multiple_list = []
for num in range(3,31,3):
    three_multiple_list.append(num)
    print(num)
print(three_multiple_list)
# 4-8 4-9
cube_list = [value**3 for value in range(1,11)]
for num in cube_list:
    print(num)