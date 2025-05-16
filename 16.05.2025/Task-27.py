from math import dist

def centroid(cluster):
    distance = []
    for dot in cluster:
        sum_dist = 0
        for dot2 in cluster:
            sum_dist += dist(dot,dot2)
        distance.append([sum_dist,dot])
    return min(distance)[1]


with open('27_A_18884.txt') as file:
    cluster1 = []
    cluster2 = []
    for i in file:
        x, y = map(float, i.split())
        if x > 40:
            cluster1.append([x,y])
        elif x < 40:
            cluster2.append([x,y])
centers = [centroid(cluster) for cluster in [cluster1,cluster2]]
px = sum(center[0] for center in centers) / len(centers)
py = sum(center[1] for center in centers) / len(centers)

print(int(px),int(py))