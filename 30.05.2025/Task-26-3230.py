with open('26_3230.txt') as file:
    N = int(file.readline())
    trees = [list(map(int,i.split())) for i in file]

trees = sorted(trees, key=lambda x:(-x[0], x[1]))
ans =[]
for tree1,tree2 in zip(trees,trees[1:]):
    if tree1[0] == tree2[0]:
        if tree2[1] - tree1[1] - 1 ==11:
            print(tree2[0])
        break