#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : items.py
# @Author: yu.jin
# @Date  : 2019-04-14
# @Desc  :

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class CarBrandItem(Item):
    name = Field()  # 品牌
    url = Field()   # 品牌链接


