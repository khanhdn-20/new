import math
def prime(n):
    if n==1:
        return False
    for x in range(2,int(math.sqrt(n))+1):
        if n%x==0:
            return False
    return True
def fprime(n):
    for x in range(1,n+1):
        if prime(x):
            yield x
            
def perfnumber(n):
    result = 0
    for d in range(1,n):
        if n%d==0:
            result += d
    if n==result:
        return True
    return False
def sumperfnum(n):
    result = 0 
    for x in range(2,n):
        if perfnumber(x):
            result += x
    return result

            
print(list(fprime(1000)))
n = int(input())
print(sumperfnum(n))