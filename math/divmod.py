def divmod_func(a, b):
    div = divmod(a, b)
    print(div[0], div[1], div, sep='\n')


if __name__ == "__main__":
    a = int(input())
    b = int(input())
    divmod_func(a, b)
