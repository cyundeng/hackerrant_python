if __name__ == "__main__":
    # a, b, m = map(int, (input(), input(), input()))
    a, b, m = [int(input()) for _ in range(3)]
    p = a ** b
    r = p % m
    print(p, r, sep='\n')
