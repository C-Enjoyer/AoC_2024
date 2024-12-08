path = 'input.txt'

l = []

with open(path, 'r') as file:
    for row in file:
        res, nums = row.strip().split(': ')
        l.append((int(res), [int(x) for x in nums.split(' ')]))


def IsPossible(nums, res, doCon = False, curRes = 0):
    if len(nums) == 0:
        return curRes == res

    if IsPossible(nums[1:], res, doCon, curRes + nums[0]):
        return True
    if IsPossible(nums[1:], res, doCon, curRes * nums[0]):
        return True
    if doCon and IsPossible(nums[1:], res, doCon, int(str(curRes) + str(nums[0]))):
        return True

    return False


def part1(list):
    """ part 1 """

    result = 0

    for res, nums in list:
        if IsPossible(nums, res):
            result += res

    return result
    
def part2(list):
    """ part 2 """

    result = 0

    for res, nums in list:
        if IsPossible(nums, res, True):
            result += res

    return result


print(part1(l))
print(part2(l))
