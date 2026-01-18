class People:

    def __init__(self, name, age, weight, height, address):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    def showinfo(self):
        # print("Name: " + self.name)
        # print("Age: " + str(self.age))
        return f'{self.name} {self.age} {self.weight} {self.height}'

    @staticmethod
    def playgame():
        return f'to be or not to be this is question | this static method so no required self paramster'

    @classmethod
    def playpiano(cls, whoes):
        return f'the piano ->>>>>>>>>> {whoes} {cls.playgame() } '

jeff = People('jeff', 20, 10, 10, "Jeff")
# jeff.showinfo()
print(jeff.showinfo())
print(People.playgame())
# print(jeff.playgame())
print(People.playpiano('Jeff'))

'''
python基本类型： 字符串、数值、列表、元组、字典 五种基本类型

静态方法
类方法

'''
