from pydantic import UUID1


class lesson20260118:
    def __init__(self):
        pass

    def Increment(self, value):
        self.value += 1
        return self.value

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


print('lesson 20260118')