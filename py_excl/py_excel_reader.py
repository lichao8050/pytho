# _*_ coding: utf-8 _*_
# @Time     : 2022/4/25 20:24
# @Author   : Mr_Li
# @FileName :
# 用代码读取Excel
from py_excl.read_excel import ExcelReader

excel = ExcelReader(r"G:\pytho\py_excl\test_excel.xlsx")
count = excel.get_case_count()
print(count)
excel.close_file()
# 循环遍历所有用例
for row in range(0, count): #  循环语句   row是变量  范围是0到count
    api_url = excel.get_url(row)
