import re
import sys

def minion_game2(word):
    vowels = 'AEIOU'
    stu = {}
    kevin = {}

    for i in range(len(word)):
        if word[i] in vowels:
            get_substring2(word, i, kevin)
        else:
            get_substring2(word, i, stu)

    # print(kevin)
    # print(stu)
    kevin_score = sum(list(kevin.values()))
    stu_score = sum(list(stu.values()))
    if kevin_score == stu_score:
        print('Draw')
    elif kevin_score > stu_score:
        print('Kevin {}'.format(kevin_score))
    else:
        print('Stuart {}'.format(stu_score))

def get_substring2(word, i, game_dict):
    for j in range(i+1, len(word)+1):
        frag = word[i:j]
        if not frag in game_dict:
            game_dict[frag] = find_all(word, frag)
   

def find_all(word, frag):
    pattern = r'(?={})'.format(frag)
    # print(pattern)
    return len(re.findall(pattern, word))
    

def minion_game(word):
    vowels = 'AEIOU'

    kevin_score = stu_score = 0

    for i in range(len(word)):
        if word[i] in vowels:
            kevin_score += len(word) - i
        else:
            stu_score += len(word) - i

    if kevin_score == stu_score:
        print('Draw')
    elif kevin_score > stu_score:
        print('Kevin {}'.format(kevin_score))
    else:
        print('Stuart {}'.format(stu_score))


if __name__ == '__main__':
    s = input()
    minion_game(s)