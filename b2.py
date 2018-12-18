from random import randint


def sum_algo(n):
    sum = 0
    for i in range(1, n+1):
        if randint(1, 2*i) <= i:
            sum += i

    return sum


def main():
    for i in range(100, 10000, 100):
        alg = sum_algo(i)
        exp = 0.25*i*(i+1)
        print(f'i: {i} sum_algo: {alg} expected: {exp} diff: {abs(exp-alg)*100 / alg:.2f}%')


if __name__ == '__main__':
    main()
