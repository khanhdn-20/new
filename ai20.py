import numpy as np

def func(x: np.array):
    new0 = 2*x[0]
    new1 = 4*x[1]
    return np.array([new0, new1])
def gd2(res: np.array,lr: float):
    for n in range(100):
        if np.linalg.norm(func(res)) < 10**(-6):
            return n, res
        res = res - lr*func(res)
        if n%10==9:
            print(f"[x,y]= {res}, f(x)= {res[0]**2 + 2*res[1]**2}")
    return n, res    

sp = np.array([4,2])
lr = 0.1
print(f"Ket qua ht voi so lan: {gd2(sp,lr)}")
print("#####################")
print(f"Ket qua ht voi so lan: {gd2(sp,0.01)}")
print("#####################")
print(f"Ket qua ht voi so lan: {gd2(sp,0.4)}")