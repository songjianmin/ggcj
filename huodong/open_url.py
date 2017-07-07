#!usr/bin/env python
# -*- coding:utf-8 -*-

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