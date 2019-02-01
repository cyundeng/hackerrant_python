def check_subset(set_a, set_b):
    set_a -= set_b
    # print(set_a)
    return len(set_a) == 0


def check_subset2(set_a, set_b):
    return set_a.issubset(set_b)


def check_subset3(set_a, set_b):
    return not set_a.difference(set_b)


if __name__ == "__main__":
    results = []
    for i in range(int(input())):
        num_a = int(input())
        set_a = set(map(int, input().split(' ')))
        num_b = int(input())
        set_b = set(map(int, input().split(' ')))
        results.append(check_subset3(set_a, set_b))

    print('\n'.join(map(str, results)))
