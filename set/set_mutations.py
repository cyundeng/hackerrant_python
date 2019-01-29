def operation(set_a, cmd, set_b):
    if cmd == 'intersection_update':
        set_a &= set_b
    elif cmd == 'update':
        set_a |= set_b
    elif cmd == 'symmetric_difference_update':
        set_a ^= set_b
    elif cmd == 'difference_update':
        set_a -= set_b


if __name__ == "__main__":
    len_1 = int(input())
    set_a = set(map(int, input().split()))

    num_cmd = int(input())
    for i in range(num_cmd):
        cmd, len_2 = input().split(' ')
        set_b = set(map(int, input().split(' ')))
        operation(set_a, cmd, set_b)
        # print(set_a)

    print(sum(set_a))
