import csv
data = []
a = 1
f = csv.reader(open("transfers.csv"), delimiter=",")
for row in data:
    if a == 1:
        data.append(row)
        a = a+1
    else:
        if(len(row[5])) == 0:
            row[5] = str('name')
        else:
            row[5] = str('row[5]')
        if(len(row[8])) == 0:
            row[8] = 'null'
        if(len(row[9])) == 0:
            row[9] = 'USD'
        if (len(row[10])) == 0:
            row[10] = 'USD'
writer = csv.writer(open("transfer_data_cleaned.csv", "w+", newline=''))
for row in data:
    writer.writerow(row)
print(writer)
#read file
#for row in csv.reader(open("transfer_data_cleaned.csv"), delimiter=","):
 #   data.append(row)
#for row in data:
 #   print(row)

file = open("transfer_data_cleaned.csv", "r", encoding="utf_8")
data = file.readlines()
for d in data[:4701]:
    print(d, end="")
file.close()

