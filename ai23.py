import pandas as pd
from sklearn.model_selection import train_test_split

c = pd.read_csv('used_cars.csv')
# print(c.isna().sum())
c.drop('clean_title', axis=1, inplace=True)
c.fillna("Unknown", inplace=True)
# print(c.isna().sum(), '\n')


c['price'] = c['price'].str.replace('$','').str.replace(',','').astype(float)
# print(c['price'], '\n')


c['car_year'] = c['model_year'].apply(lambda x: 2025-x)
# print(c['car_year'], '\n')
c['milage'] = c['milage'].str.replace(',','').str.replace(' mi.','').astype(int)
# print(c['milage'], '\n')

c['engine'] = c['engine'].str.extract(r'(\d+\.\d+)L').astype(float)
c['engine'] = c['engine'].fillna(c['engine'].mean())
# print(c['engine'], '\n')

u = c['brand'].unique()
udict = { u[x]: x for x in range(len(u))}
# for x in range(len(u)):
#     udict[u[x]] = x
# print(udict)

c['brand'] = c['brand'].apply(lambda x: udict.get(x))
# print(c['brand'])

X = c.drop('brand', axis=1)
y = c['brand']

xtr, xt, ytr, yt = train_test_split(X, y, test_size=0.2, random_state=42)

print("--- KÍCH THƯỚC CÁC TẬP DỮ LIỆU ---")
print(f"Tong so mau ban dau: {len(c)}")
print("-" * 30)
print(f"X_train (đặc trưng huấn luyện): {xtr.shape}")
print(f"y_train (nhãn huấn luyện):     {ytr.shape}")
print("-" * 30)
print(f"X_test  (đặc trưng kiểm tra):  {xt.shape}")
print(f"y_test  (nhãn kiểm tra):       {yt.shape}")

print("\n--- 5 DÒNG ĐẦU CỦA X_TRAIN ---")
print(xtr.head())
# print(ytr.head())