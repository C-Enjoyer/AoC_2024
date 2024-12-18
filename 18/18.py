import sys
from heapq import heappush, heappop

path = 'input.txt'

l = []

with open(path, 'r') as file:
    for row in file:
        xp, yp = row.strip().split(',')
        l.append((int(xp), int(yp)))


def findBestPath(corrupted):
    leny = 70 + 1
    lenx = 70 + 1
    start = (0, 0)
    end = (lenx - 1, leny - 1)

    q = []
    heappush(q, (0, (0, 0)))

    visited = dict()
    visited[start] = 0

    source = dict()
    source[start] = None

    while q:
        length, pos = heappop(q)
        x, y = pos

        if pos == end:
            break

        length += 1

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            next = (x + dx, y + dy)
            nextx, nexty = next
            if not (0 <= nextx < lenx and 0 <= nexty < leny):
                continue
            if next in corrupted:
                continue
            if next in visited and visited[next] <= length:
                continue

            heappush(q, (length, next))
            visited[next] = length
            source[next] = pos

    if end not in visited:
        return -1

    path = [end]
    while source[path[-1]] is not None:
        path.append(source[path[-1]])

    return len(path) - 1


def part1(list):
    """ part 1 """

    return findBestPath(list[:1024])


def part2(list):
    """ part 2 """

    for i in range(1024, len(list)):
        if findBestPath(list[:i + 1]) == -1:
            return str(list[i][0]) + "," + str(list[i][1])

    return "-1,-1"


print(part1(l))
print(part2(l))
