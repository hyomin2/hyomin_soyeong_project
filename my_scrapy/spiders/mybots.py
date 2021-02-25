import scrapy
from my_scrapy.items import MyScrapyItem
import time
from selenium import webdriver

class MybotsSpider(scrapy.Spider):

  
    name = 'mybots'
    allowed_domains = ['finance.naver.com/item/sise.nhn?code=005930']
    # start_urls = ['https://finance.naver.com/item/sise.nhn?code=005930']
    start_urls = []
    for i in range(1, 10000):
        start_urls.append('https://finance.naver.com/item/sise.nhn?code=005930')


    # def start_requests(self):
    #     urls = [
    #         'https://finance.naver.com/item/sise.nhn?code=005930'
    #     ]
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)

    # 결과값
    def parse(self, response):

        items = []

        now_time = response.xpath('//*[@id="time"]/em/text()').extract()
        amount = response.xpath('//*[@id="_quant"]/text()').extract()
        price = response.xpath('//*[@id="_nowVal"]/text()').extract()
        max_price = response.xpath('//*[@id="content"]/div[2]/div[1]/table/tbody/tr[8]/td[1]/span/text()').extract()
        min_price = response.xpath('//*[@id="content"]/div[2]/div[1]/table/tbody/tr[9]/td[1]/span/text()').extract()
        s_code = response.xpath('//*[@id="middle"]/div[1]/div[1]/div/span[1]/text()').extract()

        print(now_time)
        print(amount)
        print(price)
        print(max_price)
        print(min_price)
        print(s_code)

        item = MyScrapyItem()
        item['now_time'] = now_time[0]
        item['amount'] = amount[0]
        item['price'] = price[0]
        item['max_price'] = max_price[0]
        item['min_price'] = min_price[0]
        item['s_code'] = s_code[0]
        items.append(item)

        return items

        
