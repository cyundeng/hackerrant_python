if __name__ == '__main__':
    a = int(input())
    set_a = set(map(int, input().split()))
    b = int(input())
    set_b = set(map(int, input().split()))
    set_a = set_a & set_b
    # print(set_a)
    print(len(set_a))
