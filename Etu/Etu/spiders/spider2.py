import scrapy


class Spider(scrapy.Spider):
    name = "courses2"
    start_urls = [
        'http://servis.erzurum.edu.tr/bologna/de/mufredat?program=70&mufredatID=4367&dersID=2126',
    ]

    def parse(self, response):
        yield {
            'isim': response.css('td::text').get(),
            'amac': response.css('small::text')[1].get(),
            'icerik': response.css('small::text')[2].get()
        }
