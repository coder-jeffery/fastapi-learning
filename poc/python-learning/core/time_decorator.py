# 步骤1：定义装饰器函数
def timer_decorator(func):
    """计时装饰器：统计函数执行时间"""
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)  # 执行原函数
        end = time.time()
        print(f"{func.__name__} 执行耗时：{end-start:.2f}秒")
        return result
    return wrapper

# 步骤2：使用装饰器（@+装饰器名）
@timer_decorator
def calculate_sum(n):
    """计算1到n的和"""
    return sum(range(n+1))

# 调用函数（自动触发装饰器）
calculate_sum(1000000)  # 输出：calculate_sum 执行耗时：0.02秒

print(timer_decorator(1000000))



print('****************************')
# 步骤1：定义装饰器函数（接收原函数作为参数）
def decorator(func):
    # 步骤2：定义内层函数（包装函数，添加额外功能）
    def wrapper():
        print("装饰器：执行前的额外操作")  # 新增功能
        result = func()  # 调用原函数
        print("装饰器：执行后的额外操作")  # 新增功能
        return result  # 返回原函数的结果
    # 步骤3：返回内层函数（替代原函数）
    return wrapper

# 步骤4：定义原函数
def say_hello():
    print("Hello, Python!")
    return "执行完成"

# 步骤5：用装饰器包装原函数（核心：替换原函数）
say_hello = decorator(say_hello)

# 调用原函数（实际调用的是wrapper）
result = say_hello()
print(f"原函数返回值：{result}")