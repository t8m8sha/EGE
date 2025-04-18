from itertools import permutations, combinations


def f1(nums):
    return max(nums) < sum(nums) - max(nums)

def f2(nums):
    for i in permutations(nums):
        if sum(i[:2]) == sum(i[2:]):
            return True
    return False

def f3(nums):
    for i in combinations(nums,2):
        if sum(i) == sum(num) - sum(i):
            return True
    return False


with open('9_4589.txt') as file:
    data = [list(map(int,i.split())) for i in file]
cnt = 0
for i in data:
    if f1(i) and f2(i):
        cnt += 1
print(cnt)


