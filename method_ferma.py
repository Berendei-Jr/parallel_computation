from math import sqrt

n = 247

m = round(sqrt(n))
print(f"{m = }")
print()

for i in range(m+1):
    q = (m+i)**2 - n
    
    s = sqrt(q)
    print(i, q, s)
    if (s-int(s))<0.0001:
        break
else:
    print("not found")
    exit()

print()

p = int(m+i+s)
q = int(m+i - s)
if (q < 0): q = -q
print(f"{n} = {p} * {q}")