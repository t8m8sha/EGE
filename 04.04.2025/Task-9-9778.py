def f1 (nums):
    cnt = [nums.count(i) for i in nums]
    return cnt.count(2) == 2  and cnt.count(1) == 5
def f2 (nums):
    nepov = [i for i in nums if nums.count(i) == 1]
    pov = [i for i in nums if nums.count(i) != 1]
    return (pov) < sum(nepov)/len(nepov)





with open("09_9778.txt") as file:
    data = [list(map(int, i.split())) for i in file]
cnt = 0
for i in data:
    if f1(i) and f2(i):
        cnt += 1
print(cnt)
