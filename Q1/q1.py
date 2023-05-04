import csv
f = open('q1.csv')
data = csv.reader(f)
header = next(data)
i = 0
av_temp = av_min_temp = av_max_temp = 0
for row in data:
    i += 1
    av_temp += float(row[1])
    av_min_temp += float(row[2])
    av_max_temp += float(row[3])
    print(row)

print("*** Annual Temperature Report for Seoul in 2022 ***")

print(f"Average Temperature: {av_temp:0.2f} Celsius")
print(f"Average Temperature: {av_min_temp:0.2f} Celsius")
print(f"Average Temperature: {av_max_temp:0.2f} Celsius")





f.close()
