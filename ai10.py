
def fre(s):
    dic = dict({})
    for x in range(len(s)):
        dic[int(s[x][1])] = 0
    for x in range(len(s)):
        # if x != (int(t) for t in dic.keys()):
        #     dic[int(s[x][1])] = 0
            
        dic[int(s[x][1])] += 1
    return dic
    
s = [("T",4,8.5),("L",3,9.0),("H",3,8.0)]
print(f"Tu dien so tin chi la: {fre(s)}")

set1 = set({x[2] for x in s})
print(f"Tap hop diem trung binh: {set1}")
print("Mon hoc co diem trung binh cao nhat la: ", *tuple(s[i] for i in range(len(s)) if s[i][2] == int(max(set1)))) #unpack
print("")
###########################################
numbers = [1,2,3,3,1,4]
def fre2(num):
    dic2 = {}
    for x in num:
        dic2[int(x)] = num.count(x)
    return dic2

dix = fre2(numbers)
print(f"Tan so la: {dix}")
one_time = set({})
for k, v in dix.items():
    if v == 1:
        one_time.add(k)
print(f"Danh sach cac phan tu xuat hien 1 lan la: {one_time}")

dix = list(dix.items())
dix = sorted(dix, key = lambda x:x[1], reverse=True)
print(f"Sau khi sap xep: {dix}")
print("")
############################################
pairs = [(10,0),(15,1),(13,2),(12,3)]

pairs = sorted(pairs, key = lambda x:x[0])
hieu = abs(pairs[0][0]-pairs[1][0])
for x in range(len(pairs)-1):
    if abs(pairs[x][0]-pairs[x+1][0]) <= hieu :
        cap = (pairs[x][1], pairs[x+1][1])
        hieu = abs(pairs[x][0]-pairs[x+1][0])
print(f"Cap chi so gan nhat: {cap}")

pairs = sorted(pairs, key = lambda x:x[1])
lech = {}
for x in pairs:
    for y in pairs[pairs.index(x)+1::]:
        key = (int(x[1]),int(y[1]))
        lech[key] = abs(x[0]-y[0])
print(lech)

giatri = []
dpairs = dict(pairs)
for k,v in dpairs.items():
    giatri.append(k)
giatri = set(giatri)
print(giatri)