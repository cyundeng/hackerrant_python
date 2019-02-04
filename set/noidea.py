def happy_score(numbers, a, b):
    score = 0
    for i in numbers:
        if i in a:
            score += 1
        elif i in b:
            score -= 1
    return score


if __name__ == "__main__":
    result = True
    n, m = map(int, input().split(' '))
    numbers = list(map(int, input().split(' ')))
    set_a = set(map(int, input().split(' ')))
    set_b = set(map(int, input().split(' ')))

    print(happy_score(numbers, set_a, set_b))
