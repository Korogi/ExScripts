

def test_permutation(A):
    current_push_count = 0
    current_push_element = A[1]

    current_pop_count = 1

    for a in A:
        if a > current_push_element:
            current_push_element = a
            current_push_count += a - current_push_count

        else:
            current_pop_count += 1

        if a < current_push_count - current_pop_count:
            return False

        print("PUSH count: ", current_push_count)
        print("POP count: ", current_pop_count)
        print()


def main():
    Astrich = [3, 2, 4, 1, 8, 9, 10, 7, 6, 5]  # true
    Astrich = [5, 4, 3, 10, 9, 8, 7, 6, 1, 2]  # false
    Astrich = [3, 2, 4, 1, 8, 9, 10, 5, 6, 7]  # false
    Astrich = [7, 8, 9, 10, 6, 5, 4, 3, 2, 1]  # true

    print("\n", test_permutation(Astrich))


if __name__ == '__main__':
    main()
