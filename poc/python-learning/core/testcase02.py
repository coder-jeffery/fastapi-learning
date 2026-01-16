# 变量、数据类型（int/str/list/dict/tuple/set 等）、运算符、流程控制（if-else、for/while 循环、break/continue）、异常处理（try-except-finally、自定义异常

# set 无序 不重复

words = ["apple", "banana", "apple", "orange", "banana"]
dictionary = dict(zip(words, words))
unique_count = len(set(words))
print("唯一单词数：", unique_count)  # 3
print(set(words))
print(list(words))
print(tuple(words))
print(dictionary)
for word in words:
    print(word)

# set 无序不重复 自动去重复 中括号
# tuple 元组 小括号

# 中括号： set 和 里 list- 可变（支持增删改）
# 大括号 dict

dict = {"1":"apple", "2":"banana", "3":"orange", "4":"banana"}
print(dict)
print(type(dict))


sum =0
x  = 1
while x <= 100:
    sum += x
    x += 1
print(sum)
