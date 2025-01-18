with open('26_4604.txt') as file:
    N = int(file.readline())
    boxes = [int(i) for i in file]
boxes = sorted(boxes, reverse= True)

true_boxes_list = [boxes[0]]

for box in boxes:
    if true_boxes_list[-1] - box >= 3:
        true_boxes_list.append(box)

print(len(true_boxes_list),true_boxes_list[-1])