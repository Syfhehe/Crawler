#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : selenium_test.py
# @Author: yu.jin
# @Date  : 2019-04-18
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

try:
    url = "https://www.qidian.com/rank/yuepiao"
    print("now visit url is %s" % url)
    driver.get(url)

    xpath = '//*[@id="rank-view-list"]/div/ul/li[*]/div[2]/h4/a'
    print("now xpath is %s" % xpath)
    # u"/html/body/div[4]/div/ul/li[1]/a[1]"
    brands = driver.find_elements_by_xpath(xpath)
    for url in brands:
        print(url.get_attribute("href"))
        print(url.text)


except Exception as e:
    print(e)
