if __name__ == "__main__":
    # a, b, m = map(int, (input(), input(), input()))
    a, b, c, d = (int(input()) for _ in range(4))
    print(a ** b + c ** d)
