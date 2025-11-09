def pow(a, n, m):
    return a**n%m

def urovn(osn, base, arr, res, mod):
    l = len(arr)
    print("2**(", end = "")
    for i in range(l+1):
        print(f"x{i}*2**{i}", end = "")
        print(" ... )")
    stepen = (mod-1)//(base**(l+1))
    stepen_arr = [stepen*base**i for i in range(l+1)]
    for i in range(l):
        stepen_arr[i] *= arr[i]
    

    
    left_pow = stepen_arr[-1]
    right_pow = [0]+[mod-i-1 for i in stepen_arr[:-1]]
    #right = sum([pow(osn, i, mod) for i in right_pow]) * pow(res, stepen, mod)
    right =  pow(osn, sum(right_pow), mod) * pow(res, stepen, mod)
    right = right % mod
    stepen_arr[-1] = f"{stepen_arr[-1]}x"
    
    print(f"{osn}**{left_pow}x={right}")
    for i in range(base):
        if pow(osn, left_pow*i, mod) == right:
            x = i
            break
    else:
        print("x not found; error")
        return
    
    print(f"{x = }")
    return x


BASE = 2
TARGET = 15
MOD = 37

MNOJITELI = [[2, 2], [3, 2]]

d= dict()

for p, n in MNOJITELI:
    x_arr = []
    for i in range(n):
        x = urovn(BASE, p, x_arr, TARGET, MOD)
        print()
        x_arr += [x]
    
    d[p] = x_arr

print(d)
for i in range(MOD):
    valid = 1
    for p, arr in d.items():
        m = sum([p**j*arr[j] for j in range(len(arr))])
        if i%(p**(len(arr))) != m: break
    else:
        print(i)

