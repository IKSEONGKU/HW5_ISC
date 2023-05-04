import csv
f = open('q2.csv')
data = csv.reader(f)
header = next(data)

min_diff = 999
max_diff = 0
min_day = ''
max_day = ''

for row in data:
    diff = float(row[3]) - float(row[2])
    if diff < min_diff:
        min_diff = diff
        min_day = row[0]
    if diff > max_diff:
        max_diff = diff
        max_day = row[1]

print("*** Annual Temperature Report for Seoul in 2022 ***")
print(f"Day With the Largest Temperature Variation: {max_day}")
print(f"Maximum Temprature Difference: {max_diff}")
print(f"Day With the Smallest Temperature Variation: {min_day}")
print(f"Minimum Temprature Difference: {min_diff:0.2f}")

f.close()
