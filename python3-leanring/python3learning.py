
class pythonlearning:

    a = 1

    def __init__(self):
        print("pythonlearning...")


    def learning_basetype(self):
        print("learning_basetype...")

    b  =10
    llamaindex = 'this is large language model'
    test = bool
    pai = 3.1415926
    money = 999999999999999.1234
    number = [1,2,3,4,5,6,7,8,9]




    print(type(a), a,type(llamaindex), llamaindex, type(b), b)
    print(f'********************************************************')
    print(type(money), type(number), type(pai))
    print(f'********************************************************')
    print(f'python基本数据类型： 数字 number，字符串 string，列表 list， 元祖 tuple， 字典 dictionary')
    print(f'********************************************************')


    var_list = [1,2,3,4,5,6,7,8,9]
    print(type(var_list), var_list)
    print(f'********************************************************')
    var_data = {'llamaindex','LangChain', 'LangGraph', 'Milvus', 'postgresql'}
    print(type(var_data), var_data)

    var_dictionary = {}
    var_tuple = ('pytorch', 'tensorflow', 'python', 'django', 'fastapi', 'flask')
    print(type(var_tuple), var_tuple, var_tuple[0])

    for item in var_tuple:
        var_dictionary[item] = var_tuple.index(item)
        # var_dictionary[item] = var_tuple[var_tuple.index(item)]
        print(var_dictionary[item])

    print(f'********************************************************')


print(pythonlearning())
print(pythonlearning().learning_basetype())
print(f'中文显示主题内容')



