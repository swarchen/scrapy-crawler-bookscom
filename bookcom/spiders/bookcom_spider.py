import scrapy

from bookcom.items import BookcomItem

class BookcomSpider(scrapy.Spider):
    name = "bookcom"
    allowed_domains = ["http://www.books.com.tw"]
    f = open('urls.txt')
    start_urls = [url.strip() for url in f.readlines()]
    f.close()


    def parse(self, response):
        item = BookcomItem()
        item['title'] = response.xpath('//h1/text()').extract()
        item['author'] = response.xpath('//li[@itemprop="author"]/a/text()').extract()
        item['category'] = response.xpath('//body/ul/li[3]/a/span/text()').extract()
        item['publisher'] = response.xpath('//span[@itemprop="brand"]/text()').extract()
        item['pages'] = response.xpath('//div[@class="bd"]/ul/li/text()').extract()
        item['imgUrl'] = response.xpath('//img[@itemprop="image"]/@src').re('(.*?)&v')
        yield item