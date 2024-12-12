path = 'input.txt'

g = []

with open(path, 'r') as file:
    for row in file:
        g.append([x for x in row.strip()])


def getAreas(grid):
    m = len(g)
    n = len(g[0])

    def getArea(r, c, element, seen):
        if not (0 <= r < m and 0 <= c < n):
            return seen
        if grid[r][c] != element:
            return seen
        if (r, c) in seen:
            return seen

        seen.add((r, c))

        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            seen = getArea(r + dr, c + dc, element, seen)

        return seen

    areas = []
    visited = set()

    for r in range(m):
        for c in range(n):
            if (r, c) in visited:
                continue
            visited.add((r, c))
            area = getArea(r, c, grid[r][c], set())
            visited.update(area)
            areas.append((grid[r][c], area))

    return areas


def part1(grid, areas):
    """ part 1 """
    m = len(g)
    n = len(g[0])

    def getOutline(area):

        element, coords = area
        result = 0

        for r, c in coords:
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                curR = r + dr
                curC = c + dc

                if not (0 <= curR < m and 0 <= curC < n):
                    result += 1
                elif grid[curR][curC] != element:
                    result += 1

        return result

    result = 0

    for area in areas:
        _, coords = area
        result += getOutline(area) * len(coords)

    return result


def part2(grid, areas):
    """ part 2 """
    m = len(g)
    n = len(g[0])

    def getSides(area):

        element, coords = area
        result = 0
        outlineCoords = dict()

        for r, c in coords:
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):

                curR = r + dr
                curC = c + dc

                if not (0 <= curR < m and 0 <= curC < n) or grid[curR][curC] != element:

                    if (curR, curC) in outlineCoords and (dr, dc) in outlineCoords[(curR, curC)]:
                        continue

                    result += 1

                    if (curR, curC) not in outlineCoords:
                        outlineCoords[(curR, curC)] = [(dr, dc)]
                    else:
                        outlineCoords[(curR, curC)].append((dr, dc))

                    nr, nc = r, c
                    while 1:
                        nr += abs(dc)
                        nc += abs(dr)
                        if not (0 <= nr < m and 0 <= nc < n) or grid[nr][nc] != element:
                            break

                        outr = nr + dr
                        outc = nc + dc
                        if (0 <= curR < m and 0 <= curC < n) and grid[outr][outc] == element:
                            break

                        if (outr, outc) not in outlineCoords:
                            outlineCoords[(outr, outc)] = [(dr, dc)]
                        else:
                            outlineCoords[(outr, outc)].append((dr, dc))

                    nr, nc = r, c
                    while 1:
                        nr -= abs(dc)
                        nc -= abs(dr)
                        if not (0 <= nr < m and 0 <= nc < n) or grid[nr][nc] != element:
                            break

                        outr = nr + dr
                        outc = nc + dc
                        if (0 <= curR < m and 0 <= curC < n) and grid[outr][outc] == element:
                            break

                        if (outr, outc) not in outlineCoords:
                            outlineCoords[(outr, outc)] = [(dr, dc)]
                        else:
                            outlineCoords[(outr, outc)].append((dr, dc))

        return result

    result = 0

    for area in areas:
        _, coords = area
        result += getSides(area) * len(coords)

    return result


a = getAreas(g)

print(part1(g, a))
print(part2(g, a))
