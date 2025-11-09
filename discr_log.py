BASE = 2
TARGET = 11
MOD = 37

MNOJITELI = [[2, 4], [3, 9]]


for mnojitel in MNOJITELI:
    razlozhenie_base = mnojitel[0]
    print(f"Множитель {razlozhenie_base}")

    power = int((MOD - 1) / razlozhenie_base)

    a = (TARGET ** power) % MOD

    print(f"{BASE}^({power}*X0) = {a}")

    if a == 1:
        x0 = 0
    else:
        for x in range(razlozhenie_base):
            if BASE ** (power * x) % MOD == a:
                x0 = x

    print(f"X0 = {x0}\n")

    second_mnoj = mnojitel[1]

    print(f"Множитель {second_mnoj}")
    power = int((MOD - 1) / second_mnoj)
    a = (TARGET ** power) % MOD
    print(f"{BASE}^({power}*X0 + {razlozhenie_base*power}*X1) = {a}")

    if x0 == 0:
        if a == 1:
            x1 = 0
        else:
            for x in range(second_mnoj):
                if BASE ** (razlozhenie_base*power * x) % MOD == a:
                    x1 = x
    else:
        x1 = (a - BASE ** (power * x0)) // BASE ** (power * razlozhenie_base * x0)

    print(f"X1 = {x1}\n")
