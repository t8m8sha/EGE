with open('9_9832.txt') as file:
    nums = [list(map(int,i.split()))for i in file]

def f(nums):
    cnt = [nums.count(i) for i in nums]
    return  cnt.count(2) == 4 and cnt.count(1) == 3

def f1(nums):
    return nums.count(max(nums)) == 1
for i in nums:
    if f(i) and f1(i):
        print(sum(i))
        break