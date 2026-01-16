# main.py
# from core import  class_a, CustomError , deduct_balance, testcase01, testcase02

#
# import os
# correct_path = "/Users/jeffery/Documents/workspace/python/sufellmv1/poc/python-learning/核心语法"
# # 先检查路径是否存在
# if os.path.exists(correct_path):
#     os.chdir(correct_path)  # 切换工作目录
# else:
#     print(f"错误：目录不存在 → {correct_path}")

# 写法1：导入整个模块，通过「模块名.类名」调用（推荐，避免命名冲突）
import core.class_a
# 创建ClassA实例
obj_a = core.class_a.ClassA("张三")
obj_a.say_hello()  # 输出：Hello, 张三! 我是ClassA的实例

# 写法2：直接导入类（简洁，适合常用类）
from core.class_a import ClassA
obj_a2 = ClassA("李四")
obj_a2.say_hello()  # 输出：Hello, 李四! 我是ClassA的实例

# 写法3：导入类并起别名（避免类名冲突）
from core.class_a import ClassA as A
obj_a3 = A("王五")
obj_a3.say_hello()  # 输出：Hello, 王五! 我是ClassA的实例


# print(111)