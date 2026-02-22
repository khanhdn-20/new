import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def grad(w: np.array, ex: list):
    res = np.array([0.0,0.0])
    for n in range(len(ex)):
        x = np.array([ex[n][0],1.0])
        res += 2*(w@x - ex[n][1])*x
    return res/float(len(ex))

car = pd.read_csv('used_cars.csv')
x = car['model_year']
y = car['price'].str.replace('$','').str.replace(',','').astype(float)
x = (x - x.min())/(x.max() - x.min())
y = (y - y.min())/(y.max() - y.min())
ex = list(zip(x, y))

w0 = np.array([0,0])
for i in range(2000):
    w0 = w0 - 0.1*grad(w0, ex)
    
print(f"Ket qua la: {w0}")
plt.scatter(x, y, color='blue', label='Dữ liệu gốc')
plt.plot(x, w0[0]*x + w0[1], color='red', label='Đường dự đoán')
plt.legend()
plt.show()