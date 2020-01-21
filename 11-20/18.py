#Find the maximum total from top to bottom moving to adjacent numbers on the row below of the triangle in "18.txt"

import time
start = time.time()

# get data into a list of rows
with open('18.txt') as infile:
    data = []
    for line in infile:
        intlist = [(int(num)) for num in line.split()]
        data.append(intlist)

def max_total(data):
    if len(data) == 1:
        print('Answer is', data[0][0])
        print('Elapsed time:', (time.time() - start)*1000, 'milliseconds')
    else:
        return max_total(change_last_row(data))

def change_last_row(data):
    height = len(data)
    data[height -2] = [data[height-2][index] + max(data[height-1][index], data[height-1][index + 1]) for index in range(len(data[height-2]))]
    data.pop()
    return data
    
max_total(data)
#answer is 1074