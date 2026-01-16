# 方式1：简单自定义异常（无额外属性）
class CustomError(Exception):
    """自定义基础异常类（可作为业务异常的父类）"""
    pass

# 方式2：带自定义信息的异常（推荐，更实用）
class InsufficientBalanceError(Exception):
    """余额不足异常"""
    def __init__(self, current_balance, need_balance):
        # 自定义异常属性
        self.current_balance = current_balance
        self.need_balance = need_balance
        # 自定义错误提示信息
        super().__init__(f"余额不足！当前余额：{current_balance}，需要余额：{need_balance}")

class UserNotFoundError(Exception):
    """用户不存在异常"""
    def __init__(self, user_id):
        self.user_id = user_id
        super().__init__(f"用户ID {user_id} 不存在！")


# 模拟业务函数：扣减余额
def deduct_balance(user_id, amount):
    # 模拟用户余额数据
    user_balances = {"1001": 50, "1002": 200}

    # 1. 检查用户是否存在
    if user_id not in user_balances:
        raise UserNotFoundError(user_id)  # 抛出用户不存在异常

    # 2. 检查余额是否足够
    current = user_balances[user_id]
    if current < amount:
        raise InsufficientBalanceError(current, amount)  # 抛出余额不足异常

    # 3. 扣减余额（正常逻辑）
    user_balances[user_id] -= amount
    print(f"扣减成功！用户{user_id}剩余余额：{user_balances[user_id]}")




# 调用业务函数，捕获自定义异常
try:
    deduct_balance("1001", 100)  # 余额50，扣减100 → 触发余额不足异常
    # deduct_balance("1003", 50)  # 用户不存在 → 触发用户不存在异常
except UserNotFoundError as e:
    # 处理用户不存在异常
    print(f"错误：{e}")
    # 可访问异常的自定义属性
    print(f"异常详情：用户ID {e.user_id} 未注册")
    # 额外操作：记录日志、返回用户友好提示等
except InsufficientBalanceError as e:
    # 处理余额不足异常
    print(f"错误：{e}")
    print(f"异常详情：当前{e.current_balance} < 需要{e.need_balance}")
except Exception as e:
    # 兜底捕获其他未预期的异常
    print(f"未知错误：{e}")
else:
    # 无异常时执行
    print("操作完成！")
finally:
    # 无论是否异常都执行（如关闭资源）
    print("本次操作结束\n")