from random import randint

from math import prod

def notLiarF(a, m):
    return (a**2+1)%m

def getP(B):
    arr = []
    for i in range(2, B):
        for p in arr:
            if i%p == 0:
                break
        else:
            arr += [i]
    return arr
    

def getM(arr, B):
    out = []
    for q in arr:
        i = 1
        while q**i < B:
            i+=1
        i -= 1
        out += [q**i]
    return prod(out)
    

def nod(a, b):
    res = 1
    for i in range(2, max(a, b)):
        if a%i== 0 and b%i==0:
            res = i
    return res

n = 1313
B = 6
B1 = 10

x = randint(0, n)

arr_B = getP(B)
M = getM(arr_B, B)
print(f"{M = }")
print(f"{x = }")
a = x**M%n
print(f"{a = }")
p = nod(a-1, n)
print(f"{nod(a-1, n) = }")
if n%p == 0:
    print()
    print(f"{n} = {p} * {n//p}")
else:
    print("ERROR")
    print(f"{n} = {p} * {n/p}")