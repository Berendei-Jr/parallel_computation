a = 2
b = 37
p = 101
from math import sqrt



def isP(n):
    s = int(sqrt(n))
    a = [i for i in range(2, s+1)]
    while a:
        if n%a[0] == 0: return False
        a = [a[i] for i in range(1, len(a), a[0])]
    return True

def getZUV(p, a, b):
    u = 0
    v = 0
    z = 1
    while 1:


        yield z, u, v

        if z < p//3:
            u +=1
        elif z < 2*p//3:
            u *= 2
        else:
            u = u
        u = u%(p-1)
        
        if z < p//3:
            v = v
        elif z < 2*p//3:
            v *= 2
        else:
            v = v + 1
        v = v %(p-1)
        

        z = a**v * b**u
        z = z%p

        
d = dict()
for z, u, v in getZUV(p, a, b):
    print(u, v, z)
    if z not in d:
        d[z] = (u, v)
    else:
        u2, v2 = d[z]
        print(f"{a}**{v} * {b}**{u} = {a}**{v2} * {b}**{u2}")
        q = u-u2 if u2<u else u2-u
        if q == 0: exit(0)
        if (p-1)%q==0:continue
        if isP(q):break
print()
print(f"{a}**{v} * {b}**{u} = {a}**{v2} * {b}**{u2}")
if u2 < u: u, v = u-u2, v-v2
else: u, v = u2-u, v2-v
print(f"log{a}({b}) = {(-v)%(p-1)} * {u}**-1")