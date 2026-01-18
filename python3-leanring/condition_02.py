class condition_02:

    list_list = ['TOT','COT', 'GOT']

    def learnfor(self, number) :
        sum  = 0
        while number > 0:
            sum = sum + number
            number = number - 1
        return sum

    def learnwhile(self, number) :
        sum = 0
        while number > 0:
            sum = sum + number
            number = number - 1
        return sum

    def learnbreak(self) :
        number = [1,2,3,4,5]
        for i in number:
            if i == 3:
                break # 终止当前的循环
            print(i)
        print('结束')

sumtools = condition_02()
print(sumtools.learnfor(100))
print(sumtools.learnwhile(100))
print(sumtools.learnbreak())




