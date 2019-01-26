#!/bin/python3
def bubble_sort(a):
    total_swaps = 0
    for i in range(len(a)):
        swaps = 0
        for j in range(len(a) - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swaps += 1
        total_swaps += swaps
        if swaps == 0:
            break
    # print(a, total_swaps)
    print("Array is sorted in {} swaps.".format(total_swaps))
    print("First Element: {}".format(a[0]))
    print("Last Element: {}".format(a[-1]))


n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
bubble_sort(a)
