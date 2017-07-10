#!usr/bin/env python
# -*- coding:utf-8 -*-

from selenium import webdriver

class Open_Url():

    def __init__(self,url_goal = "http://hd.ggcj.com"):
        self.url = url_goal
        # self.drive = webdriver.Chrome()   #此处注意chrome webdriver的版本与chrome版本对应的问题

        # profile = webdriver.FirefoxProfile()
        # profile.assume_untrusted_cert_issuer = True
        # accept_untrusted_certs = True
        self.drive = webdriver.Firefox()

        # self.drive = webdriver.Ie()

        self.drive.get(self.url)
        self.drive.maximize_window()
        # self.drive.set_window_size(480,800)

    def exe_jscript(self,js = "window.open('https://www.baidu.com');"):
        self.drive.execute_script(js)


if __name__ == "__main__":
    test_case = Open_Url()
    test_case.exe_jscript()