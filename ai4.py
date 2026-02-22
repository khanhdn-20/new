import math
def factorial(n):
    result = 1.000000000
    for x in range(1,n+1):
        result *= x
    return result
def euler(n):
    result = 0.000000000
    for x in range(n+1):
        result += 1.000000000/factorial(x)
    return result
def exp(x,n):
    return pow(euler(n),x)

#################################################

n = 6
print(f"Giai thừa của {n} là: {factorial(n)}")

n = 8
e_approx = euler(n)
print(f"Số e gần đúng với {n} số hạng: {e_approx}")
print(f"Số e thực tế: {math.e}")
print(f"Độ lệch: {abs(math.e-e_approx)}")

x = 2
n = 10
exp_approx = exp(x, n)
print(f"e^{x} gần đúng với {n} số hạng: {exp_approx}")
print(f"e^{x} thực tế: {math.exp(x)}")
print(f"Độ lệch: {abs(math.exp(x)- exp_approx)}")