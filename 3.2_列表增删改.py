# 练习
# 3-4
persons = ['Uncle', 'Grandpa', 'Grandma']
print(persons[0] + "、" + persons[1] + "、" + persons[2] + ",I'd like to invite you to have dinner with me.")
# 3-5
print(persons[1] + "can't keep his appointment.")
persons[1] = "Chairman Mao"
print(persons[0] + "、" + persons[1] + "、" + persons[2] + ",I'd like to invite you to have dinner with me.")
# 3-6
print("I found a bigger table.")
persons.insert(0, "ZengShiQiang")
persons.insert(2, 'NanHuanJin')
persons.append("NiHaiXia")
print(persons[0] + "、" + persons[1] + "、" + persons[2] + "、" + persons[3] + "、" + persons[4] + "、" + persons[5] + ",I'd like to invite you to have dinner with me.")
print("Since the new table could not be delivered in time, only two guests could be invited.")
print(persons.pop() + ",I'm sorry I can't invite you to dinner.")
print(persons.pop() + ",I'm sorry I can't invite you to dinner.")
print(persons.pop() + ",I'm sorry I can't invite you to dinner.")
print(persons.pop() + ",I'm sorry I can't invite you to dinner.")
print(persons[0] + ",You're still invited.")
print(persons[1] + ",You're still invited.")
del persons[0]
del persons[0]
print(persons)
print("It's sad exercise.")