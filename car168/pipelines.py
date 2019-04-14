#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : pipelines.py
# @Author: yu.jin
# @Date  : 2019-04-14
# @Desc  :


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import codecs
import os

from scrapy.exporters import CsvItemExporter

from car168.items import CarBrandItem


class CarBrandPipeline(object):
    def open_spider(self, spider):
        home_dir = os.environ['HOME']
        self.outputPath = home_dir + '/crawler_data/car168/'
        if not os.path.exists(self.outputPath):
            os.mkdir(self.outputPath)
        self.car168_brand_csv = codecs.open(self.outputPath + 'car168_brand.csv', 'w', encoding='utf-8')
        self.car168_brand_exporter = CsvItemExporter(self.car168_brand_csv)
        self.car168_brand_exporter.start_exporting()

    def process_item(self, item, spider):
        if isinstance(item, CarBrandItem):
            self.car168_brand_exporter.export_item(item)
        return item

    def close_spider(self, spider):
        self.car168_brand_exporter.finish_exporting()
        self.car168_brand_csv.close()
