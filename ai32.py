import torch
import math
import numpy as np

x = torch.tensor(3.0, requires_grad=True)
f1 = x**2 + 3*x +1
f1.backward()
print(float(x.grad))
x.grad.zero_()
f2 = torch.sin(x) + torch.exp(x)
f2.backward()
print(float(x.grad))
x.grad.zero_()

x = torch.tensor(2.0, requires_grad=True)
y = torch.tensor(4.0, requires_grad=True)
z = (x**2)*y + y**3
z.backward()
print(float(x.grad))
print(float(y.grad))
x.grad.zero_()
y.grad.zero_()

x = torch.tensor(1.0, requires_grad=True)
u = x**3 + 2*x
f = torch.log(u)
f.backward()
print(float(x.grad))
x.grad.zero_()
