import scrapy
from scrapy.http.request import Request
import time
from os.path import isfile

from ..items import LightshotItem


class getImages(scrapy.Spider):
    name = 'lightshot-images'
    #variables = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    variables = ['9', '8', '7', '6', '5', '4', '3', '2', '1', '0', 'z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']
    def start_requests(self):
        global nome
        for a in self.variables:
            for b in self.variables:
                for c in self.variables:
                    url = 'https://prnt.sc/as3{}{}{}'.format(a,b,c)
                    nome = url[-6:]
                    time.sleep(2)
                    if isfile(PAUSEFILE):
                        input('Remove ' + PAUSEFILE + ' and hit ENTER to continue')
                    yield Request(url, meta={'start_url':url}, callback=self.parse)


    def parse(self, response):
        print(self.start_urls)
        item = LightshotItem()
        img_urls = []
        for image in response.xpath('/html/body/div[3]/div'):
            print("Aqui",image.css('::attr(src)').extract_first())
            img_urls.append(image.css('::attr(src)').extract_first())
            item["image_urls"] = img_urls
            item["image_name"] = [nome]
        print(img_urls)
        yield item


