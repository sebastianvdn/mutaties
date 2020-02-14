import xlsxwriter
import json

workbook = xlsxwriter.Workbook('data.xlsx')
worksheet = workbook.add_worksheet()

bold = workbook.add_format({'bold': True})

headers = [
    'policy', 'comment', 'admin', 'gpo', 'date'
]

with open('tests/data.json') as f:
    policies = json.load(f)

first_row = 0
for header in headers:
    col = headers.index(header)
    worksheet.write(first_row, col, header, bold)

row = 1
for policy in policies:
    for _key, _value in policy.items():
        col = headers.index(_key)
        worksheet.write(row, col, _value)

    row += 1

workbook.close()