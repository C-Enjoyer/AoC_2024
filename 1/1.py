from collections import Counter

path = 'input.txt'

l = []
r = []

with open(path, 'r') as file:
    for row in file:
        lNum, rNum = row.strip().split('   ')
        l.append(int(lNum))
        r.append(int(rNum))

def part1(l, r):
    """ part 1 """

    l.sort()
    r.sort()

    result = 0

    for num1, num2 in zip(l, r):
        result += abs(num1 - num2)

    return result

def part2(l, r):
    """ part 2 """

    rf = Counter(r)
    result = 0

    for num in l:
        result += num * rf[num]

    return result


print(part1(l, r))
print(part2(l, r))