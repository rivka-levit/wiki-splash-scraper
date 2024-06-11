import scrapy


class WikiSplashSpider(scrapy.Spider):
    name = "wiki_splash"
    allowed_domains = ["www.wikipedia.org"]
    start_urls = ["https://www.wikipedia.org"]

    def parse(self, response, **kwargs):
        pass
