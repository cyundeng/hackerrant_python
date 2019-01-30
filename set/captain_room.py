def find_captain(numbers):
    rooms = set(numbers)
    groups = {}
    for num in numbers:
        if num in groups:
            groups[num] += 1
            rooms.discard(num)
        else:
            groups[num] = 1

    # print(rooms, groups)
    return rooms.pop()


# This is too slow
def find_captain2(numbers):
    rooms = set(numbers)
    for room in rooms:
        numbers.remove(room)

    rooms2 = set(numbers)
    return rooms.difference(rooms2).pop()


if __name__ == "__main__":
    group_size = int(input())
    numbers = list(map(int, input().split()))
    print(find_captain(numbers))
