class Calculator(object):
    def power(self, n, p):
        if any(map(lambda x: (x < 0), [n, p])):
            raise ValueError('n and p should be non-negative')
        return n**p


myCalculator = Calculator()
T = int(input())
for i in range(T):
    n, p = map(int, input().split())
    try:
        ans = myCalculator.power(n, p)
        print(ans)
    except Exception as e:
        print(e)
