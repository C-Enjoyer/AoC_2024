from functools import cache
path = 'input.txt'

l = []

with open(path, 'r') as file:
    for row in file:
        for x in row.strip().split(' '):
            l.append(int(x))


@cache
def getCount(num, d):

    if d == 0:
        return 1

    d -= 1

    if num == 0:
        return getCount(1, d)

    strNum = str(num)
    n = len(strNum)

    if n % 2 == 0:
        half = n // 2
        return getCount(int(strNum[:half]), d) + getCount(int(strNum[half:]), d)

    return getCount(num * 2024, d)


def part1(list):
    """ part 1 """

    result = 0

    for x in list:
        result += getCount(x, 25)

    return result


def part2(list):
    """ part 2 """

    result = 0

    for x in list:
        result += getCount(x, 75)

    return result


print(part1(l))
print(part2(l))
