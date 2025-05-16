with open('24_3792.txt') as file:
    data = file.readline()
    data = data.replace('E',' ')
    data = data.replace('D',' ')


data = data.split()
print (len(max(data,key=len)))