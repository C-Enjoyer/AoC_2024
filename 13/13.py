import math
path = 'input.txt'

l = []

with open(path, 'r') as file:
    i = 0
    for row in file:
        if i == 0:
            button = [(0, 0), (0, 0), (0, 0)]
            numbers = [int(part.split('+')[1]) for part in row.strip().split(',')]
            button[0] = (numbers[0], numbers[1])
        elif i == 1:
            numbers = [int(part.split('+')[1]) for part in row.strip().split(',')]
            button[1] = (numbers[0], numbers[1])
        elif i == 2:
            numbers = [int(part.split('=')[1]) for part in row.strip().split(',')]
            button[2] = (numbers[0], numbers[1])
            l.append(button)

        i += 1
        if i >= 4:
            i = 0


def part1(list):
    """ part 1 """

    result = 0

    for (ax, ay), (bx, by), (px, py) in list:

        a, ra = divmod(px * by - py * bx, ax * by - ay * bx)
        b, rb = divmod(py * ax - px * ay, ax * by - ay * bx)

        if ra == 0 and rb == 0:
            result += 3 * a + b

    return result


def part2(list):
    """ part 2 """

    result = 0

    for (ax, ay), (bx, by), (px, py) in list:
        px += 10000000000000
        py += 10000000000000

        a, ra = divmod(px * by - py * bx, ax * by - ay * bx)
        b, rb = divmod(py * ax - px * ay, ax * by - ay * bx)

        if ra == 0 and rb == 0:
            result += 3 * a + b

    return result


print(part1(l))
print(part2(l))
