# _*_ coding: utf-8 _*_
# @Time    : 2021/5/19 0019 22:13
# @Author  : Mr_Li
# @FileName: yyshenpi_swht_page.py
from pywinauto.keyboard import send_keys
from pywinauto.mouse import click
from selenium.webdriver.common.by import By
from base.base_page import BasePage
from time import sleep
from pageobject.login_page import LoginPage


class MatrixCollegeCourse(BasePage):
    """矩阵学院"""
    # ht_gl = (By.XPATH, "//*[@id='1260220714821226498']/div/span")
    ht_gl = (By.XPATH, "//span[text()='矩阵学院']")
    xy_zx = (By.XPATH, "//span[text()='學院中心']")
    kc_gl = (By.XPATH, "//a[text()='课程管理']")
    yy_sy = (By.XPATH, "//span[text()='新增课程']")
    yy_dw = (By.XPATH, "/html/body/section/div/section/section/"
                       "main/div/div[2]/div/form/div/div/div[3]/"
                       "div[1]/div/div/div/div[1]/input")
    yy_dw1 = (By.XPATH, "//span[text()='财务部']")
    jj_cd = (By.XPATH, "/html/body/section/div/section/section/"
                       "main/div/div[2]/div/form/div/div/div[3]/"
                       "div[2]/div/div/div/span[5]")
    wj_lx = (By.XPATH, "/html/body/section/div/section/section/"
                       "main/div/div[2]/div/form/div/div/div[5]/"
                       "div/div/div/div/div/div[1]/input")
    wj_lx1 = (By.XPATH, "/html/body/section/div/section/section/"
                        "main/div/div[2]/div/form/div/div/div[5]/"
                        "div/div/div/div/div/div[2]/div[1]/div[1]/ul/li[2]")
    jy_df = (By.XPATH, "/html/body/section/div/section/section/main/div/"
                       "div[2]/div/form/div/div/div[6]/div[1]/"
                       "div/div/div/div[1]/input")
    jy_df1 = (By.XPATH, "//span[text()='采购用印测试1']")
    xm_mc = (By.XPATH, "/html/body/section/div/section/section/"
                       "main/div/div[2]/div/form/div/div/div[6]/"
                       "div[2]/div/div/div/div/div[1]/input")
    xm_mc1 = (By.XPATH, "//span[text()='采购项目新增测试3万以下']")
    xm_je = (By.XPATH, "//input[@placeholder='请输入项目金额']")

    sf_gl = (By.XPATH, "/html/body/section/div/section/section/"
                       "main/div/div[2]/div/form/div/div/div[9]/"
                       "div[1]/div/div/div/div/label[1]/span[1]/span")
    yz_lx = (By.XPATH, "/html/body/section/div/section/section/main/"
                       "div/div[2]/div/form/div/div/div[11]/div[1]/"
                       "div/div/div/div/div[2]/input")
    yz_lx1 = (By.XPATH, "//span[text()='合同专用章']")
    yz_gs = (By.XPATH, "/html/body/section/div/section/section/"
                       "main/div/div[2]/div/form/div/div/div[11]/"
                       "div[2]/div/div/div/div[1]/input")
    yz_gs1 = (By.XPATH, "/html/body/section/div/section/section/"
                        "main/div/div[2]/div/form/div/div/div[11]/"
                        "div[2]/div/div/div/div[2]/div[1]/div[1]/ul/li[1]")
    yy_xz = (By.XPATH, "/html/body/section/div/section/section/main/div/"
                       "div[2]/div/form/div/div/div[6]/div[1]/"
                       "div/div/div/div[1]/input")
    wj_fs = (By.XPATH, "/html/body/section/div/section/section/main/"
                       "div/div[2]/div/form/div/div/div[12]/"
                       "div[1]/div/div/div/input")
    yy_sl = (By.XPATH, "/html/body/section/div/section/section/"
                       "main/div/div[2]/div/form/div/div/div[12]/"
                       "div[2]/div/div/div/input")
    qk_sm = (By.XPATH, "/html/body/section/div/section/section/main/"
                       "div/div[2]/div/form/div/div/div[13]/div/"
                       "div/div/div/div/textarea")
    wj_sc = (By.XPATH, "//input[@name='file']")
    tj_sp = (By.XPATH, "/html/body/section/div/section/section/"
                       "main/div/div[2]/div/div[2]/div[1]/button[1]")
    tj_spqd = (By.XPATH, "//span[text()='确定']")

    def test_matrix_college(self, username, password):
        login = LoginPage(self.driver)  # 登录
        login.login_erp(username, password)  # 输入用户名、密码

        sleep(1)
        self.click(MatrixCollegeCourse.ht_gl)
        sleep(1)
        self.click(MatrixCollegeCourse.xy_zx)
        self.click(MatrixCollegeCourse.kc_gl)
        sleep(1)
        self.click(MatrixCollegeCourse.yy_sy)
        sleep(5)
        '''self.send_ks(MatrixCollegeCourse.yy_sy, value1)
        self.click(MatrixCollegeCourse.yy_dw)
        sleep(1)
        self.click(MatrixCollegeCourse.yy_dw1)
        self.click(MatrixCollegeCourse.jj_cd)
        self.click(MatrixCollegeCourse.wj_lx)
        sleep(1)
        self.click(MatrixCollegeCourse.wj_lx1)
        self.send_ks(MatrixCollegeCourse.jy_df, '采购')
        sleep(1)
        self.click(YyShenPiSwHtPage.jy_df1)
        self.click(YyShenPiSwHtPage.xm_mc)
        sleep(1)
        self.click(YyShenPiSwHtPage.xm_mc1)
        self.send_ks(YyShenPiSwHtPage.xm_je, value2)
        self.click(YyShenPiSwHtPage.sf_gl)
        self.click(YyShenPiSwHtPage.yz_lx)
        sleep(1)
        self.click(YyShenPiSwHtPage.yz_lx1)
        self.click(YyShenPiSwHtPage.yz_gs)
        sleep(1)
        self.click(YyShenPiSwHtPage.yz_gs1)
        self.send_ks(YyShenPiSwHtPage.wj_fs, value3)
        self.send_ks(YyShenPiSwHtPage.yy_sl, value4)
        self.send_ks(YyShenPiSwHtPage.qk_sm, value5)
        sleep(1)
        self.send_ks(YyShenPiSwHtPage.wj_sc, value6)
        self.send_ks(YyShenPiSwHtPage.wj_sc, value7)
        self.send_ks(YyShenPiSwHtPage.wj_sc, value8)
        sleep(3)
        self.click(YyShenPiSwHtPage.tj_sp)
        sleep(3)
        self.jp_qd()'''
