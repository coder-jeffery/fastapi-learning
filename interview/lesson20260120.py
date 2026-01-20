'''
list推导循环 和 普通循环区别：
    推导循环底层调用c语言代码，减少解释器开销，效率高， 性能高，减少内存开销，代码量大
    普通循环：python解释器执行 效率低 使用用于处理复杂逻辑

'''
class lesson20260120:

    def learnlist(self):
        test_list = []
        for i in range(1,11):
            test_list.append(i **1)
        print(f'普通循环列表 :',test_list)
        result = [i **1 for i in test_list]
        print(f'列表推导循环: ',result)


    def testcase02(self):
        test_case02 = []
        for num in range(1,5):  #普通循环
            test_case02.append(num **2)
        print(test_case02)
        res = [num **2 for num in range(1,5)] #推导式循环
        print(res)

tools = lesson20260120()
print(tools.learnlist())
print(tools.testcase02())