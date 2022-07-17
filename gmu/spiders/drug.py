import scrapy

class DrugSpider(scrapy.Spider):
    name = 'drug'
    start_urls = [
        'https://mosbatesabz.com/']
        

    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formdata={'s': f'{self.name}', },
            callback=self.scrap_drug
        )

    def scrap_drug(self,response):
            
        for products in response.css('div.row.product-image-summary-inner'):
            consume = products.xpath(
                '//div[contains(@id, "tab-description")]/div[contains(@class,"wc-tab-inner")]').re('چطور مصرف کنیم</h3>\n<p style="text-align: justify..(.*.*.*.\.)')
            consume = consume[0]
            drug_property = products.xpath(
                '//div[contains(@id, "tab-description")]/div[contains(@class,"wc-tab-inner")]/ul/li/text()').getall()
            yield {
                'name' : products.css('h1.product_title.entry-title::text').get(),
                'price': products.css('span.woocommerce-Price-amount.amount > bdi::text').get().replace('\xa0', ''),
                'consume' : consume.replace('>',''),
                'review': products.xpath('//div[contains(@id, "tab-description")]/div[contains(@class,"wc-tab-inner")]/p/text()').extract_first(),
                'drug_property' : '، '.join(drug_property)
            }
