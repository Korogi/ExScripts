
def chain(lst):
    return [(i, (3*i + 7) % 16) for i in lst]


def probe(lst, h):
    probed = [(0, 0)] * 16

    for element in lst:
        i = 0

        while probed[int(h(element, i))][0] != 0:
            i += 1
            print(h(element, i))
        probed[int(h(element, i))] = (element, i)

    return sum([probed[i][1] for i in range(len(probed))]), probed


def linear_probe(lst):
    return probe(lst, lambda k, i: (((3*k + 7) % 16) + i) % 16)


def quadratic_probe(lst):
    c_1 = c_2 = 0.5
    return probe(lst, lambda k, i: (((3*k + 7) % 16) + c_1 * i + c_2 * i * i) % 16)


def double_probe(lst):
    return probe(lst, lambda k, i: (((3*k + 7) % 16) + i*(7-2*(k % 4))) % 16)


def main():
    lst = [44, 12, 23, 88, 71, 11, 94, 39, 20, 5, 16]
    func_lst = [chain, linear_probe, quadratic_probe, double_probe]
    for func in func_lst:
        print(f'{func.__name__}' + " " * (max([len(str(x)) for x in func_lst])-len(str(func))) + ":", *func(lst))


if __name__ == '__main__':
    main()
