#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : file_read.py
# @Author: yu.jin
# @Date  : 2019-04-18
# @Desc  :
#

import numpy as np
import queue

company_urls = set()
series_urls_crawl = set()
company_queue = queue.Queue()
company_queue.put(("A", "B", "C"))
company_queue.put(("A", "B", "C"))
company_queue.put(("A", "B", "D"))

while not company_queue.empty():
    a = company_queue.get()
    print(a)
    company_urls.add(a)


for company in company_urls:
    print("%s, %s, %s" % (company[0], company[1], company[2]))

# a = np.random.random(1)
#
# print(a[0]+1)

# file_path = "/Users/yu.jin/Downloads/chehang168_series_0418.txt"
# #
# with open(file_path, "r") as f:    #设置文件对象
#     urls = f.readlines()
#     for url in urls:
#         print(url[:-1].split(",")[1])

# lists = [('a', 'a'), ('b', 'b'), ('jy', 'jy'), ('syf', 'syf'), ('a', 'a')]
# sets = set()
#
# for i in lists:
#     sets.add(i)
#
# print(len(sets))
# lists1 = ['a', 'b', 'c', 'd']
# lists2 = ['a', 'b', 'c', 'd']
# lists3 = zip(lists1, lists2)
# print(type(lists3))
#
# file_path = "/Users/yu.jin/Downloads/chehang168_seri"
# with open(file_path, "w") as f:    #设置文件对象
#     # f.write('\n'.join(lists3))
#     lists4 = ["%s,%s"%(line[0], line[1]) + "\n" for line in lists]
#     f.writelines(lists4)

# a = "http://www.chehang168.com/index.php?c=index&m=series&psid=7986z&type=1&pricetype=0&page=14"
# print(a.find("page="))
# print(a[a.find("page=")+5:])

# for i in range(5):
#     print(i)