import copy

# n = int(input("Nhap so phan tu cua list: "))
# list1 = [x for x in range(1, n+1) if x%2!=0]
# print(list1)


ori = [1,2,[3,4]]
sao1 = ori.copy()
sao2 = copy.deepcopy(ori)

sao1[2][0] = 7
sao2[2][0] = 10

print(ori)
print(sao1)
print(sao2)


stu = {"An":8.5, "Binh":9.0}
stu["Cuong"] = 8.5

print(stu.keys())
print(sum(stu.values())/len(stu.values()))

