from functools import wraps, lru_cache


def api_cache(expire=60):
    """接口缓存装饰器：缓存expire秒内的请求结果"""

    def decorator(func):
        # 用lru_cache实现缓存，maxsize=None无限制
        cached_func = lru_cache(maxsize=None)(func)

        @wraps(func)
        def wrapper(*args, **kwargs):
            # 简化版：实际需结合时间实现过期（此处用lru_cache基础功能）
            return cached_func(*args, **kwargs)

        return wrapper

    return decorator


@api_cache(expire=300)
def get_user_info(user_id):
    """模拟接口请求：获取用户信息"""
    print(f"请求接口：get_user_info({user_id})")
    return {"user_id": user_id, "name": "张三" '\n' }


# 第一次调用：执行接口请求
print(get_user_info(1001), '\n' )
# 第二次调用：直接返回缓存（无接口请求打印）
print(get_user_info(1001))







@lru_cache(maxsize=None, typed=False)
def calculate_fib(n):
    """计算斐波那契数列（递归场景，缓存效果显著）"""
    if n <= 1:
        return n
    return calculate_fib(n-1) + calculate_fib(n-2)

# 第一次调用：执行计算并缓存结果
print(calculate_fib(100))  # 快速返回（无缓存会因重复计算卡死）
# 第二次调用：直接返回缓存值（无需计算）
print(calculate_fib(100))

# 查看缓存信息（命中/未命中次数）
print(f"缓存命中次数：{calculate_fib.cache_info().hits}")
print(f"缓存未命中次数：{calculate_fib.cache_info().misses}")

# 清空缓存（如需重新计算）
calculate_fib.cache_clear()