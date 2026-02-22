import numpy as np
import matplotlib.pyplot as plt

def grad(w: np.array, ex: list):
    res = np.array([0.0,0.0])
    for n in range(len(ex)):
        x = np.array([ex[n][0],1.0])
        res += 2*(w@x - ex[n][1])*x
    return res/float(len(ex))

np.random.seed(42)
n = 100
x = np.linspace(0,10,n)
epsilon = np.random.normal(0,0.1,n)
y = 2*x + 1 + epsilon
ex = list(zip(x,y))

# x_min, x_max = x.min(), x.max()
# x_scaled = (x - x_min) / (x_max - x_min)
# ex = list(zip(x_scaled, y))
# plt.scatter(x,y)

w0 = np.array([0.0,0.0])
for i in range(2000):
    w0 = w0 - 0.01*grad(w0, ex)

print(f"Ket qua la: {w0}")
plt.scatter(x, y, color='blue', label='Dữ liệu gốc')
plt.plot(x, w0[0]*x + w0[1], color='red', label='Đường dự đoán')
plt.legend()
plt.show()