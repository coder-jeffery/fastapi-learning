class lamdbalearn:

    def hello(self):
        hello = lambda:  "Hello, world!"
        return hello()

    def testAdd(self,x,y):
        value = lambda x,y : x+y
        return value(x,y)


lambdaTools = lamdbalearn()
print(lambdaTools.testAdd(1,2))
print(lambdaTools.hello())

func = lambda x, y=10: x + y
print(func(1))

# 直接调用，计算两数乘积，执行一次就销毁
print((lambda x,y: x*y)(3,4))  # 输出：12
# 直接调用，计算列表元素求和
print((lambda lst: sum(lst))([1,2,3,4])) # 输出：10


print(f'************************************************')
print(f'************************************************')
# 需求：将列表 [1,2,3,4] 的每个元素求平方，得到新列表
lst = [1,2,3,4]

# 方式1：普通函数+map（代码冗余）
def square(x):
    return x*x
res1 = list(map(square, lst))
print(res1)  # [1,4,9,16]

# 方式2：lambda+map（极简推荐，一行搞定）
res2 = list(map(lambda x: x*x, lst))
print(res2)  # [1,4,9,16]

# 进阶：多参数的map+lambda → 两个列表对应元素相加
lst1 = [1,2,3]
lst2 = [4,5,6]
res3 = list(map(lambda x,y: x+y, lst1, lst2))
print(res3)  # [5,7,9]