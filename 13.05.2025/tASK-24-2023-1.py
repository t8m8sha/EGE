with open('24_9845.txt') as file:
    data = file.readline()
for i in "ABC":
    data = data.replace(i,'B')
for i in '89':
    data = data.replace(i,'1')
for i in "ABC89":
    data = data.replace(i," ")
data = data.split()
print(len(max(data,key=len)))
