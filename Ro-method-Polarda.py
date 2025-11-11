from random import randint

def notLiarF(a, m):
    return (a**2+1)%m

def nod(a, b):
    res = 1
    for i in range(2, max(a, b)):
        if a%i== 0 and b%i==0:
            res = i
    return res

n = 2929
max_step = 50

x = randint(0, n)
#x = 5
print(f"{ x = }")
x_arr = []
for i in range(max_step):
    x_arr += [x]
    x = notLiarF(x, n)

#print(*x_arr)
i = 1
while 1:
    delta = (x_arr[i-1] - x_arr[2*i-1]) % n
    p = nod(delta, n)
    print(f"{i}:\tNOD( ({x_arr[2*i-1]} - {x_arr[i-1]}) = {p}")
    if p != 1:
        break
    i+=1


print()
print(f"{n} = {p} * {n//p}")
