
from openpyxl import Workbook
from openpyxl.styles import PatternFill
import time
import json

print("Inputting data to excel file...")

CG = []
CMC = []

with open('CG.txt', 'r') as f:
    CG = json.loads(f.read())
with open('CMC.txt', 'r') as f:
    CMC = json.loads(f.read())

book = Workbook()
sheet = book.active
sheet.title = "CG and CMC"

sheet['A1'] = "Name"
sheet['B1'] = "CG Time"
sheet['C1'] = "CMC Time"

sheet['A1'].fill = PatternFill(start_color="55C7CE", fill_type = "solid")
sheet['B1'].fill = PatternFill(start_color="BBFF99", fill_type = "solid")
sheet['C1'].fill = PatternFill(start_color="AAC7CC", fill_type = "solid")

sheet.column_dimensions['A'].width = 25
sheet.column_dimensions['B'].width = 10
sheet.column_dimensions['C'].width = 10

for i in range(len(CG)):
    name = CG[i]["name"]
    sheet.cell(row=i+2, column=1).value = name
    sheet.cell(row=i+2, column=2).value = CG[i]["time"]
    for c in CMC:
        if(c["name"] == name):
            sheet.cell(row=i+2, column=3).value = c["time"]

book.save("sample.xlsx")

print("Done.")





