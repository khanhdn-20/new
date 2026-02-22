def cremat():
    summ = 0
    mat = [[0,0,0],
           [0,0,0],
           [0,0,0]]
    for y in range(len(mat)):
        for x in range(len(mat[0])):
            # mat[y][x] = input("Nhap gia tri: ")
            mat[y][x] = 1
            while True:
                try:
                    mat[y][x] = int(mat[y][x])
                    break
                except ValueError:
                    mat[y][x] = input("Hay nhap gia tri la so thuc: ")
            summ += mat[y][x]
    return mat, summ


matrix, summ = cremat()
print("Ma tran la: ")
for y in range(len(matrix)):
    print(matrix[y])
print(summ)
print("")

number = [0,1,2,3,4,5,6,7,8,9]
print(number[2:6+1])
print(number[::2])
number.reverse()
print(number)
print("")

new = [1, 2, 2, 3, 4, 4, 5]
new = set(new)
new.add(6)
print(new)
new = tuple(new)
print(new)
print(max(new))
