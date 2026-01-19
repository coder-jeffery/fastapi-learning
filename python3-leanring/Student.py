class Student:
    """学生类：包含姓名、年龄、成绩三个属性"""
    # 1. 初始化属性：必写
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    # 2. 友好字符串输出：必写
    def __str__(self):
        return f"学生：{self.name}，年龄：{self.age}，成绩：{self.score}"

    # 3. 官方调试字符串输出：必写
    def __repr__(self):
        return f"Student(name='{self.name}', age={self.age}, score={self.score})"

# 创建对象
stu1 = Student("小明", 15, 98)
stu2 = Student("小红", 14, 95)

# 测试：触发__str__
print(stu1)  # 学生：小明，年龄：15，成绩：98
print(stu2)  # 学生：小红，年龄：14，成绩：95

# 测试：触发__repr__
print(repr(stu1)) # Student(name='小明', age=15, score=98)

# 访问对象属性
print(stu1.name, stu1.score) # 小明 98