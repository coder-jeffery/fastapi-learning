import functools

def check_permission(required_role):
    """权限校验装饰器：检查用户角色是否符合要求"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(user, *args, **kwargs):
            if user.get("role") != required_role:
                raise PermissionError(f"无权限！需要{required_role}角色")
            return func(user, *args, **kwargs)
        return wrapper
    return decorator

@check_permission(required_role="admin")
def delete_user(user, user_id):
    print(f"管理员{user['name']}删除用户：{user_id}")

# 测试：管理员角色（正常执行）
admin_user = {"name": "管理员", "role": "admin"}
delete_user(admin_user, 1001)  # 输出：管理员管理员删除用户：1001

# 测试：普通用户（抛出异常）
normal_user = {"name": "普通用户", "role": "user"}
# delete_user(normal_user, 1001)  # 报错：PermissionError: 无权限！需要admin角色