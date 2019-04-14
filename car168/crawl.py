#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : crawl.py
# @Author: yu.jin
# @Date  : 2019-04-14
# @Desc  :

from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
from scrapy.utils.log import configure_logging
from car168.spiders.car168_crawl import Car168Spider


def start_crawl():
    settings = get_project_settings()
    configure_logging(settings=settings)
    runner = CrawlerRunner(settings=get_project_settings())
    runner.crawl(Car168Spider)
    d = runner.join()
    d.addBoth(lambda _: reactor.stop())
    reactor.run()


if __name__ == '__main__':
    start_crawl()
