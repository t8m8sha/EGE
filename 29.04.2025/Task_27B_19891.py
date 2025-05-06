from math import dist
with open('27.19.B_20497.txt') as file:
    data = [list(map(float,i.split())) for i in file]


eps = 1
clusters =[]
while data:
    cluster = [data.pop()]
    for dot in cluster:
        for dot2 in data.copy():
            if dist(dot, dot2) < eps:
                cluster.append(dot2)
                data.remove(dot2)
    if len(cluster) > 10:
        clusters.append(cluster)
    centers = [centroid(cluster) for cluster in [cluster_B1, cluster_B2, cluster_B3, cluster_B4]]
    p_x = sum(center[0] for center in centers) / len(centers)
    p_y = sum(center[1] for center in centers) / len(centers)
    print(int(p_x * 10_000), int(p_y * 10_000))