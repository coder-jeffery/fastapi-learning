from pydantic import UUID1

class lesson20260118:
    def __init__(self):
        pass

    def Increment(self, value):
        self.value += 1
        return self.value

    def add_sub_mul_divi(self, number1, number2, operation):
        if operation == '+':
            return number1 + number2
        elif operation == '-':
            return number1 - number2
        elif operation == '*':
            return number1 * number2
        elif operation == '/':
            return number1 / number2

    # calc  = lesson20260118()
    # print(f'运算所得结果：', lesson20260118().add_sub_mul_divi(5, 10, '+'))


    var_int = 100
    var_float = 250.09
    var_str = f'RAG | deepseek | Qwen | Chatgpt | Grok | Zhipu | OpenAI | Claude | Gemini'
    var_list = ['语义分割', '长度分块切割', '递归分割' , '文档结构分割' ,'大模型自动分割']

    var_number = (1,2,3,4,5)

    var_tuple = tuple(var_list)

    var_dict = dict(zip(var_number, var_tuple))

    print(type(var_int), type(var_float), type(var_str), type(var_list) , type(var_tuple), type(var_dict))
    print('\n')
    print(var_dict, '\n',var_tuple)

'''
list vs tuple:
    list 可变  []     有序
    tuple 不可变 （）  有序
    dictionary {}
    
'''

calc = lesson20260118()
# print(calc.Increment(2))
print(f'运算所得数值：',calc.add_sub_mul_divi(15, 15, '*'))

print('lesson 20260118')