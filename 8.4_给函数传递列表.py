def print_models(unprinted_designs, completed_models):
    """
    模拟打印每个设计，直到没有未打印的设计为止
    打印每个设计后，都将其转移到列表completed_models中
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        # 模拟根据设计制作3D打印模型的过程
        print("Printing model: " + current_design)
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """显示打印好的所有模型"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs_list = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models_list = []

print_models(unprinted_designs_list, completed_models_list)
show_completed_models(completed_models_list)

# 练习
# 8-9 8-10
magicians = ['Steven Frayne', 'Franz Harary', 'Liu qian']


def show_magicians(magicians_list):
    """打印列表中每个魔术师的名字"""
    for magician in magicians_list:
        print("\n" + magician)


def make_great(magicians_list):
    """在每个魔术师的名字前都加入字样the Great"""
    magicians_new = []
    while magicians_list:
        magician = 'the Great ' + magicians_list.pop()
        magicians_new.append(magician)
    for magician in magicians_new:
        magicians_list.append(magician)
    return magicians_list


# 使用副本方式调用make_great函数
magicians_list_copy = make_great(magicians[:])
show_magicians(magicians)
show_magicians(magicians_list_copy)
