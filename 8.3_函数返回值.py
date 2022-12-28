def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + last_name
    return full_name.title()


while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")

# 练习
# 8-6


# def city_country(city, country):
#     string = "\n" + city + ", " + country
#     return string
#
#
# print(city_country('Hangzhou', 'China'))
# print(city_country('Reykjavik', 'Iceland'))
# print(city_country('Santiago', 'Chile'))

# 8-7


# def make_album(singer, album, songs_numbers=''):
#     album_message = {'singer': singer, 'album': album}
#     if songs_numbers:
#         album_message['songs_numbers'] = songs_numbers
#     return album_message
#
#
# print(make_album('Adele', '30', 12))
# print(make_album('Taylor Swift', 'Anti-Hero', 1))

# 8-8


def make_album(singer, album, songs_numbers=''):
    album_message = {'singer': singer, 'album': album}
    if songs_numbers:
        album_message['songs_numbers'] = songs_numbers
    return album_message


while True:
    album_input = input("\nPlease tell me a album: ")
    if album_input == 'q':
        break

    singer_input = input("Please tell me the singer: ")
    if singer_input == 'q':
        break

    print(make_album(singer_input, album_input))
