import scrapy


class MySpider(scrapy.Spider):
    name = 'mySpider'
    allowed_domains = ['xnews.jin10.com']
    start_urls = ['https://xnews.jin10.com/details.html?id=21130']

    def parse(self, response):
        print("-------------------------->>>>>>>" + response.css('html').extract_first())
        for item in response.xpath('//*[@id="app"]/div[3]/div/div/div[1]/div[5]/div[2]/p'):
            print('----->' + item.extract_first())
            yield {
                'newsMsg': item.extract_first()
            }
        pass
