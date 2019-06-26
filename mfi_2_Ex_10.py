from random import randint


def omega():
    omega = []
    for i in range(1, 11):
        for j in range(1, 11):
            for k in range(1, 11):
                omega.append((i, j, k))

    return omega


def ex_one_a(bool_test, calc=None, n=1000000):
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


print(f"omega: {len(omega())}")
print("E1: ", end="")
ex_one_a(lambda sample: len(list(filter(lambda x: x <= 3, sample))) == 3, (3/10)**3)
print("E2: ", end="")
ex_one_a(lambda sample: sample[0] <= 3 and sample[1] >= 4 and sample[2] >= 4, (3/10)*(7/10)*(7/10))
print("E3: ", end="")
ex_one_a(lambda sample: sample[0] <= 3, 0.3)
print("E1 or E2: ", end="")
ex_one_c(lambda sample: len(list(filter(lambda x: x <= 3, sample))) == 3,
         lambda sample: sample[0] <= 3 and sample[1] >= 4 and sample[2] >= 4, (3/10)**3 + (3/10)*(7/10)*(7/10))
print("E2 or E3: ", end="")
ex_one_a(lambda sample: sample[0] <= 3 or sample[1] <= 3 or sample[2] <= 3, 1 - (7/10) ** 3)
