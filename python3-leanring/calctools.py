class CalcTools:

    def add_sub_mul_div(self, number1, number2, operation):
        if operation == '+':
            return number1 + number2
        elif operation == '-':
            return number1 - number2
        elif operation == '*':
            return number1 * number2
        elif operation == '/':
            return number1 / number2




calc = CalcTools()
print(f'运算所得结果：',calc.add_sub_mul_div(1,2,'+'))