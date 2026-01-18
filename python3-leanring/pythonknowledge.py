class pythonknowledge:

    a = 100
    llamaindex = 250.55
    python = ['django', 'fastapi', 'fask']

    def sayHello(self):
        return 'this is large language model on 2022 11'

    def statistical(self, var_zimu):
        count = 0
        data = 'dahkjsdhqiwuiueqdwbbdmnasdabsdkjahsdjkzmcbzowqeuhiquweh'

        for c in data:
            if c == var_zimu:
                count += 1

        print('a出现的次数', count)
        return  f'出现的次数',count

    def learnTuple(self):
        number = (1,2,3,4,5,6,7,8)
        return number

    def learnStr(self):
        data_str = 'llm: Qwen deepseek Zhipu minimax GLM'
        return data_str

    def learnbasetype(self):
        '''
        数字类型：int / long / float / complex
        '''
        number = 100000
        big_number  =  9000000000 * number
        decimal_number = 99999999999.9999
        print(f'how to learn learnbasetype ->>>>>>',type(big_number), type(decimal_number), type(number))
        return type(big_number), type(decimal_number), type(number)

    def learnlist(self):
        list_value = [1,2,3,4,5,6,7,8,9,10,11,12,13] # list集合
        # list_tuple = (1,2,3,4,5,6,7,8,9,10,11,12,13)
        # list_dictionary = {'a':1,'b':2,'c':3,'d':4}
        list_value.append('this is bubble')
        return list_value

    def learnTupleknowledge(self):
        list_tuple = (1,2,3,4,5,6,7,8,9,10,11,12,13)
        return list_tuple

    def learnDictionaryknowledge(self):
        list_dictionary = {'a':1,'b':2,'c':3,'d':4}
        return list_dictionary

testmethod = pythonknowledge()
print(testmethod.sayHello(), '\n')
print(testmethod.a, type(testmethod.a),'\n')
print(testmethod.llamaindex,type(testmethod.llamaindex), '\n')
print(testmethod.learnbasetype())

print(testmethod.statistical('q'))
print(pythonknowledge.learnTuple(2))

learn = pythonknowledge()
print(learn.learnStr())

learncollection = pythonknowledge()
print(learncollection.learnlist(), type(learncollection.learnlist()), '\n')

list_tuple = pythonknowledge()
print(list_tuple.learnTupleknowledge(), type(list_tuple.learnTupleknowledge()), '\n')

list_dictionary = pythonknowledge()
print(list_dictionary.learnDictionaryknowledge(), type(list_dictionary.learnDictionaryknowledge()), '\n')
