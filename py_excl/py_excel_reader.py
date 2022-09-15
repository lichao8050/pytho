# _*_ coding: utf-8 _*_
# @Time     : 2022/4/25 20:24
# @Author   : Mr_Li
# @FileName :
# 用代码读取Excel
from py_excl.read_excel import ExcelReader
import requests

excel = ExcelReader(r"G:\pytho\py_excl\test_excel.xlsx")
count = excel.get_case_count()
print(count)
excel.close_file()
# 循环遍历所有用例
for row in range(0, count): #  循环语句   row是变量  范围是0到count
    api_case_name = excel.get_test_case_name(row) # 读取用例名字
    api_method = excel.get_method(row) # 读取用例请求方式
    api_url = excel.get_url(row) # 读取用例请求URL
    api_params = excel.get_headers(row) # 读取用例请求数据
    api_data = excel.get_test_data(row) # 读取用例请求数据
    print(api_case_name, api_method)
    if api_method == 'get':
        res = requests.get(
            url=api_url,
            params=eval(api_params)  # 此处参数类型不是字符串，所以用eval转换为字典类型
        )
        print(res.json())
    if api_method == 'post':
        requests.post()