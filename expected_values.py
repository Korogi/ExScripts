from random import randint


def algo1(a):
    count = 0
    count2 = 0
    for i in range(1, a+1):
        if randint(1, a+1) <= i:
            count += 1
            for j in range(i, a+1):
                count2 += 1

    total = sum([(i/a)*(a-i+1) for i in range(1, a+1)])
    print(f'rnd <= i: {count} times in range: {a}\n'
          f'amount printed: {count2} expected value: {total:.2f}\n'
          f'discrepancy to amount printed: {abs(total - count2)*100/count2:.2f}%\n')


def main():
    for i in range(100, 1000, 50):
        algo1(i)


if __name__ == '__main__':
    main()
