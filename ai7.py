import sys
def createlist():
    n = int(input("So phan tu cua list la: "))
    list = []
    for x in range(n):
        i = int(input(f"Nhap so nguyen thu {x}: "))
        list.append(i)
    return list

def sum(list):
    result = 0
    for x in list:
        result += x
    return result

def max2(list):
    result = 0
    for x in list:
        if x >= result:
            result = x
    return result

def min(list):
    return int(sorted(list)[0])

def max(list):
    return int(sorted(list,reverse=1)[0])


x = createlist()
print(x)
print(sum(x))
print(min(x))
print(max(x))


num = [10,20,30,40]
num.append(int(input("Them phan tu: ")))
print(num)
num.insert(int(input("Chon chi so: ")), int(input("Dien so can them: ")))
print(num)
num.remove(int(input("Nhap gia tri can xoa: ")))
print(num)

for x in range(len(num)):
    print(f"Phan tu tai chi so {x} la: {num[x]}")
print("")
i = 0
while i < len(num):
    print(f"Phan tu tai chi so {i} la: {num[i]}")
    i += 1


newnum = [10, 25, 30, 40, 50]

# x = int(input("Nhap so can tim: "))         
# if not(isinstance(x)):
#     print("LOI")                            ERROR
#     sys.exit()
    
x = input("Nhap so can tim: ")

try:
    x = int(x)
except ValueError:
    print("Loi... Dang dung chuong trinh")
    sys.exit()

print( f"Co ton tai\nChi so la: {newnum.index(x)}" if x in newnum else "Khong tim thay")