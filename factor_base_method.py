from random import randint as ri

n = 319
b = (-1, 2, 3, 5, 7, 11, 13)
t = dict()

def get_vector(a):
    d = dict()
    for p in b:
        d[p] = 0

    while a != 1:
        for p in b:
            if a%p == 0:
                a = a//p
                d[p] += 1
                break
    else:
        return None
    
    


def gen_new_int():
    while 1:
        i = ri(1, n)
        o = i**2 % n
        print(i, o)
        for p in b:
            if o%p == 0:
                return i, o
        else: 
            o = (-o)%n
            for p in b:
                if o%p == 0:
                    return i, o
                

while len(t) < len(b)+1:
    i, o = gen_new_int()
    t[i] = o
print(t)