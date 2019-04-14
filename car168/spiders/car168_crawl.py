#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : car168_crawl.py
# @Author: yu.jin
# @Date  : 2019-04-14
# @Desc  :



import scrapy
# import sys
import re
from importlib import reload
from scrapy.spiders import Spider
from ..items import CarBrandItem
from scrapy.http import Request, FormRequest
from scrapy.selector import Selector


# reload(sys)
# sys.setdefaultencoding('utf-8')


class Car168Spider(Spider):
    """

    """
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip,deflate",
        "Accept-Language": "en-US,en;q=0.8,zh-TW;q=0.6,zh;q=0.4",
        "Connection": "keep-alive",
        "Content-Type":" application/x-www-form-urlencoded; charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",
        "Origin": "http: // www.chehang168.com",
        "Referer": "http: // www.chehang168.com / index.php?c = login & m = index"
    }

    name = 'car168_spider'

    custom_settings = {
        'ITEM_PIPELINES': {'car168.pipelines.CarBrandPipeline': 100},
        'USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
        'ROBOTSTXT_OBEY': True
    }

    start_urls = [
        'http://www.chehang168.com/index.php?c=login&m=index',
    ]

    start_urls2 = [
        'http://www.chehang168.com/index.php?c=index&m=allBrands',
    ]

    def start_requests(self):
        return [Request("http://www.chehang168.com/index.php?c=login&m=GetLoginBySms",
                        meta={'cookiejar': 1},
                        callback=self.post_login)]  # 重写了爬虫类的方法, 实现了自定义请求, 运行成功后会调用callback回调函数

    # FormRequeset
    def post_login(self, response):
        print
        'Preparing login'
        # 下面这句话用于抓取请求网页后返回网页中的_xsrf字段的文字, 用于成功提交表单
        # xsrf = Selector(response).xpath('//input[@name="_xsrf"]/@value').extract()[0]
        # print
        # xsrf
        # FormRequeset.from_response是Scrapy提供的一个函数, 用于post表单
        # 登陆成功后, 会调用after_login回调函数
        return [FormRequest.from_response(response,
                                          meta={'cookiejar': response.meta['cookiejar']},
                                          # headers=self.headers,
                                          formdata={
                                              'name': '17816861605',
                                              'verify': '2286'  # 手机收到的验证码
                                          },
                                          callback=self.after_login,
                                          dont_filter=True
                                          )]

    def after_login(self, response):
        for url in self.start_urls2:
            yield self.make_requests_from_url(url)

    def parse(self, response):
        self.logger.info('Start Crawling Car 168...')
        names = response.xpath("/html/body/div[4]/div/ul/li[*]/a[*]/text()").extract()
        urls = response.xpath("/html/body/div[4]/div/ul/li[*]/a[*]/@href").extract()
        names_and_urls = zip(names, urls)
        for name, url in names_and_urls:
            item = CarBrandItem
            item['name'] = name
            item['url'] = url
            yield item

