from itertools import permutations, combinations



with open('9_12918.txt') as file:
    data = [list(map(int, i.split())) for i in file]
cnt = 0

def f1(nums):
    for i in permutations(nums):
        if nums.count('0') == 2 or nums.count('1') == 2 or nums.count('2') == 2 or nums.count('3') == 2 or nums.count('4') == 2 or nums.count('5') == 2 or nums.count('6') or nums.count('7') == 2 or nums.count('8') == 2 or nums.count('9') == 2 or nums.count('0') == 2:
            return True
        return False

def f2(nums):
    chisl = max(nums)
    if num.count(chisl) == 0