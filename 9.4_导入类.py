# 练习
# 9-10 导入Restaurant类：

from restaurant_9_4 import Restaurant  # 9-10
from admin_9_4 import Admin  # 9-11
from admin_privileges_9_4 import Admin as mn
restaurant = Restaurant('Sam', 'Mexico')
restaurant.describe_restaurant()

# 9-11 导入Admin类：
admin = Admin('Matt', 'Damon', 50)
admin.privilege.show_privileges()

# 9-12 多个模块
admin1 = mn('Matt', 'Damon', 50)
admin1.privilege.show_privileges()
