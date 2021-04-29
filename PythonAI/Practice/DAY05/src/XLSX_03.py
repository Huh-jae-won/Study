import openpyxl

filename = "../data/stats_100701.xlsx"

book = openpyxl.load_workbook(filename)
sheet = book.worksheets[0]

data = []
skip = 1
for row in sheet.rows:
    if skip>4 :
        data.append([row[0].value,row[sheet.max_column-2].value])
    skip+=1

data = sorted(data,key=lambda x:x[1],reverse=True)

for i in data:
    print("%-3s %-5d"%(i[0],i[1]))