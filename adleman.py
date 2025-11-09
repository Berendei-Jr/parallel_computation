def pow(a, n, m):
    return a**n%m

def isDelitsya(a, arr):
    out = []
    while a>1:
        for i in arr:
            if a%i == 0:
                a = a//i
                out += [i]
                break
        else:
            return []
    return out

a = 2
b = 37
mod = 101

ps = [2, 3, 5, 7]
d = dict()

for i in range(mod):
    p = pow(a, i, mod)
    if p in ps:
        d[p] = i
        print(p, i)
print()
for i in range(mod):
    s = (b*pow(2, i, mod))%mod
    deli = isDelitsya(s, ps)
    if deli:
        break

print(i, s, deli)
deli = [d[i] for i in deli]

print(f"log({d})+i = {deli}")

print(f"otvet: {(sum(deli)-i)%(mod-1)}")
