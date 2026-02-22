studentname = "Khanh"
mathscore = 9.0
sciencescore = 8.5
ms = str(mathscore)
print("Ten: " + studentname + "  Diem toan: " + ms)
print(f"Ten: {studentname}  Diem toan: {mathscore}  Diem khoa hoc: {sciencescore}")

print(mathscore + sciencescore)
print(mathscore - sciencescore)
print(mathscore * sciencescore)
print(mathscore / sciencescore)

mathscore += 1
print(f"Ten: {studentname}  Diem toan: {mathscore}  Diem khoa hoc: {sciencescore}")

tb = (mathscore + sciencescore)/2
if tb>=8.0:
    print("XUAT SAC")
elif tb>=6.5:
    print("GIOI")
elif tb>=5.0:
    print("TRUNG BINH")
else:
    print("CAN CO GANG")