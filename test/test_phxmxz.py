# _*_ coding: utf-8 _*_
# @Time    : 2021/5/30 0030 23:05
# @Author  : LiChao
# @FileName: test_phxmxz.py
from base.base_util import BaseUtil
from pageobject.xmlc_rzsyb_page import XmLcPaGe

class TestPhXmXz(BaseUtil):

    def test_phxmxz(self):

        phxmxz = XmLcPaGe(self.driver)
        phxmxz.test_fzphxmxz(username='heqiangming', password='abc123456',
                             xm_mc='方案配合项目新增测试@1',ht_yg=999999,
                             tx_bz='这是用于测试的一段文字，检查备注填写内容@#！123')