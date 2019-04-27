from selenium import webdriver

options=webdriver.FirefoxProfile()
options.set_preference('permissions.default.image', 2)
b=webdriver.Firefox(options)
b.get('http://image.baidu.com/')
