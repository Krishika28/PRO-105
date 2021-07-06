import math, csv

with open('data.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)


data = file_data[0]

def mean(data):
    n= len(data)
    total =0
    for x in data:
        total += int(x)

    mean = total / n
    return mean

list= []
for number in data:
    q = int(number) - mean(data)
    q = 2*q
    list.append(q)


sum = 0
for i in list:
    sum =sum + i

result = sum/ (len(data)-1)
std_deviation = math.sqrt(result)


print(std_deviation)