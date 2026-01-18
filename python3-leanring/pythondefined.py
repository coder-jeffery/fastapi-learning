class pythondefined:

    def sayHi(self) -> str | None:
        # print("Hi!")
        return "Hello World!"


    def sayTuple(self) -> tuple | None:
        return (1, 2, 3)


    def testParams(self, num1, num2) -> dict[int] | None:
        return  num2, num1

    def introduce(self, name, age, city='成都'):
        return f'我叫{name}, 今年{age}, 家住在{city}'

    #收集位置参数
    def sum_all(self, *args):
        total = 0
        for arg in args:
            total += arg
        return total

    def show_info(self, **kwargs) -> str | None:
        # print(kwargs)
        for key, vlaue in kwargs.items():
            print(f'{key}: {vlaue}')

    print(f'*******************分割线*****************************')

    # def outer(self):
    #     print("我是外层函数")
    #     def inner():  # 内层函数，嵌套在outer里
    #         print("我是内层函数")
    #     inner()  # 外层函数内部调用内层函数
    # outer()  # 调用外层函数，会触发内层函数执行

    print(f'*******************分割线*****************************')

    def add(self, a, b):
        """
        功能：计算两个数字的和
        参数：a-第一个数字，b-第二个数字
        返回值：两个数字的和
        """
        return a + b

    # 查看函数注释



tools = pythondefined()
# print(tools.add.__doc__)
# help(tools.add)
print(tools.sayHi())
print(tools.sayTuple(), type(tools.sayTuple()))
print(tools.testParams(2,3))
print(tools.introduce('xiaoming', 20))
print(tools.introduce('xiaohong', 22, 'jiangsu'))
print(tools.sum_all(1,2,10000))
print(f'*******************分割线*****************************')
print(tools.show_info(name='Tim', age=28, address ='Shanghai', sex = 'male' ))
print(f'*******************分割线*****************************')
print(tools.show_info(name="testing", age=999))
