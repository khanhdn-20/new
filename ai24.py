import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

c = pd.read_csv('used_cars.csv')

c.drop('clean_title', axis=1, inplace=True)
c.fillna("Unknown", inplace=True)
c['price'] = c['price'].str.replace('$','').str.replace(',','').astype(float)
c['car_year'] = c['model_year'].apply(lambda x: 2025-x)
c.drop('model_year', axis=1, inplace=True)
c['milage'] = c['milage'].str.replace(',','').str.replace(' mi.','').astype(int)
c['engine'] = c['engine'].str.extract(r'(\d+\.\d+)L').astype(float)
c['engine'] = c['engine'].fillna(c['engine'].mean())
u = c['brand'].unique()
udict = { u[x]: x for x in range(len(u))}
c['brand'] = c['brand'].apply(lambda x: udict.get(x))

pd.set_option('display.max_columns', None)
# print(c.head())

def grad(w: np.array, ex: list):
    res = np.zeros_like(w, dtype=float)

    for n in range(len(ex)):
        x = np.concatenate([ex[n][0],[1.0]])
        res += 2*(w@x - ex[n][1])*x
        
    return res/float(len(ex))

features = ['brand', 'engine', 'car_year', 'milage']
targets = 'price'

xr = c[features].values
y = c[targets].values

xmean = xr.mean(axis=0)
xstd = xr.std(axis=0)
xscaled = (xr - xmean)/xstd

ex = [[xscaled[i], y[i]] for i in range(len(y))]

w0 = np.zeros(len(features) + 1)

loss_history = []

for i in range(2000):
    w0 = w0 - 0.01*grad(w0, ex)
    
    y_pred_all = np.array([w0 @ np.concatenate([e[0], [1.0]]) for e in ex])
    mse = np.mean((y_pred_all - y)**2)
    loss_history.append(mse)
    
print(f"Kết quả cuối cùng: ")
print(f"Trọng số (weights): {w0[:-1]}")
print(f"Hệ số tự do (bias): {w0[-1]}")


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

ax1.plot(loss_history, color='blue', lw=2)
ax1.set_title('Biểu đồ giảm sai số (Loss Function)', fontsize=14)
ax1.set_xlabel('Số lần lặp (Epochs)')
ax1.set_ylabel('Mean Squared Error (MSE)')
ax1.grid(True, linestyle='--', alpha=0.7)

y_final_pred = np.array([w0 @ np.concatenate([e[0], [1.0]]) for e in ex])

ax2.scatter(y, y_final_pred, alpha=0.5, color='green', s=10)
ideal_line = [min(y), max(y)]
ax2.plot(ideal_line, ideal_line, color='red', linestyle='--', lw=2, label='Lý tưởng')

ax2.set_title('So sánh Thực tế vs Dự đoán', fontsize=14)
ax2.set_xlabel('Giá thực tế ($)')
ax2.set_ylabel('Giá dự đoán ($)')
ax2.legend()
ax2.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()