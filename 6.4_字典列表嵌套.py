# 练习
# 6-7
person1 = {
    "first_name": "Hideo",
    "last_name": "Kojima",
    "age": 59,
    "city": "Japan"
}

person2 = {
    "first_name": "Bill",
    "last_name": "Gates",
    "age": 67,
    "city": "America"
}

person3 = {
    "first_name": "Elon",
    "last_name": "Reeve Musk",
    "age": 51,
    "city": "South Africa"
}

people = [person1, person2, person3]
for person in people:
    print(person)

# 6-8
pet1 = {
    'type': 'dog',
    'master': 'nancy'
}
pet2 = {
    'type': 'cat',
    'master': 'lucy'
}
pets = [pet1, pet2]
for pet in pets:
    print(pet)

# 6-9
favorite_places = {
    'nancy': ['nanjing'],
    'lucy': ['beijing', 'shanghai'],
    'mack': ['chengdu', 'kunming', 'lanzhou']
}
for name in favorite_places.keys():
    if len(favorite_places[name]) <= 1:
        print("\n" + name.title() + "'s favorite places is:")
    else:
        print("\n" + name.title() + "'s favorite places are:")
    for place in favorite_places[name]:
        print("\t" + place)

# 6-10
favorite_num = {
    "nancy": [9],
    "mack": [3, 4, 6],
    "lucy": [4],
    "jack": [7, 666],
    "ming": [10]
}
for name in favorite_num.keys():
    if len(favorite_num[name]) < 2:
        print("\n" + name.title() + "'s favorite num is:")
    else:
        print("\n" + name.title() + "'s favorite num are:")
    for num in favorite_num[name]:
        print("\t" + str(num))

# 6-11
cities = {
    'beijing': {'country': 'China', 'population': 1000, 'fact': 'It is the capital.'},
    'zhengzhou': {'country': 'China', 'population': 10000, 'fact': 'It is in the Central Plains.'},
    'guilin': {'country': 'China', 'population': 800, 'fact': 'It has good scenery.'},
}
for city, describe in cities.items():
    print(city.title() + " belongs to country " + describe['country'])
    print(city.title() + " has " + str(describe['population']) + " million population")
    print("About " + city.title() + "," + describe['fact'] + '\n')
