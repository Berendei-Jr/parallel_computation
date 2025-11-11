a = 11
b = 69
mod = 109

given_ps = [2, 3]

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

d = dict()
ps = [2, 3, 5, 7]

for i in range(mod):
    p = pow(a, i, mod)
    if p in ps:
        d[p] = i
      #  print(p, i)
print()

for i in range(1, mod):
    s = (b*pow(a, i, mod))%mod
    deli = isDelitsya(s, ps)
    print(f"Проверяем {i}: {b}*{a}^{i} mod {mod} = {s}\t {s} раскладывается на множители {deli}")

    if deli == given_ps:
        print(f"\nНайдено искомое разложение: {s} = {'*'.join([str(delitel) for delitel in deli])}")
        break

deli = [d[i] for i in deli]

print(f"log({b})+{i} = {'*'.join([str(delitel) for delitel in deli])} mod {mod-1}")
print(f"log({b})+{i} = {sum(deli)%(mod-1)}")
print(f"Ответ: {(sum(deli)-i)%(mod-1)}")
