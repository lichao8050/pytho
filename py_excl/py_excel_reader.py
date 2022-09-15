# _*_ coding: utf-8 _*_
# @Time     : 2022/4/25 20:24
# @Author   : Mr_Li
# @FileName :
# 用代码读取Excel
from py_excl.read_excel import  ExcelReader

excel = ExcelReader(r"G:\pytho\py_excl\test_excel.xlsx")
count = excel.get_case_count()
excel.close_file()