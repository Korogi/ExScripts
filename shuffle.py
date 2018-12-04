from random import randint


def shuffle(lst):
    n = (len(lst)+1) // 2
    l = [i for i in lst[:n]]
    r = [i for i in lst[n:]]

    i, j, m = 0, 0, 0
    for k in range(len(lst)):
        if (randint(0, 1) and i < n) or j >= len(r):  # if [0, 1, 1, 1, 0, 0, 1, 0, 1][m] == 0 or j >= n-1:
            lst[k] = l[i]
            i += 1
        else:
            lst[k] = r[j]
            j += 1
        # m += 1


def main():
    lst = [4, 3, 2, 7, 9, 1, 8, 5, 6]
    lst = [1, 2, 3, 4, 6, 7]
    shuffle(lst)
    print(lst)


if __name__ == '__main__':
    main()
