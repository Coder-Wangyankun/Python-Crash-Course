# 练习
# 6-1
person = {
    "first_name": "Hideo",
    "last_name": "Kojima",
    "age": 59,
    "city": "Japan"
}
print(person["first_name"])
print(person["last_name"])
print(person["age"])
print(person["city"])

# 6-2
person_num = {
    "nancy": 9,
    "mack": 3,
    "lucy": 4,
    "jack": 7,
    "ming": 10
}
print("Nancy lover number " + str(person_num["nancy"]))
print("Mack lover number " + str(person_num["mack"]))
print("Lucy lover number " + str(person_num["lucy"]))
print("Jack lover number " + str(person_num["jack"]))
print("Ming lover number " + str(person_num["ming"]))

# 6-3 词汇表
vocabulary = {
    'application': '应用程式 应用、应用程序',
    'bit field': '位元栏 位域',
    'border': '边框、框线 边框',
    'build-in': '内建 内置',
    'chain': '串链',
    'abstract base class': '抽象基类',
    'class': '类',
    'garbage collection': '垃圾回收',
    'import path': '导入路径',
    'named tuple': '具名元组',
}

for key, value in vocabulary.items():
    print('\n' + key.title() + ': ' + value)
