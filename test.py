
import xlrd

data = xlrd.open_workbook('openMe.xls')

table = data.sheet_by_index(0)

table.row_values(0)
