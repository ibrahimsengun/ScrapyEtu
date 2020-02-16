import scrapy

from ..items import EtuItem


class CoursesSpider(scrapy.Spider):
    name = "courses"
    start_urls = [
        'http://servis.erzurum.edu.tr/bologna/de/program/70',
    ]

    def parse(self, response):
        for course in response.css('tr'):
            next_page = course.css("a::attr(href)").get()
            if next_page is not None:
                next_page = response.urljoin(next_page)
                yield scrapy.Request(next_page, callback=self.parse)


        if len(response.css('small::text')) == 8:
            yield {
                'isim': response.css('td::text').get(),
                'amac': response.css('small::text')[1].get(),
                'icerik': response.css('small::text')[2].get()
            }

        if len(response.css('small::text')) == 7:
            yield {
                'isim': response.css('td::text').get(),
                'amac': response.css('small::text')[0].get(),
                'icerik': response.css('small::text')[1].get()
            }
