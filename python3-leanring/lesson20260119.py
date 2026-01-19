# 普通循环
import time

res  = []
for i in range(5):
    res.append(i)
print(res)

# 链式推导循环
res = [i for i in range(5)]
print(res)


res2 = []
for i2 in  range(1,6):
    res2.append(i2**2)
print(res2)

#列表推导
res2 = [i**2 for i in range(1,6)]
print(res2)


class lesson20260119:

    '''
    BM25 0-∞
    向量 0-1
    如何合并两个结果集： 归一化

    推导式循环和普通循环区别
    '''
    def __init__(self):
        pass

    def showinfo(self):
        # print('testing')
        return f'testing'

tools = lesson20260119()
print(tools.showinfo())




n = 10 ** 5

# 普通for循环
start = time.time()
res = []
for i in range(n):
    res.append(i ** 2)
print(f"普通for循环(10万级)：{time.time()-start:.4f} s")

# 列表推导式
start = time.time()
res = [i ** 2 for i in range(n)]
print(f"列表推导式(10万级)：{time.time()-start:.4f} s")
