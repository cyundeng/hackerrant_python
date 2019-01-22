def diff(list_1, list_2):
    set_1 = set(list_1)
    set_2 = set(list_2)
    diff_1 = set_1.difference(set_2)
    diff_2 = set_2.difference(set_1)
    set_3 = diff_1.union(diff_2)
    # print(set_3)
    arr = []
    arr.extend(set_3)
    arr.sort()
    print('\n'.join(map(str, arr)))


if __name__ == "__main__":
    len_1 = int(input())
    list_1 = list(map(int, input().split()))

    len_2 = int(input())
    list_2 = list(map(int, input().split()))

    diff(list_1, list_2)
