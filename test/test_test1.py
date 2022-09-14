# _*_ coding: utf-8 _*_
# @Time     : 2021/10/18 12:15
# @Author   : Mr_Li
# @FileName : test_test1.py
from base.base_util import BaseUtil
# 数据驱动ddt导包
from ddt import ddt, data, unpack
# yaml文件导包
from ddt import file_data
from pageobject.test_page import LoginPage1


@ddt
class TestLogin(BaseUtil):
    """用户登录"""

    @file_data("E:\\A999\\yaml\\test_test.yaml")
    def test_login(self, **kwargs):
        username = kwargs.get('username')
        password = kwargs.get('password')
        value1 = kwargs.get('value1')
        index = kwargs.get('index')
        login = LoginPage1(self.driver)
        login.login_erp(username, password, value1, index)
