import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://www.nhc.noaa.gov/gis/archive_forecast_results.php?id=al02&year=2016&name=Tropical%20Storm%20BONNIE',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'url': quote.css('span.text::text').extract_first(),
                'author': quote.xpath('span/small/text()').extract_first(),
            }

        next_page = response.css('li.next a::attr("href")').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)