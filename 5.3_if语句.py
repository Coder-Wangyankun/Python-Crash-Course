# 练习
# 5-3
alien_color = 'green'
if alien_color == 'green':
    print("You get 5 points.")

# 5-4
if alien_color == 'green':
    print("You get 5 points")
else:
    print("You get 10 points")

if alien_color != 'green':
    print("You get 10 points")
else:
    print("You get 5 points")

# 5-5
if alien_color == 'green':
    print("You get 5 points")
elif alien_color == 'yellow':
    print("You get 10 point")
elif alien_color == 'red':
    print("You get 15 points")

# 5-6
age = 25
if age < 2:
    print("He is a baby")
elif age < 4:
    print("He is learning walk")
elif age < 13:
    print("He is a child")
elif age < 20:
    print("He is teenager")
elif age < 65:
    print("He is adult")
elif age >= 65:
    print("He is old people")

# 5-7
favorite_fruits = ['orange', 'apple', 'bananas']
if 'watermelon' in favorite_fruits:
    print("You really like watermelon!")
if 'strawberry' in favorite_fruits:
    print("You really like strawberry!")
if 'orange' in favorite_fruits:
    print("You really like orange!")
if 'apple' in favorite_fruits:
    print("You really like apple!")
if 'bananas' in favorite_fruits:
    print("You really like bananas!")
