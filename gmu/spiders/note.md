name = product.css('h1.product_title.entry-title::text').get()
price = product.css('span.woocommerce-Price-amount.amount > bdi::text').get().replace('\xa0','')

consume = product.xpath('//div[contains(@id, "tab-description")]/div[contains(@class,"wc-tab-inner")]').re('چطور مصرف کنیم</h3>\n<p style="text-align: justify"(>*.*.\.)') 
consume = consume[0]
consume = consume.replace('>','')

review = product.xpath('//div[contains(@id, "tab-description")]/div[contains(@class,"wc-tab-inner")]/p/text()').get()

drug_property = product.xpath('//div[contains(@id, "tab-description")]/div[contains(@class,"wc-tab-inner")]/ul/li/text()').getall()
drug_property = '، '.join(drug_property)

