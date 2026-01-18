class condition_02:
    '''

    if-else
    while
    for
    break
    continue

    '''
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
            print(f'test-->>>>>>>> {i}')
        print('结束')

    def learncontinue(self):
        numbers = [1,2,3,4,5]
        for i in numbers:
            if i == 4:
                continue
            print(f'i value is ', i)
            print(f'test-->>>>>>>> {i}')

sumtools = condition_02()
print(sumtools.learnfor(100))
print(sumtools.learnwhile(100))
print(sumtools.learnbreak())
print(sumtools.learncontinue())




