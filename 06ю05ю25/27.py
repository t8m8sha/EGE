def dist(dot1,dot2):
    return max(abs(dot1[0] - dot2[0]),abs(dot1[1] - dot2[1]))

def centroid(cluster):
    dists = []
    for dot in cluster:
        sum_dist = 0
        for dot2 in cluster:
            sum_dist += dist(dot,dot2)
        dists.append([sum_dist,dot])
    return min(dists)[1]
with open('27.3.A_19891.txt') as file:
    cluster_A1 = []
    cluster_A2 = []
    for i in file:
        x,y = map(float,i.split())
        if x<3:
            cluster_A1.append([x,y])
        else:
            cluster_A2.append([x,y])

centers = [centroid(cluster) for cluster in [cluster_A1,cluster_A2]]
p_x = sum(center[0] for center in centers) / len(centers)
p_y = sum(center[1] for center in centers) / len(centers)
print(int(p_x * 10_000), int(p_y * 10_000))