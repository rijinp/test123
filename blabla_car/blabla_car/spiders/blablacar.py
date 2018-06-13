# -*- coding: utf-8 -*-
import scrapy
from ..items import RiderItem

class BlablacarSpider(scrapy.Spider):
     name = 'blablacar'
     allowed_domains = ['blablacar.in']
     start_urls = ['https://www.blablacar.in/ride-sharing/new-delhi/chandigarh/?fn=New+Delhi&fc=28.6139391%7C77.2090212&fcc=IN&fp=0&tn=Chandigarh&tc=30.7333148%7C76.7794179&tcc=IN&tp=0&sort=trip_date&order=asc&radius=48.858&limit=10&page=2&v=default','https://www.blablacar.in/ride-sharing/new-delhi/chandigarh/?fn=New+Delhi&fc=28.6139391%7C77.2090212&fcc=IN&fp=0&tn=Chandigarh&tc=30.7333148%7C76.7794179&tcc=IN&tp=0&sort=trip_date&order=asc&radius=48.858&limit=10&page=25&v=default','https://www.blablacar.in/ride-sharing/new-delhi/chandigarh/?fn=New+Delhi&fc=28.6139391%7C77.2090212&fcc=IN&fp=0&tn=Chandigarh&tc=30.7333148%7C76.7794179&tcc=IN&tp=0&sort=trip_date&order=asc&radius=48.858&limit=10&page=4&v=default']

     def parse(self, response):
        riders = response.css('.trip-search-results li')
        for r in riders:
            name = r.css('.ProfileCard-info--name::text').extract_first().strip()
            rating=r.css('.u-darkGray::text').extract_first()
            age=r.css('.ProfileCard-info::text')[1].extract().strip()
            date = r.css('.description .time::attr(content)').extract_first()
            source=r.css('.trip-roads-stop::text').extract_first()
            trip=r.css('a::attr(href)').extract_first()
            departure= r.css('.js-tip-custom::text').extract_first()
            fare= r.xpath('/html/body/div[2]/div/div[3]/div[2]/div/div[3]/ul/li[3]/a/article/div[3]/div[1]/strong/span').extract_first().strip()
            availablity= r.css('.availability').extract()
            image= r.xpath('/html/body/div[2]/div/div[3]/div[2]/div/div[3]/ul/li[1]/a/article/div[1]/div[1]/div[1]/div/img').extract()[0]
            item = RiderItem()
            item['name'] = name
            item['rating']=rating
            item['age']=age
            item['date'] = date
            item['source']=source
            item['trip']=trip
            item['departure_point']=departure
            item['fare']=fare
            item['availablity']=availablity
            item['image']=image
            yield item
        nextPageLinkSelector = response.css('.pagination .next:not(.disabled) a').extract()
        if nextPageLinkSelector:
            nextPageLink = nextPageLinkSelector[0].extract()
            yield scrapy.Request(url=response.urljoin(nextPageLink))

            
          #  for a_tag in response.css('.pagination .next:not(.disabled) a'):
        #yield response.follow(a_tag, self.parse_route)