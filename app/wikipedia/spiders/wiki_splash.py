import scrapy


class WikiSplashSpider(scrapy.Spider):
    name = "wiki_splash"
    allowed_domains = ["www.wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/Web_scraping"]

    def parse(self, response, **kwargs):
        pass
