with open('26_3230.txt') as file:
    N = int(file.readline())
    chairs = [list(map(int,i.split())) for i in file]

chairs = sorted(chairs, key=lambda x:(-x[0], x[1]))
ans =[]
for chair1,chair2 in zip(chairs,chairs[1:]):
    if chair1[0] == chair2[0]:
        if chair2[1] - chair1[1] - 1 == 2:
            print(chair1[0],chair1[1]+1)
        break