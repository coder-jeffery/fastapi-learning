import torch

# 创建 tensor
x = torch.tensor([1, 2, 3])
y = torch.randn(3, 3)  # 随机初始化

# 基本操作
z = x + y[0]  # 自动广播
print(z)

# 转移到 GPU（如果有）
if torch.cuda.is_available():
    x = x.cuda()


x = torch.tensor(2.0, requires_grad=True)
y = x ** 2
y.backward()  # 计算 dy/dx
print(x.grad)  # 输出: tensor(4.0)