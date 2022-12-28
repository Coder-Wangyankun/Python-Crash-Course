# 此文件供8.6_将函数存储在模块中使用


def make_sandwich(*toppings):
    """对顾客点的三明治进行概述"""
    print("\nMaking a sandwich with the following toppings: ")
    for topping in toppings:
        print("- " + topping)
