def merge_the_tools(string, k):
    rpt = 1
    arr = []
    word = ''
    for i in range(len(string)):
        if rpt > k:
            arr.append(word)
            word = string[i]
            rpt = 1
        elif string[i] not in word:
            word += string[i]
        rpt += 1
    arr.append(word)
    print('\n'.join(arr))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
