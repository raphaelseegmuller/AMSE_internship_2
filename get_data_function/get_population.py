import xlrd
import numpy as np


workbook = xlrd.open_workbook('estim-pop-dep-sexe-gca-1975-2020.xls')
SheetNameList = workbook.sheet_names()

mySheet = workbook.sheets()[1]

A = mySheet.col(7)[5:101]
B = []
for i in range(len(A)):
    B += [int(str(A[i])[7:-2])]
print(float(str(A[0])[7:]))
print(B)
