with open('26_4205.txt') as file:
    N = int(file.readline())
    trees = [list(map(int,i.split())) for i in file]

trees = sorted(trees,key=lambda x:(-x[0],x[1]))
ans =[]
for tree1,tree2 in zip(trees,trees[1:]):
    if tree1[0] == tree2[0]:
        ans.append([tree2[1] - tree1[1] - 1,tree1[0]])

print(max(ans))