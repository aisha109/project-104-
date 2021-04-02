import csv

with open('height-weight.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)

newData=[]
for i in range(len(file_data)):
	n_num = file_data[i][1]
	newData.append(n_num)

n = len(newData)
newData.sort()



if n % 2 == 0:
    #getting the first number
	median1 = float(newData[n//2])
    #getting the second number
	median2 = float(newData[n//2 - 1])
    #getting mean of those numbers
	median = (median1 + median2)/2
else:
	median = newData[n//2]

print("Median is: " + str(median))
