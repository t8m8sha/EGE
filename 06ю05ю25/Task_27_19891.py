from math import dist
with open('27.19.A_20497.txt') as file:
    data = [list(map(float,i.split())) for i in file]

eps = 0.45
clusters = []
while data:
    cluster= [data.pop()]
    for dot in cluster:
        for dot2 in data.copy():
            if dist(dot,dot2) < eps:
                cluster.append(dot2)
                data.remove(dot2)
    if len(cluster) > 10:
        clusters.append(cluster)

print([len(cluster) for cluster in clusters])