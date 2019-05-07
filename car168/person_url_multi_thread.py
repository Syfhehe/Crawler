import queue
import threading
import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

from car168.databaseDemo import insert_data_brand, insert_data_series, query_series_person_url_by_status, \
    update_series_person_status_by_url, insert_data_person
from car168.multi_thread_util import div_list

def main():
    driver = webdriver.Firefox()
    driver.get("http://www.chehang168.com/")
    time.sleep(0.1)
    name = driver.find_element_by_name("uname")

    # 金宇
    name.send_keys("13766116462")
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
    # name.send_keys("15618932927")

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
    # TODO, 验证码填写框
    # TODO, 登录按钮点击
    # 确定登录成功
    while driver.current_url != "http://www.chehang168.com/index.php?c=index&m=index":
        time.sleep(1)
        print(driver.current_url)
    print(driver.current_url)
    time.sleep(1)

    cookie = driver.get_cookies()
    print(cookie)
    print(type(cookie))
    company_queue = queue.Queue()
    finished_queue = queue.Queue()

    series_urls_not_crawl = query_series_person_url_by_status("TODO")
    series_urls_not_crawl = [url[0] for url in series_urls_not_crawl]
    series_urls_not_crawl_4 = div_list(series_urls_not_crawl, 3)

    # TODO, 切分
    t1 = [threading.Thread(target=get_urls, args=(cookie, urls, company_queue, finished_queue)) for urls in
          series_urls_not_crawl_4]
    for t in t1:
        t.start()

    for t in t1:
        t.join()

    company_urls = set()
    series_urls_crawl = set()

    while not company_queue.empty():
        company_urls.add(company_queue.get())

    while not finished_queue.empty():
        series_urls_crawl.add(finished_queue.get())

    for company in company_urls:
        print("%s, %s, %s" % (company[0], company[1], company[2]))

    insert_data_person(company_urls)

    for url_crawl in series_urls_crawl:
        print("finished url is " + url_crawl)
        update_series_person_status_by_url(url_crawl, "DONE")
    print('All subprocesses done.')


def get_urls(cookies, series_urls_not_crawl, company_queue, finished_queue):
    options = webdriver.FirefoxProfile()
    options.set_preference('permissions.default.image', 2)
    driver = webdriver.Firefox(options)
    driver.get("http://www.chehang168.com/")
    time.sleep(2)
    for cookie in cookies:
        driver.add_cookie(cookie)
    time.sleep(8)

    flag = 0
    for series_url in series_urls_not_crawl:
        # TODO, 页码爬取
        driver.get(series_url + '&pricetype=0&page=1')

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
                company_queue.put((url.text, url.get_attribute("href"), "TODO"))

            company2 = driver.find_elements_by_xpath(company_xpath2)
            for url in company2:
                # print("%s, %s" % (url.text, url.get_attribute("href")))
                company_queue.put((url.text, url.get_attribute("href"), "TODO"))

                finished_queue.put(series_url)

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
                company_queue.put((url.text, url.get_attribute("href"), "TODO"))

            company2 = driver.find_elements_by_xpath(company_xpath2)
            for url in company2:
                # print("%s, %s" % (url.text, url.get_attribute("href")))
                company_queue.put((url.text, url.get_attribute("href"), "TODO"))

       if flag:
            finished_queue.put(series_url)
            break
        else:
            finished_queue.put(series_url)


if __name__ == '__main__':
    main()


