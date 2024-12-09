path = 'input.txt'

l = []

with open(path, 'r') as file:
    for row in file:
        for c in row:
            l.append(c)


def part1(list):
    """ part 1 """

    mem = []

    for i, c in enumerate(list):
        num = int(c)
        if num == 0:
            continue

        if i % 2 == 0:
            app = str(i // 2)
            for i in range(num):
                mem.append(app)
        else:
            for i in range(num):
                mem.append('.')

    i = 0
    j = len(mem) - 1

    while i < j:
        if mem[i] == '.':
            while mem[j] == '.':
                j -= 1
            if j <= i:
                break

            mem[i] = mem[j]
            mem[j] = '.'
            j -= 1

        i += 1

    result = 0

    for i, c in enumerate(mem):
        if c == '.':
            break
        result += i * int(c)

    return result

def part2(list):
    """ part 2 """

    blocks = [] # [id, index, length]

    cnt = 0
    for i, c in enumerate(list):
        num = int(c)
        if num == 0:
            continue

        if i % 2 == 0:
            blocks.append([str(i // 2), cnt, num])
        else:
            blocks.append(['.', cnt, num])

        cnt += num

    j = len(blocks) - 1

    while j >= 0:
        rid, rindex, rlen = blocks[j]
        if rid != '.':
            for i in range(j):
                lid, lindex, llen = blocks[i]
                if lid != '.' or llen < rlen:
                    continue
                if llen == rlen:
                    blocks[i][0] = rid
                    blocks[j][0] = '.'
                    break
                else:
                    blocks[i][0] = rid
                    blocks[i][2] = rlen
                    blocks[j][0] = '.'
                    blocks.insert(i + 1, ['.', lindex + rlen, llen - rlen])
                    j += 1
                    break
        j -= 1

    result = 0

    for id, index, l in blocks:
        if id == '.':
            continue

        for i in range(l):
            result += (index + i) * int(id)

    return result


print(part1(l))
print(part2(l))
