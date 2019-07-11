import csv
from collections import defaultdict

#edit the csv file to append header

def editFile(datafile):

    with open(datafile,'r') as f:
        r = csv.reader(f)
        data = [line for line in r]
    with open('file.csv','w') as f:
        w = csv.writer(f)
        w.writerow(['customerId','contractId','geozone','teamcode','projectcode','buildduration'])
        w.writerows(data)
    return 'file.csv'



def result(filename):

    with open(filename, 'r') as f:
        reader = csv.reader(f)
        next(reader)   #Skip header
        for row in reader:
            unique_CustID_contractID[row[1]].add(row[0])
            unique_CustID_geozone[row[2]].add(row[0])
            avg_bd_geozone[row[2]].add(row[5])
            list_CustID_geozone[row[2]].add(row[0])

    print("The number of unique customerId for each contractId.")
    for i in unique_CustID_contractID.items():
        print(i[0],  len(i[1]))

    print("The number of unique customerId for each geozone.")
    for i in unique_CustID_geozone.items():
        print(i[0], len(i[1]))

    print("The average buildduration for each geozone.")
    for i in avg_bd_geozone.items():
        k = list(i[1])
        num_list = [int(j.strip('s')) for j in k]

        avg = sum(num_list)/len(num_list)

        print(i[0], avg)

    print("The list of unique customerId for each geozone.")
    for i in list_CustID_geozone.items():
        print(i[0], list(i[1]))

if __name__ =="__main__":
    datafile = 'data.csv'
    resultfile = editFile(datafile)

    unique_CustID_contractID = defaultdict(set)
    unique_CustID_geozone = defaultdict(set)
    avg_bd_geozone = defaultdict(set)
    list_CustID_geozone = defaultdict(set)
    result(resultfile)
