def sum(n):
    result = 0
    while n != 0:
        n, du = divmod(n,10)
        result += du
    return result    
    
def func(x):
    return 3*(x**2-1)

def newton(x):
    n = 0
    while True:
        if n > 100:
            break
        a = x
        x = x - (x**3 - 3*x + 1)/func(x)
        n += 1
        if abs(a-x) < 0.0001:
            break
    return x
        

    
n = int(input())
print(sum(n))
print(newton(5))