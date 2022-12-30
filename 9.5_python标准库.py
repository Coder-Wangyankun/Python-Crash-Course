# 练习
from collections import OrderedDict
from random import randint

# 9-13 使用OrderedDict：

vocabulary = OrderedDict()
vocabulary['application'] = '应用程式 应用、应用程序'
vocabulary['bit field'] = '位元栏 位域'
vocabulary['border'] = '边框、框线 边框'
vocabulary['build-in'] = '内建 内置'
vocabulary['chain'] = '串链'
vocabulary['abstract base class'] = '抽象基类'
vocabulary['class'] = '类'
vocabulary['garbage collection'] = '垃圾回收'
vocabulary['import path'] = '导入路径'
vocabulary['named tuple'] = '具名元组'

for key, value in vocabulary.items():
    print('\n' + key.title() + ': ' + value)

# 9-14 骰子：


class Die:
    """创建一个骰子"""
    def __init__(self, frequencies, sides=6):
        """
        frequency代表投掷次数
        sides代表骰子的每一面
        """
        self.frequencies = frequencies
        self.sides = sides

    def roll_die(self):
        """打印位于1和骰子面数之间的随机数"""
        random_number_str = ''
        for frequency in range(0, self.frequencies):
            random_number_str += (' ' + str(randint(1, self.sides)))
        print(random_number_str)


# 创建一个6面骰子，投掷10次
six_sides_dice = Die(10)
six_sides_dice.roll_die()

# 创建一个10面骰子，投掷10次
six_sides_dice = Die(10, 10)
six_sides_dice.roll_die()

# 创建一个20面骰子，投掷10次
six_sides_dice = Die(10, 20)
six_sides_dice.roll_die()
