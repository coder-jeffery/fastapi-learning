class closurelearn:
    '''

    python闭包：一种特殊的嵌套函数 内层函数把外层函数的参数打包带走
        1.存在外层函数 嵌套一个内层函数
        2.内存函数引用一个外层函数的局部变量
        3.外层函数返回内层函数本身
    特性：
        a.保存变量状态，持久话存储
        b.变量互相隔离，互不干扰

        nonlocal 闭包修改外层变量专用
        global 全局变量
    使用场景：
        保持上下文状态
        实现函数工厂
        python装饰器的底层闭包
    作用：
        计数器、函数工程， 装饰器
    '''
    def __init__(self):
        pass

    def outter_function(self, x):
        def inner_function(y):
            return x + y
        return inner_function


    # def outter_function(self, x):
    #     def inner_function(y):
    #         return x + y
    #     return inner_function
    #

instance = closurelearn()
print(instance)

func = instance.outter_function(10)
print(func(5))



