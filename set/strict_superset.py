def is_superset(set_a, set_b):
    sym_diff = set_a.symmetric_difference(set_b)
    return sym_diff.issubset(set_a)


def is_superset2(set_a, set_b):
    return set_a > set_b


if __name__ == "__main__":
    result = True
    set_a = set(map(int, input().split(' ')))
    # print(all(set_a > set(input().split()) for _ in range(int(input()))))

    for i in range(int(input())):
        set_b = set(map(int, input().split(' ')))
        if not is_superset2(set_a, set_b):
            result = False
            break
    print(result)
