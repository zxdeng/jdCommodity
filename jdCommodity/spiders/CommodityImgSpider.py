import scrapy
from ..items import JdCommodityItem
from jdCommodity.image_splice import spliceImage

class CommodityImgGetSpider(scrapy.Spider):
    name = "jd"

    def start_requests(self):
        start_urls = (
                      #   'https://item.m.jd.com/product/8024543.html',
                      # 'https://item.m.jd.com/product/100002964733.html',
                      # 'https://item.m.jd.com/product/100003433872.html',
                      # 'https://item.m.jd.com/product/100004363706.html',
                      # 'https://item.m.jd.com/product/39198890862.html',
                      # 'https://item.m.jd.com/product/100000234079.html',
                      # 'https://item.m.jd.com/product/100001964366.html',
                      # 'https://item.m.jd.com/product/100000260076.html',
                      # 'https://item.m.jd.com/product/100001332632.html',
                      # 'https://item.m.jd.com/product/100001054333.html',
                      'https://item.m.jd.com/product/100004680720.html',
                      )
        for url in start_urls:
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        urls = response.xpath("//div[@id='commDesc']//img/@item_init_src").extract()
        # name = response.xpath("//title/text()").extract()[0]
        print(urls)
        name = response.xpath("//div[@id='buyArea']//div[@id='itemName']/text()").extract()[0]
        for i in range(len(urls)):
            urls[i] = 'https:' + urls[i]
            urls[i] = urls[i].replace('!q70.dpg', '')
        yield JdCommodityItem(image_urls=urls, name=name)

    def close(spider, reason):
        spliceImage()