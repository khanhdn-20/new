import numpy as np

arr = np.array([1,-2,3,-4,5,-6])
print(np.where(arr < 0, 0, arr))
arr2 = np.where(arr % 2, "odd", "even") #np.where(condition, True = x, False = y), ko co x va y return index
print(arr2)
print("List index:", *np.where(arr>2))
print("")

t = np.array([25, 28, 30, 22, 35, 18, 20])
print(np.select([t<20, t>=30],["Cold","Hot"],default="Mild"))
print("")

mat = np.random.randint(1,100,(5,5))
def chuanhoa(mat1):
    return (mat1 - np.min(mat1))/(np.max(mat1)-np.min(mat)) 
mat = np.apply_along_axis(chuanhoa, 1, mat)
print(mat)
print("")

mat = np.random.randint(1,100,(5,5))
mat = mat - np.max(mat, axis = 0, keepdims= True)
# print(mat)
mat = np.exp(mat)
tong = mat.sum(axis=0)
mat = mat/tong
print(mat)
print("")

data = np.array([
                [1,2,np.nan],
                [4,np.nan,6],
                [7,8,9]
                ])
# print(data)
data = np.where(np.isnan(data), np.apply_along_axis(np.nanmean,0,data), data)
print(data)


def zsco(mat):
    return (mat - np.mean(mat))/np.std(mat)
    
data = np.apply_along_axis(zsco,0,data)
print(data)


data = np.apply_along_axis(chuanhoa,0,data)
print(data)