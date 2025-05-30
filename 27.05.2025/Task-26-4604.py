
with open('26_4604.txt') as file:
    N = int(file.readline())
    boxes = [int(i) for i in file]

boxes = sorted(boxes,reverse=True)
last = boxes[0]
cnt = 1

for box in boxes:
    if last - box >= 3:
        cnt += 1
        last = box

print(cnt,last)


