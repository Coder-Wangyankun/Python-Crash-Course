# 练习
# 5-8 5-9
user_list = ['admin', 'jack', 'lucy', 'mack', 'nancy']
if user_list:
    for user in user_list:
        if user == 'admin':
            print("Hello admin,would you like to see a status report?")
        else:
            print("Hello " + user + ",thant you for logging in again.")
else:
    print("We need to find some users!")

# 5-10
current_users = ['jack', 'lucy', 'mack', 'john', 'william']
new_users = ['jeff', 'chris', 'ford', 'JOHN', 'william']
for user in new_users:
    if user.lower() in current_users:
        print("You need to enter a different user name!")
    else:
        print("This user name is not used.")

# 5-11
number_list = list(range(1, 10))
print(number_list)
for number in number_list:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(str(number) + "th")
