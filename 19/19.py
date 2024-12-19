from functools import cache

path = 'input.txt'

t = set()
d = []

with open(path, 'r') as file:
    for row in file:
        if ',' in row:
            t = set(row.strip().split(', '))
        elif len(row) >= 2:
            d.append(row.strip())


def part1(towels, designs):
    """ part 1 """

    @cache
    def checkPossible(design):
        if len(design) == 0:
            return True

        for towel in towels:
            if not design.startswith(towel):
                continue
            if checkPossible(design[len(towel):]):
                return True

        return False

    result = 0
    for design in designs:
        if checkPossible(design):
            result += 1

    return result

    
def part2(towels, designs):
    """ part 2 """

    @cache
    def getAll(design):
        if len(design) == 0:
            return 1

        combinations  = 0

        for towel in towels:
            if not design.startswith(towel):
                continue
            combinations += getAll(design[len(towel):])

        return combinations

    result = 0

    for design in designs:
        result += getAll(design)

    return result


print(part1(t, d))
print(part2(t, d))
