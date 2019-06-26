from random import randint, shuffle
from math import factorial


def omega():
    omega = []
    for i in range(1, 11):
        for j in range(1, 11):
            for k in range(1, 11):
                omega.append((i, j, k))

    return omega


def ex_one_b(bool_test, calc=None, n=1000000):
    hit = 0

    for _ in range(n):
        if bool_test([randint(1, 10) for _ in range(3)]):
            hit += 1

    print(f"simulation: {hit/n}, calc: {calc}")


def ex_one_c(bool_test_1, bool_test_2, calc=None, n=1000000):
    hit = 0

    for _ in range(n):
        sample = [randint(1, 10) for _ in range(3)]
        if bool_test_1(sample) or bool_test_2(sample):
            hit += 1

    print(f"simulation: {hit/n}, calc: {calc}")


def ex_two(n=1000000):
    def choose():
        markets = [0] * 20 + [1] * 10
        stores = []

        for i in range(6):
            rand = randint(0, 29-i)
            stores.append(markets[rand])
            del markets[rand]

        return stores

    def calc():
        comb = lambda n, k: factorial(n)/(factorial(k)*factorial(n-k))
        return 1 - sum([comb(6, k)*(factorial(24)/factorial(30))*(factorial(20)/factorial(20-6+k))*
                        (factorial(10)/factorial(10-k)) for k in range(3)])

    success = 0

    for _ in range(n):
        sample = choose()
        success += sum(sample) >= 3

    print(f"simulation: {success / n} calc: {calc()}")


def calc_2():
    a = [30-i for i in range(6)]
    b = [20-i for i in range(6)]
    mult = 1

    for x, y in zip(b, a):
        mult *= x/y

    print(mult)


ex_two()

"""print(f"omega: {len(omega())}")
print("E1: ", end="")
ex_one_b(lambda sample: len(list(filter(lambda x: x <= 3, sample))) == 3, (3 / 10) ** 3)
print("E2: ", end="")
ex_one_b(lambda sample: sample[0] <= 3 and sample[1] >= 4 and sample[2] >= 4, (3 / 10) * (7 / 10) * (7 / 10))
print("E3: ", end="")
ex_one_b(lambda sample: sample[0] <= 3, 0.3)
print("E1 or E2: ", end="")
ex_one_c(lambda sample: len(list(filter(lambda x: x <= 3, sample))) == 3,
         lambda sample: sample[0] <= 3 and sample[1] >= 4 and sample[2] >= 4, (3/10)**3 + (3/10)*(7/10)*(7/10))
print("E2 or E3: ", end="")
ex_one_b(lambda sample: sample[0] <= 3 or sample[1] <= 3 or sample[2] <= 3, 1 - (7 / 10) ** 3)
"""