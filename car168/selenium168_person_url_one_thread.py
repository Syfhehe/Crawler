#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : selenium168_person_url_one_thread.py
# @Author: yu.jin
# @Date  : 2019-05-07
# @Desc  :

import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

from car168.databaseDemo import query_series_person_url_by_status, \
    update_series_person_status_by_url, insert_data_person

options = webdriver.FirefoxProfile()
options.set_preference('permissions.default.image', 2)
driver = webdriver.Firefox(options)
driver.get("http://www.chehang168.com/")
time.sleep(0.1)
name = driver.find_element_by_name("uname")

name.send_keys("13766722942")

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
time.sleep(2)
driver.find_element_by_id("sendCode").click()


# TODO, 发送短信按钮点击
# TODO, 验证码填写框
# TODO, 登录按钮点击
# 确定登录成功
while driver.current_url != "http://www.chehang168.com/index.php?c=index&m=index":
    time.sleep(1)
    print(driver.current_url)
print(driver.current_url)
time.sleep(1)

series_urls_not_crawl = query_series_person_url_by_status("TODO")
series_urls_not_crawl = [url[0] for url in series_urls_not_crawl]
series_urls_crawl = set()

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

        # 展厅ICON
        # icon = driver.find_element_by_class_name("ic zt")

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
        break
    else:
        series_urls_crawl.add(series_url)

for company in company_urls:
    print("%s, %s, %s" % (company[0], company[1], company[2]))

insert_data_person(company_urls)


for url_crawl in series_urls_crawl:
    update_series_person_status_by_url(url_crawl, "DONE")
