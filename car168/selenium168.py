
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import tkinter as tk
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


# 构造滑动轨迹
def get_trace(distance):
    '''
    :param distance: (Int)缺口离滑块的距离
    :return: (List)移动轨迹
    '''

    # 创建存放轨迹信息的列表
    trace = []
    # 设置加速的距离
    faster_distance = distance * (4 / 5)
    # 设置初始位置、初始速度、时间间隔
    start, v0, t = 0, 0, 0.05
    # 当尚未移动到终点时
    while start < distance:
        # 如果处于加速阶段
        if start < faster_distance:
            # 设置加速度为2
            a = 20.0
        # 如果处于减速阶段
        else:
            # 设置加速度为-3
            a = -1.0
        # 移动的距离公式
        move = v0 * t + 1 / 2 * a * t * t
        # 此刻速度
        v = v0 + a * t
        # 重置初速度
        v0 = v
        # 重置起点
        start += move
        # 将移动的距离加入轨迹列表
        trace.append(round(move))
    # 返回轨迹信息
    return trace

# # 模拟拖动
# def move_to_gap(trace):
#     # 得到滑块标签
#     slider = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'gt_slider_knob')))
#     # 使用click_and_hold()方法悬停在滑块上，perform()方法用于执行
#     ActionChains(browser).click_and_hold(slider).perform()
#     for x in trace:
#         # 使用move_by_offset()方法拖动滑块，perform()方法用于执行
#         ActionChains(browser).move_by_offset(xoffset=x, yoffset=0).perform()
#     # 模拟人类对准时间
#     sleep(0.5)
#     # 释放滑块
#     ActionChains(browser).release().perform()


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
# 得到滑块标签
# trace = get_trace(230)
# slider = WebDriverWait.until(EC.presence_of_element_located((By.CLASS_NAME, 'gt_slider_knob')))
# 使用click_and_hold()方法悬停在滑块上，perform()方法用于执行
ActionChains(driver).click_and_hold(source).perform()
time.sleep(0.5)
ActionChains(driver).move_by_offset(xoffset=250, yoffset=0).perform()
# for x in trace:
#     # 使用move_by_offset()方法拖动滑块，perform()方法用于执行
#     ActionChains(driver).move_by_offset(xoffset=x, yoffset=0).perform()
# 模拟人类对准时间
time.sleep(0.5)
# 释放滑块
ActionChains(driver).release().perform()
while driver.current_url != "http://www.chehang168.com/index.php?c=index&m=index":
    time.sleep(0.5)
    print(driver.current_url)
print(driver.current_url)
time.sleep(0.5)

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
        # print("now visit url is %s" % E1.get())
        # driver.get(E1.get())
        # print("now xpath is %s" % E2.get())
        # brands = driver.find_elements_by_xpath(E2.get())
        # for url in brands:
        #     print(url.get_attribute("href"))

        brand_url_path = "/Users/yu.jin/Downloads/chehang168_brands"

        series_urls = []
        with open(brand_url_path, "r") as f:  # 设置文件对象
            urls = f.readlines()
            for url in urls:
                print(url[:-1])
                driver.get(url[:-1])
                series_xpath = "/html/body/div[4]/div[1]/div[1]/div/div[2]/div/div[*]/ul/li[*]/a"
                series = driver.find_elements_by_xpath(series_xpath)
                for series_url in series:
                    print(series_url.get_attribute("href") + "&type=1")
                    series_urls.append(series_url.get_attribute("href") + "&type=1")  # type=1 代表选中公司

        series_url_path = "/Users/yu.jin/Downloads/chehang168_series"
        with open(series_url_path, "w") as f:  # 设置文件对象
            f.write('\n'.join(series_urls))

    except Exception as e:
        print(e)


button = tk.Button(top, text="按钮", command=access_url, width=20, height=5, padx=20, pady=20)
button.pack()

top.mainloop()


