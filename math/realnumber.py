import cmath


def polar(z):
    print(abs(z))
    print(cmath.phase(z))


def polar2(z):
    print(*cmath.polar(z), sep='\n')


if __name__ == "__main__":
    z = complex(input())
    polar2(z)
