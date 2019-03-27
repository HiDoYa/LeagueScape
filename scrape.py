import scrapy
from selenium import webdriver


class QuotesSpider(scrapy.Spider):
    name = 'lcstspider'
    start_urls = [
        'https://www.thescoreesports.com/lol/standings',
    ]

    def __init__ (self):
        self.driver = webdriver.Firefox()

    def parse(self, response):
        while True:
            try:
                self.driver.get('https://www.thescoreesports.com/lol/standings')
                next = self.driver.find_element_by_xpath('//a/[contains(@tabindex, "1")]')
                url = 'https://www.thescoreesports.com/lol/standings'
                yield Request(url, callback=self.parse2)
                next.click()
            except:
                break
        
        self.drive.close()


    def parse2(self, response):
        for quote in response.css('tr[class^=StandingRow]'):
            yield {
                'team': quote.css('td:nth-child(2) span::text').get(),
                'score': quote.css('td:nth_child(3)::text').get()
            }        

        # next_page = response.css('a::attr("href")').get()
        # if next_page is not None:
        #     yield response.follow(next_page, self.parse)

