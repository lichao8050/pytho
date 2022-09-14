# _*_ coding: utf-8 _*_
# @Time    : 2021/5/13 0013 23:15
# @Author  : LiChao
# @FileName: test_xinzenkehu.py
from base.base_util import BaseUtil
from pageobject.xinzenKehu_page import XinZenKeHu


class TestXinZenKeHu(BaseUtil):

    def test_xinzenkehu(self):
        '''新增客户'''

        xz_kh1 = XinZenKeHu(self.driver)
        xz_kh1.test_xz_kh(username='heqiangming', password='abc123456'
                          ,jtmc='中元建业集团',khdw='测试3号单位',qyfzr="钮双双")
