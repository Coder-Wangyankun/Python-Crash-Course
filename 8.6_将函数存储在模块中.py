# 8-15
from printing_functions_8_6 import make_sandwich

# 8-16
# 引入
import printing_functions_8_6  # 整个文件
from printing_functions_8_6 import make_sandwich  # 指定函数
from printing_functions_8_6 import make_sandwich as sandwiches  # 指定函数 && 起别名
import printing_functions_8_6 as mn  # 整个文件 && 起别名
from printing_functions_8_6 import *  # 整个文件的全部函数

# 使用
printing_functions_8_6.make_sandwich()
make_sandwich()
sandwiches()
mn.make_sandwich()
make_sandwich()


