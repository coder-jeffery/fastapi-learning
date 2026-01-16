import time
from functools import wraps

def timer(func):
    @wraps(func)  # 保留原函数__name__等属性
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        res = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__} 耗时: {end-start:.4f}秒")
        return res
    return wrapper

@timer
def calc_sum(n):
    return sum(range(n))

calc_sum(1000000)  # 输出：calc_sum 耗时: 0.0123秒