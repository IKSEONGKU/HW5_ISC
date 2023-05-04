import csv
f = open('q4.csv')
data = csv.reader(f)
header = next(data)
b_list = ['','','','']
b_pass = [0,0,0,0]

l_list = ['','','','']
l_pass = [9999999,9999999,9999999,9999999]


for row in data:
    sum = int(row[2])+int(row[3])
    if row[0] == '1호선':
        if b_pass[0] < sum:
            b_list[0] = row[1]
            b_pass[0] = sum
        elif l_pass[0] > sum:
            l_list[0] = row[1]
            l_pass[0] = sum
    
    elif row[0] == '2호선':
        if b_pass[1] < sum:
            b_list[1] = row[1]
            b_pass[1] = sum
        if l_pass[1] > sum:
            l_list[1] = row[1]
            l_pass[1] = sum
        
    elif row[0] == '3호선':
        if b_pass[2] < sum:
            b_list[2] = row[1]
            b_pass[2] = sum
        if l_pass[2] > sum:
            l_list[2] = row[1]
            l_pass[2] = sum
        
    else:
        if b_pass[3] < sum:
            b_list[3] = row[1]
            b_pass[3] = sum
        if l_pass[3] > sum:
            l_list[3] = row[1]
            l_pass[3] = sum
    


for i in range(4):
        print(f"Line {i+1}:")
        print(f"Busiest Station : {b_list[i]} ({b_pass[i]})")
        print(f"Least used Station : {l_list[i]} ({l_pass[i]})\n")
