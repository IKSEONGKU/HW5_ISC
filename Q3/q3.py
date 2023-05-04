import csv
f = open('q3.csv',encoding='UTF-8')
data = csv.reader(f)
header = next(data)

line_list = []
pass_list = []

for row in data:
    sum = int(row[2])+int(row[3])
    if row[1] not in line_list:
        line_list.append(row[1])
        pass_list.append(sum)
    else:
        i = line_list.index(row[1])
        pass_list[i] += sum

print(pass_list)
fir_max = max(pass_list)
fir_buis = pass_list.index(max(pass_list)) + 1
line_list.pop(fir_buis-1)
pass_list.pop(fir_buis-1)
sec_max = max(pass_list)
sec_buis = pass_list.index(max(pass_list)) + 1

fir_min = min(pass_list)
fir_leas = pass_list.index(min(pass_list)) + 1
line_list.pop(fir_leas-1)
pass_list.pop(fir_leas-1)

sec_min = min(pass_list)
sec_leas = pass_list.index(min(pass_list)) + 1



print("*** Subway Report for Seoul on March 2023 ***")
print(f"1st Busiest Line: Line {fir_buis} ({fir_max})")
print(f"2st Busiest Line: Line {sec_buis} ({sec_max})")
print(f"1st Least Line: Line {fir_leas} ({fir_min})")
print(f"2st Least Line: Line {sec_leas} ({sec_min})")


f.close()
