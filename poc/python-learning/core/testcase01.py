# 变量、数据类型（int/str/list/dict/tuple/set 等）、运算符、流程控制（if-else、for/while 循环、break/continue）、异常处理（try-except-finally、自定义异常

i  = 10
print(i)

str = 'test'
print(str)

list = ['a', 'b', 'c']
print(list)

for item in list:
    if item == 'a':
       list.remove(item)
    print("删除完的元素",item)



arr  =  [1, 2, 3]
print(arr)

a = 3.14159
print(a)
print(type(a))

list2 =  [ ['a', 'b'], ['c', 'd'], ['e', 'f'] ]
print(list2)

for item in list2:
    print(item)


score = 50
if score > 0 or score < 60:
    print('不及格')
elif  score <= 70:
    print('及格....')
elif  score <= 80:
    print('良好')
elif  score <= 90:
    print('优秀')
else:
    print('优秀')


dict_01 = {'a': 1, 'b': 2, 'c': 3}
# dict_02 = {'a': 1, 'b': 2, 'c': 3}
dict_03 = {'e': 4, 'f': 5, 'd': 6}
dict = dict_01  | dict_03
print(dict)

dict_03.update(dict_01)
print(dict_03)


tuple1 = ('a', 'b', 'c')
tuple2 = (1, 2, 3)
tuple3 =  tuple1 + tuple2
for item in tuple3:
    # if item == 'a':
    # print(item)
    print(tuple3)