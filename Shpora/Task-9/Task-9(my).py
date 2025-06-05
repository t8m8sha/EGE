with open('09_17550.txt') as file:
    nums = [list(map(int,i.split())) for i in file]
def f(nums):
    cnt = [nums.count(i) for i in nums]
    return cnt.count(3) == 3 and cnt.count(1) == 3
def f1(nums):
    nepov = [i for i in nums if nums.count(i) == 1]
    pov = [i for i in nums if nums.count(i) != 1]
    return sum(pov) ** 2 > sum(nepov) ** 2

cnt = 0
for i in nums:
    if f(i) and f1(i):
        cnt += 1
print(cnt)

