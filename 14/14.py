path = 'input.txt'

l = []

with open(path, 'r') as file:
    for row in file:
        parts = row.strip().split()
        p = tuple(map(int, parts[0].split('=')[1].split(',')))
        v = tuple(map(int, parts[1].split('=')[1].split(',')))
        l.append([p, v])

def part1(list):
    """ part 1 """

    seconds = 100
    xlen, ylen = 101, 103

    q1, q2, q3, q4 = 0, 0, 0, 0

    for p, v in list:
        x = (p[0] + v[0] * seconds - xlen) % xlen
        y = (p[1] + v[1] * seconds - ylen) % ylen

        hx = xlen // 2
        hy = ylen // 2

        if x < hx:
            if y < hy:
                q1 += 1
            elif y > hy:
                q2 += 1
        elif x > hx:
            if y < hy:
                q3 += 1
            elif y > hy:
                q4 += 1

    return q1 * q2 * q3 * q4


    
def part2(list):
    """ part 2 """

    xlen, ylen = 101, 103

    def doMove():
        for i in range(len(list)):
            x = list[i][0][0] + list[i][1][0]
            y = list[i][0][1] + list[i][1][1]

            if x >= xlen:
                x -= xlen
            elif x < 0:
                x += xlen

            if y >= ylen:
                y -= ylen
            elif y < 0:
                y += ylen

            list[i][0] = (x, y)

    def getLargestStructure(grid):
        seen = set()

        def dfs(x, y):
            if not (0 <= x < xlen and 0 <= y < ylen):
                return 0
            if (x, y) in seen:
                return 0
            if grid[y][x] == '.':
                return 0

            seen.add((x, y))

            cnt = 1
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    cnt += dfs(x + dx, y + dy)

            return cnt

        best = 0
        for y in range(ylen):
            for x in range(xlen):
                if grid[y][x] != '.' and (x, y) not in seen:
                    best = max(dfs(x, y), best)

        return best

    for seconds in range(100000):
        doMove()
        grid = [['.'] * xlen for _ in range(ylen)]
        for p, _ in list:
            grid[p[1]][p[0]] = '#'

        if getLargestStructure(grid) >= 100:
            return seconds + 1

    return -1


print(part1(l))
print(part2(l))
