from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get("https://account.xiaomi.com/pass/serviceLogin?callback=https%3A%2F%2Forder.mi.com%2Flogin%2Fcallback%3Ffollowup%3Dhttps%253A%252F%252Fwww.mi.com%252F%26sign%3DNzY3MDk1YzczNmUwMGM4ODAxOWE0NjRiNTU5ZGQyMzFhYjFmOGU0Nw%2C%2C&sid=mi_eshop&_bannerBiz=mistore&_qrsize=180")
time.sleep(2)
name = browser.find_element_by_name("user")
name.send_keys("账号")
passwd = browser.find_element_by_name("password")
passwd.send_keys("密码")
login_button = browser.find_element_by_id("login-button")
login_button.click()