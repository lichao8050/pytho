# _*_ coding: utf-8 _*_
# @Time     : 2022/4/25 20:24
# @Author   : Mr_Li
# @FileName :
# Excel 读取为用例对象
from openpyxl import load_workbook

excel = load_workbook("test_excel.xlsx")
sheet = excel.worksheets[0]
print(sheet.cell(2, 1).value)


class ExcelReader:
    '''不是针对普通Excel操作，专门针对测试用例表的  读、写'''

    def __init__(self, excel_path):
        self.start_row = 5
        self.excel_path = excel_path
        self.excel_file = load_workbook(excel_path)
        self.sheet_1 = self.excel_file.worksheets[0]
