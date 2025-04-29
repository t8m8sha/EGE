

with open('27_B_17882.txt') as file:
    cluster1 = []
    cluster2 = []
    cluster3 = []
    for i in file:
        x,y = map(float,i.split())
        if x < 1:
            cluster1.append([x,y])
        else:
            cluster2.append([x,y])

