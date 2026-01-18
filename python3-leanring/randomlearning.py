import random

class randomlearning:

    '''
    0-10之间随机生成一个数字

    '''
    def learnrandom(self):
        luckynum = [random.randint(0, 10) for _ in range(1)]
        return luckynum
generate = randomlearning()
print(generate.learnrandom())
print(type(generate.learnrandom()))