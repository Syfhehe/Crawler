#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : selenium168_new.py
# @Author: yu.jin
# @Date  : 2019-04-17
# @Desc  :

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from car168.databaseDemo import insert_data_brand, insert_data_series, query_series_url_by_status, \
    update_series_status_by_url, insert_data_seller
import time
import re

driver = webdriver.Firefox()
driver.get("http://www.chehang168.com/")
time.sleep(0.1)
name = driver.find_element_by_name("uname")

# 金宇
# name.send_keys("17816861605")
# 李益均
# name.send_keys("13989470972")
# 李益均
# name.send_keys("15301718215")
# 沈一凡
# name.send_keys("13732202517")
# 金宇
# name.send_keys("15702154165")
# 桂佳佳
# name.send_keys("15618691822")
# 刘树
# name.send_keys("17721338625")
# 唐师兄
name.send_keys("15618932927")

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
    time.sleep(1)
    print(driver.current_url)
print(driver.current_url)
time.sleep(1)

# 品牌爬取
# driver.get("http://www.chehang168.com/index.php?c=index&m=allBrands")
# brand_urls = []
# for i in range(25):
#     # u"/html/body/div[4]/div/ul/li[*]/a[*]"
#     brand_xpath = "/html/body/div[4]/div/ul/li[*]/a[%d]"%i
#     brands = driver.find_elements_by_xpath(brand_xpath)
#     for url in brands:
#         brand_urls.append((url.text, url.get_attribute("href"), "TODO"))
#     # brand_file_path = "/Users/yu.jin/Downloads/chehang168_brand_0418.txt"
#     # with open(brand_file_path, "w") as f:  # 设置文件对象
#     #     brands_name_url = ["%s,%s" % (line[0], line[1]) + "\n" for line in brand_urls]
#     #     f.writelines(brands_name_url)
#
# insert_data_brand(brand_urls)

# TODO, 品牌链接与品牌名称 数据库保存


# 系列爬取
# series_urls = []
# for brand_url in brand_urls:
#     driver.get(brand_url[1])
#     series_xpath = "/html/body/div[4]/div[1]/div[1]/div/div[2]/div/div[*]/ul/li[*]/a"
#     series = driver.find_elements_by_xpath(series_xpath)
#     for url in series:
#         series_urls.append((url.text, url.get_attribute("href") + "&type=1", "TODO"))  # type=1 代表选中公司
#
#     # series_file_path = "/Users/yu.jin/Downloads/chehang168_series_0418.txt"
#     # with open(series_file_path, "w") as f:  # 设置文件对象
#     #     series_name_url = ["%s,%s" % (line[0], line[1]) + "\n" for line in series_urls]
#     #     f.writelines(series_name_url)
# insert_data_series(series_urls)

# TODO, 系列链接与系列名称 数据库保存
#

# http://www.chehang168.com/index.php?c=index&m=series&psid=6aaIm&type=1&pricetype=0&page=2

import numpy as np

series_urls_not_crawl = query_series_url_by_status("TODO")
series_urls_not_crawl = [url[0] for url in series_urls_not_crawl]
series_urls_crawl = set()

# series_file_path = "/Users/yu.jin/Downloads/chehang168_series_0418.txt"
# #
# series_urls = []
# with open(series_file_path, "r") as f:    #设置文件对象
#     urls = f.readlines()
#     for url in urls:
#         series_urls.append(url[:-1].split(",")[1])
#
# # 经销商链接爬取
flag = 0
company_urls = set()
for series_url in series_urls_not_crawl:
    # TODO, 页码爬取
    driver.get(series_url + '&pricetype=0&page=1')
    # company_xpath = "/html/body/div[4]/div[1]/div[2]/ul[2]/li[*]/p[3]/a"
    # company = driver.find_elements_by_xpath(company_xpath)

    last_page_number = 1
    try:
        link = driver.find_element_by_link_text(">>")

        if link:
            link = link.get_attribute("href")
            last_page_number = int(link[link.find("page=")+5:])
    except Exception as e:
        driver.get(series_url + '&pricetype=0&page=1')  # 链接加上页码
        if driver.current_url == 'http://www.chehang168.com/index.php?c=com&m=limitPage':
            flag = 1
            break
        company_xpath = "/html/body/div[4]/div[1]/div[2]/ul[2]/li[*]/p[3]/a"
        company_xpath2 = "/html/body/div[4]/div[1]/div[2]/ul[2]/li[*]/p[2]/a"
        company = driver.find_elements_by_xpath(company_xpath)
        for url in company:
            # print("%s, %s" % (url.text, url.get_attribute("href")))
            company_urls.add((url.text, url.get_attribute("href"), "TODO"))

        company2 = driver.find_elements_by_xpath(company_xpath2)
        for url in company2:
            # print("%s, %s" % (url.text, url.get_attribute("href")))
            company_urls.add((url.text, url.get_attribute("href"), "TODO"))

        series_urls_crawl.add(series_url)

    for page in range(last_page_number):
        driver.get(series_url + '&pricetype=0&page=' + "%s" % str(page+1))  # 链接加上页码
        if driver.current_url == 'http://www.chehang168.com/index.php?c=com&m=limitPage':
            flag = 1
            break
#
        company_xpath = "/html/body/div[4]/div[1]/div[2]/ul[2]/li[*]/p[3]/a"
        company_xpath2 = "/html/body/div[4]/div[1]/div[2]/ul[2]/li[*]/p[2]/a"
        company = driver.find_elements_by_xpath(company_xpath)
        for url in company:
            # print("%s, %s" % (url.text, url.get_attribute("href")))
            company_urls.add((url.text, url.get_attribute("href"), "TODO"))

        company2 = driver.find_elements_by_xpath(company_xpath2)
        for url in company2:
            # print("%s, %s" % (url.text, url.get_attribute("href")))
            company_urls.add((url.text, url.get_attribute("href"), "TODO"))

    if flag:
        series_urls_crawl.add(series_url)
        break
    else:
        series_urls_crawl.add(series_url)

for company in company_urls:
    print("%s, %s, %s" % (company[0], company[1], company[2]))

insert_data_seller(company_urls)


for url_crawl in series_urls_crawl:
    update_series_status_by_url(url_crawl, "DONE")



        # rand = np.random.random(1)
        # rand1 = rand[0] * 10 + 20
        # print(rand1)
        # time.sleep(rand1)

# company_file_path = "/Users/yu.jin/Downloads/chehang168_company_0418.csv"
# with open(company_file_path, "w") as f:  # 设置文件对象
#     company_name_url = ["%s,%s" % (line[0], line[1]) + "\n" for line in company_urls]
#     f.writelines(company_name_url)
#
# # TODO, 经销商名称爬取
# # TODO, 经销商链接与厂商名称 保存
#
# # TODO, 经销商信息爬取
# address = []
# people_name = []
# phone_number = []
# for company_url in company_urls:
#     driver.get(company_url)
#     # 查看联系人 按钮点击
#     driver.find_element_by_id("get_tels").click()
#     # TODO, 经销商信息爬取
#     address_xpath = ""
#     address.append(driver.find_element_by_xpath("/html/body/div[4]/ul/li[4]").text)
#     # TODO, 联系人拆分，姓名电话在一个元素里，可能有多个姓名电话
#     people_name_xpath = ""
#     people_name.append(driver.find_elements_by_xpath("/html/body/div[4]/ul/li[5]/div/p[*]"))
#     phone_number_xpath = ""
#     phone_number.append(driver.find_element_by_xpath(phone_number_xpath))



