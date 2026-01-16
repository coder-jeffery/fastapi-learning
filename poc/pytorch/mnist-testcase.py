import torch.optim as optim
from sympy.printing.pytorch import torch
from torch import nn
from torch.testing._internal.data.network1 import Net

from torchvision import datasets, transforms

# 数据加载
transform = transforms.ToTensor()
train_dataset = datasets.MNIST(root='./data', train=True, download=True, transform=transform)
train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=64, shuffle=True)

# 模型、损失函数、优化器
model = Net()
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

# 训练循环
for epoch in range(3):
    for data, target in train_loader:
        optimizer.zero_grad()          # 清零梯度
        output = model(data)           # 前向传播
        loss = criterion(output, target)  # 计算损失
        loss.backward()                # 反向传播
        optimizer.step()               # 更新参数
    print(f"Epoch {epoch+1}, Loss: {loss.item():.4f}")