#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : selenium168_seller_muti_thread.py
# @Author: yu.jin
# @Date  : 2019-05-01
# @Desc  :


import time
import threading
import queue

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

from car168.databaseDemo import query_company_url_by_status, update_company_status_by_url
from car168.multi_thread_util import div_list


def main():
    options = webdriver.FirefoxProfile()
    options.set_preference('permissions.default.image', 2)
    driver = webdriver.Firefox(options)
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
    # name.send_keys("13843593401")

    name.send_keys("17685824346")

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
    # 发送验证码
    time.sleep(3)
    driver.find_element_by_id("sendCode").click()

    # 确定登录成功
    while driver.current_url != "http://www.chehang168.com/index.php?c=index&m=index":
        time.sleep(1)
        print(driver.current_url)
    print(driver.current_url)
    time.sleep(1)

    cookie = driver.get_cookies()
    print(cookie)
    print(type(cookie))

    finished_queue = queue.Queue()

    company_urls = query_company_url_by_status("TODO")
    company_urls_not_crawl = [url[0] for url in company_urls]
    company_urls_not_crawl_4 = div_list(company_urls_not_crawl, 15)

    t1 = [threading.Thread(target=get_seller_data, args=(cookie, urls, finished_queue)) for urls in company_urls_not_crawl_4]
    for t in t1:
        t.start()

    for t in t1:
        t.join()

    seller_data_set = set()

    while not finished_queue.empty():
        seller_data_set.add(finished_queue.get())

    for seller_data in seller_data_set:
        update_company_status_by_url(seller_data[0], seller_data[1], seller_data[2], "DONE")


def get_seller_data(cookies, company_urls_not_crawl, finished_queue):
    print("subprocss is ")
    options = webdriver.FirefoxProfile()
    options.set_preference('permissions.default.image', 2)
    driver = webdriver.Firefox(options)
    driver.get("http://www.chehang168.com/")

    time.sleep(2)
    for cookie in cookies:
        driver.add_cookie(cookie)
    time.sleep(30)
    try:
        for company_url in company_urls_not_crawl:
            driver.get(company_url)
            # 查看联系人 按钮点击
            driver.find_element_by_id("get_tels").click()
            # TODO, 经销商信息爬取
            address_xpath = "/html/body/div[4]/ul/li[4]"
            # TODO, 联系人拆分，姓名电话在一个元素里，可能有多个姓名电话
            contact_xpath = "/html/body/div[4]/ul/li[5]/div"
            finished_queue.put((driver.find_element_by_xpath(address_xpath).text, driver.find_element_by_xpath(contact_xpath).text, company_url))
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()




