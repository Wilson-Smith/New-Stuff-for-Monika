#from openpyxl import load_workbook

#workbook = load_workbook(filename="sample.xlsx")
#sheet = workbook.active
#print(sheet[A])


import pandas as pd


""" name_of_file =  "sample.xlsx"
data = pd.read_excel(name_of_file)

required_colum_name = "A"
print(data[required_colum_name]) """

import numpy as np
file_loc = "sample.xlsx"
df = pd.read_excel(file_loc, index_col=None, na_values=['NA'], usecols="A,C:AA")
print(df)



#df = pd.read_excel('sample.xlsx')

#df_sheet_index = pd.read_excel('sample.xlsx', sheet_name=1)

#print(df_sheet_index)