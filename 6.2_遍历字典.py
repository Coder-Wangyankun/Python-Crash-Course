# 练习
# 6-5
rivers = {
    "Nile": "Egypt",
    "The Changjiang River": "China",
    "Mississippi River": "America"
}
for river, country in rivers.items():
    print("The " + river + "runs throuth " + country + ".")
for river in rivers.keys():
    print(river)
for country in rivers.values():
    print(country)

# 6-6
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
participated = ['jen', 'edward']  # 已参与调查
for name in favorite_languages.keys():
    if name in participated:
        print(name.title() + ",Thank you for your participation!")
    else:
        print(name.title() + ",Hope you can participate in the investigation!")
