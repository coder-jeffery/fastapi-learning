import torch

# 创建张量
x = torch.tensor([1, 2, 3])
y = torch.randn(3, 3)  # 随机正态分布
z = torch.zeros(2, 4)

# 基本操作
a = torch.tensor([1., 2., 3.])
b = torch.tensor([4., 5., 6.])
c = a + b  # 或 torch.add(a, b)

# GPU 支持（如果可用）
if torch.cuda.is_available():
    x = x.cuda()  # 或 x.to('cuda')
print("result => ",x)


'''自动求导（Autograd）'''
x = torch.tensor(2.0, requires_grad=True)
y = x ** 2 + 3 * x + 1
y.backward()  # 计算 dy/dx
print(x.grad)  # 输出: tensor(7.) 因为 dy/dx = 2x + 3 = 7



'''构建神经网络（使用 torch.nn） '''
import torch.nn as nn
import torch.nn.functional as F

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(10, 50)   # 输入10维，输出50维
        self.fc2 = nn.Linear(50, 1)    # 输出1维

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return x

net = Net()
print(net)



'''损失函数与优化器'''
# 假设输入和目标
inputs = torch.randn(100, 10)
targets = torch.randn(100, 1)

# 损失函数（如均方误差）
criterion = nn.MSELoss()

# 优化器（如 SGD 或 Adam）
optimizer = torch.optim.Adam(net.parameters(), lr=0.01)
print(criterion(net(inputs), targets).item())



# 保存
torch.save(net.state_dict(), 'model.pth')

# 加载
net = Net()
net.load_state_dict(torch.load('model.pth'))
net.eval()  # 设置为评估模式（关闭 Dropout/BatchNorm 的训练行为）