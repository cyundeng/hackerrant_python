if __name__ == '__main__':
    countries = set()
    n = int(input())
    for i in range(n):
        country = input()
        countries.add(country)

    print(len(countries))
