import torch
import numpy as np

# x = torch.tensor([1,2,3])
# x.add_(5)
# print(x)
# x.fill_(1)
# print(x)

# a = torch.tensor([[1.0,2.0],[3.0,4.0]])
# print(a.sum(dim=0))
# print(a.mean(dim=1))

# a=torch.arange(12).reshape(3,4).float()
# print(a)
# print(a.add_(5))
# print(a.mul_(2))
# print(a.sum(dim=1,keepdim=True))
# print("Cac gia tri max va chi so tung phan tu la: ", *a.max(dim=0))

# b = torch.randn(5,5)
# print(b)
# print(b[b>0.5])
# print(b[b<-0.3], b[b>0.7])
# print(torch.where(b>=0, b, 0))
# print(torch.where(b<=0, b, 1))

# data = torch.tensor([[1,2],[3,4]])
# indices = torch.tensor([[0,0],[1,0]])
# print(data)
# print(data.sum(dim=0))   0 la theo cot
# print(torch.gather(data, 0, indices))
# print(torch.gather(data, 1, indices))
# 1 2     0 0
# 3 4     1 0

# 00 01 
# 10 01

# 00 00 
# 11 10

x=torch.randn(3,2,2)
y=torch.randn(3,2,2)
print(torch.bmm(x,y))
print(x+y)
