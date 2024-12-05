from functools import cmp_to_key

path = 'input.txt'

r = []
u = []

with open(path, 'r') as file:
    for row in file:
        if len(row) < 3:
            continue
        elif row[2] == '|':
            num1, num2 = row.strip().split('|')
            r.append((int(num1), int(num2)))
        elif row[2] == ',':
            u.append([int(x) for x in row.strip().split(',')])


def applyRules(updates, rules):
    ok, nok = [], []
    notAllowedBefore = {}

    for k, v in rules:
        if k not in notAllowedBefore:
            notAllowedBefore[k] = [v]
        else:
            notAllowedBefore[k].append(v)

    for update in updates:
        isOk = True
        cur = [update[0]]
        for num in update[1:]:
            if num in notAllowedBefore:
                if any(x in notAllowedBefore[num] for x in cur):
                    isOk = False
                    break
            cur.append(num)
        if isOk:
            ok.append(update)
        else:
            nok.append(update)

    return ok, nok


def part1(updates):
    """ part 1 """

    result = 0

    for update in updates:
        result += update[len(update) // 2]

    return result


def part2(updates, rules):
    """ part 2 """

    result = 0

    for update in updates:
        update.sort(key=cmp_to_key(lambda x, y: -1 if (x, y) in rules else 1))
        result += update[len(update) // 2]

    return result


ok, nok = applyRules(u, r)
print(part1(ok))
print(part2(nok, r))
