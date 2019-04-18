#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : selenium168_new.py
# @Author: yu.jin
# @Date  : 2019-04-17
# @Desc  :

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import tkinter as tk
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Firefox()
driver.get("http://www.chehang168.com/")
time.sleep(0.1)
name = driver.find_element_by_name("uname")

name.send_keys("17816861605")
# name.send_keys("13732202517")
script = "Object.defineProperties(navigator,{webdriver:{get:() => false}});"
driver.execute_script(script)
driver.execute_script("window.navigator.webdriver")

# 定位滑块元素
source = driver.find_element_by_xpath("//*[@id='nc_1_n1z']")
# 点击
ActionChains(driver).click_and_hold(source).perform()
time.sleep(0.5)
# 移动
ActionChains(driver).move_by_offset(xoffset=250, yoffset=0).perform()
time.sleep(0.5)
# 释放滑块
ActionChains(driver).release().perform()
# TODO, 发送短信按钮点击
# TODO, 验证码填写框
# TODO, 登录按钮点击
# 确定登录成功
while driver.current_url != "http://www.chehang168.com/index.php?c=index&m=index":
    time.sleep(0.5)
    print(driver.current_url)
print(driver.current_url)
time.sleep(0.5)

# 品牌爬取
driver.get("http://www.chehang168.com/index.php?c=index&m=allBrands")
brand_urls = []
for i in range(25):
    # u"/html/body/div[4]/div/ul/li[*]/a[*]"
    brand_xpath = "/html/body/div[4]/div/ul/li[*]/a[%d]"%i
    brands = driver.find_elements_by_xpath(brand_xpath)
    for url in brands:
        brand_urls.append(url.get_attribute("href"))
# TODO, 品牌名称爬取
# TODO, 品牌链接与品牌名称 保存
#

# 系列爬取
series_urls = []
for brand_url in brand_urls:
    driver.get(brand_url)
    series_xpath = "/html/body/div[4]/div[1]/div[1]/div/div[2]/div/div[*]/ul/li[*]/a"
    series = driver.find_elements_by_xpath(series_xpath)
    for url in series:
        series_urls.append(url.get_attribute("href") + "&type=1")  # type=1 代表选中公司
# TODO, 系列名称爬取
# TODO, 系列链接与系列名称 保存
#

# 厂商链接爬取
company_urls = set()
for series_url in series_urls:
    driver.get(series_url)
    company_xpath = "/html/body/div[4]/div[1]/div[2]/ul[2]/li[*]/p[2]/a"
    company = driver.find_elements_by_xpath(company_xpath)
    for url in company:
        company_urls.add(url.get_attribute("href"))

# TODO, 经销商名称爬取
# TODO, 经销商链接与厂商名称 保存

# TODO, 经销商信息爬取
address = []
people_name = []
phone_number = []
for company_url in company_urls:
    driver.get(company_url)
    # TODO, 查看联系人 按钮点击
    driver.find_element_by_name("").click()
    # TODO, 经销商信息爬取
    address_xpath = ""
    address.append(driver.find_element_by_xpath(address_xpath))
    people_name_xpath = ""
    people_name.append(driver.find_element_by_xpath(people_name_xpath))
    phone_number_xpath = ""
    phone_number.append(driver.find_element_by_xpath(phone_number_xpath))



