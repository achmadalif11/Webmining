import scrapy


class scrapPTA(scrapy.Spider):
    name = 'PTA'
    allowed_domains = ['pta.trunojoyo.ac.id']
    start_urls = ['https://pta.trunojoyo.ac.id/c_search/byprod/7/' +
                  str(x)+" " for x in range(1, 10)]

    def parse(self, response):
        for link in response.css('a.gray.button::attr(href)'):
            yield response.follow(link.get(), callback=self.parse_categories)

    def parse_categories(self, response):
        products = response.css('div#content_journal ul li')
        for product in products:
            yield {
                'abstrak': product.css('div div:nth-child(2) p::text').get().strip()
            }