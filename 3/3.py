import re

path = 'input.txt'

l = []

with open(path, 'r') as file:
    for row in file:
        l.append(row.strip())


def getMulPairs(str):
    pairs = []
    pat = r"mul\((?P<num1>\d+),(?P<num2>\d+)\)"
    for match in re.finditer(pat, str):
        pairs.append((int(match.group('num1')), int(match.group('num2'))))

    return pairs


def part1(list):
    """ part 1 """
    result = 0
    pairs = []

    for line in list:
        pairs += getMulPairs(line)

    for pair in pairs:
        result += pair[0] * pair[1]

    return result


def part2(list):
    """ part 2 """
    result = 0
    pat = r"(mul\(\d+,\d+\))|(do\(\))|(don't\(\))"
    pairs = []

    enabled = True

    for line in list:
        for match in re.findall(pat, line):
            if match[0]:
                if enabled:
                    pairs += getMulPairs(match[0])
            elif match[1]:
                enabled = True
            elif match[2]:
                enabled = False

    for pair in pairs:
        result += pair[0] * pair[1]

    return result


print(part1(l))
print(part2(l))
