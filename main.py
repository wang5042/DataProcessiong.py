import pandas as pd
import xlwt
file = open('19-Dec-2022_1.csv')
lines = file.readlines()
i = 0
list_sample = []
list_FITC = []
list_Texas = []
#print(lines[1])

for line in lines:
    print(i)
    print(line)
    if i%4 ==1:
        list_sample.append(lines[i].strip(','))
    elif i%4 ==2:
        list_FITC.append(lines[i].strip('> ,Median : FITC-A= '))
    elif i%4 ==3:
        list_Texas.append(lines[i].strip('> ,Median : PE-Texas Red-A= '))
    i = i+1
#print(list_sample)
#print(list_Texas)
#print(list_FITC)
a = 0
while a< len(list_sample):
    list_sample[a] = list_sample[a].split('_',3)[2]
    list_FITC[a] = list_FITC[a].split(',',2)[0]
    list_Texas[a] = list_Texas[a].split(',',2)[0]
    a = a + 1
#print(list_sample)
#print(list_Texas)
#print(list_FITC)
list0 = []
list0.append(list_sample)
list0.append(list_FITC)
list0.append(list_Texas)
book = xlwt.Workbook()
savepath = 'Data_clean.xls'
sheet = book.add_sheet('Data')
col = ("No","FITC_YFP","Texas_RFP")
for i in range(0,3):
    sheet.write(0,i,col[i])  #Each column name
for i in range(0,3):
        # print("The %d line" %(i+1))
    list_i = list0[i]# Save each list information
    for j in range(len(list_i)):
            sheet.write( j + 1, i, list_i[j])
    book.save(savepath) #Save



