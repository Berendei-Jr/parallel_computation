from random import randint

def symbol_legandra(a, p):
    return (a**((p-1)//2))%p

def tonnel_shenksa(a, p):
    print("Тонелли-Шенкса")
    while symbol_legandra(N := randint(1, p-1), p)==1:
        pass
    print(f"{N=}")
    t = p-1
    e = 0
    while t%2==0:
        t=t//2
        e+=1

    print(f"{t=}")
    r = e
    y = (N**t)%p
    print(f"{y=}")
    print(f"{r=}")
    x = a**((t-1)//2)
    x = x%p
    print(f"{x=}")
    b = (a*x*x)%p
    print(f"{b=}")
    x = (a*x)%p
    print(f"{x=}")
    i = 0
    while 1:
        if b == 1:
            return (x , p-x)
        
        m = 1
        while (b**(2**m))%p != 1:
            m+=1
        
        l = y**(2**(r-m-1))
        l = l%p
        y = (l*l)%p
        r = m
        x = (x*l)%p
        b = (b*y)%p

        print(f"{m=} {l=} {y=} {r=} {x=} {b=}")
        if i == 5:
            return None
        i+=1

def sqrt(a, m):
    if symbol_legandra(a, m)== -1:
        return None

    if m%4==3:
        k = (m-3)//4
        x = a**(k+1)
        x = x%m
        return (x, m-x)
    elif m%4==1:
        return tonnel_shenksa(a, m)

    return None

print(sqrt(61, 109))
