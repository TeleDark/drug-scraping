import scrapy

class DrugSpider(scrapy.Spider):
    name = 'drug'
    start_urls = [
        'https://mosbatesabz.com/product/vitabiotics-neurozan-feed-your-min-original-30-tab/']
        

    def parse(self, response):
        
        for products in response.css('div.row.product-image-summary-inner'):
            consume = products.xpath(
                '//div[contains(@id, "tab-description")]/div[contains(@class,"wc-tab-inner")]').re('چطور مصرف کنیم</h3>\n<p style="text-align: justify..(.*.*.*.\.)')
            consume = consume[0]
            drug_property = products.xpath(
                '//div[contains(@id, "tab-description")]/div[contains(@class,"wc-tab-inner")]/ul/li/text()').getall()
            yield {
                'iran' : 'test',
                'name' : products.css('h1.product_title.entry-title::text').get(),
                'price': products.css('span.woocommerce-Price-amount.amount > bdi::text').get().replace('\xa0', ''),
                'consume' : consume.replace('>',''),
                'review': products.xpath('//div[contains(@id, "tab-description")]/div[contains(@class,"wc-tab-inner")]/p/text()').extract_first(),
                'drug_property' : '، '.join(drug_property)
            }
