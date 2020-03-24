import scrapy
from cleaning import clean_price

"""
    Запуск:
        scrapy runspider auto_ru.py -L WARNING --output=data/auto_ru.json
"""


class Spider(scrapy.Spider):
    name = 'spider'
    start_urls = ['https://auto.ru/balashiha/cars/tesla/all/?currency=EUR']

    def parse(self, response):
        for car_div in response.css('.ListingItem-module__main'):
            link = car_div.css('a.ListingItemTitle-module__link')
            title = link.css('::text').get()
            href = link.css('::attr(href)').get()
            raw_price = car_div.css('.ListingItemPrice-module__content::text').get()
            img_urls = car_div.css('.Brazzers__image::attr(data-src)').getall()
            price = raw_price and clean_price(raw_price) or None
            yield {
                'title': title,
                'price_eur': price,
                'href': href,
                'imgs': [response.urljoin(img) for img in img_urls],
            }
