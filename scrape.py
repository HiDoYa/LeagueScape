import scrapy
from selenium import webdriver
from scrapy.selector import Selector


class QuotesSpider(scrapy.Spider):
    name = 'lcsspider'
    start_urls = [
        'https://www.thescoreesports.com/lol/standings',
    ]

    def __init__ (self):
        self.driver = webdriver.Firefox()

    def parse(self, response):
        self.driver.get(response.url)
        # next = self.driver.find_element_by_xpath('//a/[contains(@tabindex, "1")]')
        next = self.driver.find_element_by_css_selector('div[data-reactid="117"]')
        next.click()
        next = self.driver.find_element_by_css_selector('a[tabindex="1"]')
        next.click()

        
        for quote in Selector(text=self.driver.page_source).css('tr[class^=StandingRow]'):
            yield {
                'team': quote.css('td:nth-child(2) span::text').get(),
                'score': quote.css('td:nth_child(3)::text').get()
            }
    
        self.driver.close()
