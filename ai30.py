import torch as tor
import numpy as np

# n = tor.tensor([[7,7,7,7],[7,7,7,7],[7,7,7,7]])
# print(n)
# n2 = tor.tensor([2*i for i in range(6)])
# print(n2)
# n3 = tor.tensor(np.array(np.random.normal(0,1,6)))
# n3 = n3.reshape(2,3)
# print(n3)

a= tor.tensor([[1,2],
               [3,4]])
b= tor.tensor([[5],[6]])
print(a+b)
print(a@a)
print(a*b)
print(a.reshape(1,1,2,2))

# c = tor.rand(6)
# print(c.view(6,1))
# print(c)
# print(c.reshape(2,3))
# print(c)
# print(tor.cuda.is_available()) #Khong kha dung

