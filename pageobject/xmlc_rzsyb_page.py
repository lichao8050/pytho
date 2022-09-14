# _*_ coding: utf-8 _*_
# @Time    : 2021/5/30 0030 22:11
# @Author  : LiChao
# @FileName: xmlc_rzsyb_page.py
from selenium.webdriver.common.by import By

from base.base_page import BasePage

from time import sleep

from pageobject.login_page import LoginPage

'''项目流程'''
class XmLcPaGe(BasePage):

    '''页面元素'''
    xmlc_M = (By.XPATH, "//span[text()='項目流程']")
    xmlc_rzsyb = (By.XPATH, "//span[text()='軟裝事業部']")
    xmlc_xz = (By.XPATH, "//i[@class='el-icon-circle-plus']")
    # 方案配合项目新增
    faphxm_xmmc = (By.XPATH, "/html/body/section/div/section/"
                             "section/main/div/div[2]/div/div[2]/div/"
                             "form/div[1]/div[1]/div/div/div/input")
    faphxm_xmnr = (By.XPATH, "/html/body/section/div/section/section/"
                             "main/div/div[2]/div/div[2]/div/form/div[1]/"
                             "div[2]/div/div/div/div[2]/input")
    faphxm_xmnr1 = (By.XPATH, "//span[text()='精装样板间']")

    faphxm_sjs = (By.XPATH, "/html/body/section/div/section/section/main/"
                            "div/div[2]/div/div[2]/div/form/div[2]/div[1]/"
                            "div/div/div/div[1]/input")
    faphxm_sjs1 = (By.XPATH, "//span[text()='刘旭东']")
    faphxm_swjl = (By.XPATH, "/html/body/section/div/section/section/main/"
                             "div/div[2]/div/div[2]/div/form/div[2]/div[2]/"
                             "div/div/div/div/input")
    faphxm_swjl1 = (By.XPATH, "//span[text()='钟小乐']")
    faphxm_rzjd = (By.XPATH, "/html/body/section/div/section/section/main/"
                             "div/div[2]/div/div[2]/div/form/div[3]/div[1]/"
                             "div/div/div/div/div[1]/input")
    faphxm_rzjd1 = (By.XPATH, "//span[text()='深化方案阶段']")
    faphxm_sfzx = (By.XPATH, "/html/body/section/div/section/section/main/"
                             "div/div[2]/div/div[2]/div/form/div[3]/div[2]/"
                             "div/div/div/div[1]/input")
    faphxm_sfzx1 = (By.XPATH, "//span[text()='直委']")
    faphxm_htyg = (By.XPATH, "//input[@type='Number']")
    faphxm_bz = (By.XPATH, "//textarea[@placeholder='请填写备注']")
    faphxm_tj = (By.XPATH, "//span[text()='提交']")
    faphxm_qk = (By.XPATH, "//span[text()='清空']")

    '''页面动作'''
    def test_fzphxmxz(self,username, password,xm_mc,ht_yg,tx_bz):

        dl = LoginPage(self.driver)
        dl.logine_erp(username, password)

        sleep(1)
        self.click(XmLcPaGe.xmlc_M)
        self.click(XmLcPaGe.xmlc_rzsyb)
        self.click(XmLcPaGe.xmlc_xz)
        sleep(1)
        self.send_ks(XmLcPaGe.faphxm_xmmc,xm_mc)
        self.click(XmLcPaGe.faphxm_xmnr)
        sleep(1)
        self.click(XmLcPaGe.faphxm_xmnr1)
        self.click(XmLcPaGe.faphxm_sjs)
        sleep(1)
        self.click(XmLcPaGe.faphxm_sjs1)
        self.click(XmLcPaGe.faphxm_swjl)
        sleep(1)
        self.click(XmLcPaGe.faphxm_swjl1)
        self.click(XmLcPaGe.faphxm_rzjd)
        sleep(1)
        self.click(XmLcPaGe.faphxm_rzjd1)
        self.click(XmLcPaGe.faphxm_sfzx)
        sleep(1)
        self.click(XmLcPaGe.faphxm_sfzx1)
        self.send_ks(XmLcPaGe.faphxm_htyg,ht_yg)
        self.send_ks(XmLcPaGe.faphxm_bz,tx_bz)
        sleep(1)
        # 清空
        # self.click(XmLcPaGe.faphxm_qk)
        # 提交
        self.click(XmLcPaGe.faphxm_tj)






