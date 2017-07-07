#!usr/bin/env python
# -*- coding:utf-8 -*-

from selenium import webdriver
import time
from huodong_mysql import use_mysql
from get_log import Common_logger
import logging

class active_month():

    def __init__(self,url_goal = "http://hd.ggcj.com"):
        self.url = url_goal

    #初始化浏览器
    def chrome_browser(self):
        self.drive = webdriver.Chrome()

    def firefox_browser(self):
        # profile = webdriver.FirefoxProfile()
        # profile.assume_untrusted_cert_issuer = True
        # accept_untrusted_certs = True
        self.drive = webdriver.Firefox()
        # pass

    def ie_browser(self):
        self.drive = webdriver.Ie()

    def open_url(self):
        #打开url
        # url_goal = "http://hd.ggcj.com"
        self.drive.get(self.url)

    def adjust_browser(self):
        #浏览器最大化
        self.drive.maximize_window()
        # chrome_drive.set_window_size(480,800)

    def exe_jscript(self):
        js = "window.open('https://www.baidu.com');"
        self.drive.execute_script(js)

    def click_logolink(self):
        active_handle = self.drive.current_window_handle
        self.drive.find_element_by_class_name('f_logo').click()
        # self.exe_jscript()
        time.sleep(5)
        handles=self.drive.window_handles
        for handle in handles:
            if handle != active_handle:
                print ("切换至handle窗口...",handle)
                self.drive.switch_to_window(handle)
                print ("close current handle")
                self.drive.close()
            # else:
            #     self.drive.switch_to_window(active_handle)
        self.drive.switch_to_window(active_handle)

    def test_login_page(self):
        self.drive.find_element_by_link_text('登录').click()
        time.sleep(2)
        self.drive.switch_to_frame("loginIFrame")

        self.drive.find_element_by_id('username').send_keys('20735')
        self.drive.find_element_by_id('password').send_keys('qqqqqq111')
        self.drive.find_element_by_class_name("login_btn").click()

        self.drive.switch_to_default_content()
        self.drive.refresh()

    def test_hd_page(self):
        rank_list = []
        allrank_sql = []
        out_log = Common_logger(self.__class__.__name__, self.__class__.__name__,
                                s_path_log='E:\\Python-project\\Selenium\\ggcj\\huodong',
                                i_level_log=logging.DEBUG)
        try:
            test_mysql = use_mysql(hostname="183.131.6.183",portno=4987,username="test_ggcj",
                                   pwd="test_ggcj_2013",db="ggcj_gift_statistics")
            allrank_sql = test_mysql.select_sql()
            test_mysql.close_sql()
        except:
            out_log.info(r"数据库连接失败！")

        try:
            self.drive.find_element_by_id("zong_b").click()
            self.drive.find_element_by_class_name("jp_btn").click()
            self.drive.find_element_by_xpath('//*[@id="my_jp"]/span/a').click()
            for i in range(1,11):
                rank_list.append(int(self.drive.find_element_by_xpath(r'//*[@id="s10"]/dl['+str(i)+r']/dd/span/span/em').text))
        except:
            print ("获取网页榜单数据失败")

        # for i in range(10):
        #     print ([rank_list[i],allrank_sql[i]])

        if rank_list == allrank_sql and (rank_list !=[] or allrank_sql !=[]):
            print ("榜单数据与数据一致")
            out_log.info(r"榜单数据ok")
            # for each in rank_list:
            #     print (each)
        else:
            out_log.info(r"榜单数据错误")

    def close_browser(self):
        self.drive.quit()

if __name__ == "__main__":
    june_active = active_month()
    june_active.chrome_browser()
    june_active.open_url()
    june_active.adjust_browser()
    june_active.click_logolink()
    june_active.test_login_page()
    june_active.test_hd_page()
    # june_active.close_browser()
    # june_active.exe_jscript()
