#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : selenium_baidu.py
# @Author: yu.jin
# @Date  : 2019-04-17
# @Desc  :

# 目的测试 xpath

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import tkinter as tk
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Firefox()


top = tk.Tk()

L1 = tk.Label(top, text="输入url", width=20, height=5, padx=10, pady=10)
L1.pack(side=tk.LEFT)
E1 = tk.Entry(top, bd=5)
E1.pack(side=tk.RIGHT)

L2 = tk.Label(top, text="输入正则表达式", width=20, height=5, padx=10, pady=10)
L2.pack(side=tk.LEFT)
E2 = tk.Entry(top, bd=5)
E2.pack(side=tk.RIGHT)


def access_url():
    try:
        # title = driver.find_element_by_xpath("/html/body/div[2]/div/ul/li[2]/a/text()")
        # cookie_list = driver.get_cookies()
        # print(cookie_list)
        # for cookie in cookie_list:
        #     driver.add_cookie(cookie)

        print("now visit url is %s" % E1.get())
        driver.get(E1.get())

        print("now xpath is %s" % E2.get())
        # u"/html/body/div[4]/div/ul/li[1]/a[1]"
        brands = driver.find_elements_by_xpath(E2.get())
        # driver.find_element_by_css_selector()

        # driver.find_element_by_xpath(
        #     u"(.//*[normalize-space(text()) and normalize-space(.)='更多'])[3]/following::img[1]").click()
        # driver.find_element_by_link_text(u"车商首页").click()
        # time.sleep(0.5)
        # driver.find_element_by_id("get_tels").click()
        # time.sleep(0.5)
        # html = driver.page_source
        # time.sleep(0.5)
        for url in brands:
            print(url.get_attribute("href"))

    except Exception as e:
        print(e)
        #这里定位失败后的刷新按钮，重新加载滑块模块
        # driver.find_element_by_xpath("//div[@id='havana_nco']/div/span/a").click()
        # print(e)

    #退出浏览器，如果浏览器打开多个窗口，可以使用driver.close()关闭当前窗口而不是关闭浏览器
    # driver.quit()


button = tk.Button(top, text="按钮", command=access_url, width=20, height=5, padx=20, pady=20)
button.pack()

top.mainloop()