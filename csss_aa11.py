# _*_ coding: utf-8 _*_
# @Time    : 2021/8/22 0022 22:39
# @Author  : LiChao
# @FileName: csss_aa11.py
import unittest

import yaml
from base.base_util import BaseUtil
from pageobject.login_page import LoginPage
# 数据驱动ddt导包
from ddt import ddt,data,unpack
# yaml文件导包
from ddt import file_data

@ddt
class TestLogin(unittest.TestCase):

    @file_data("E:\pytho\\test\\test_1.yaml")
    def test_login(self,**kwargs):

        print(kwargs)


if __name__ == '__main__':
    unittest.main()