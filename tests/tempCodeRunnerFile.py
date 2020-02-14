import xlsxwriter
import json

workbook = xlsxwriter.Workbook('data.xlsx')
worksheet = workbook.add_worksheet()

with open('tests/data.json') as f:
    file = json.load(f)

for item in file:
    print(item)