from openpyxl import Workbook
wb=Workbook()
ws=wb.active
ws["A1"]="Hello openpyxl"
wb.save("openpyxl_test.xlsx")