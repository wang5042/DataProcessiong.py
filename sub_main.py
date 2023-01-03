import pandas as pd
import xlwt
file = pd.read_csv('Data_clean.csv')
#print(file)
file = file.T
file.to_excel('Data_clean_preview.xls',header=False)