from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from cerita_sample.items import CeritaSampleItem
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor

class MySpider(CrawlSpider):
	 name = "cerita"
	 allowed_domains = ["dongengceritarakyat.com"]
	 start_urls = ["http://dongengceritarakyat.com/cerita-rakyat-banten-legenda-asal-mula-cikaputrian/"]

	 rules = (
			 Rule(SgmlLinkExtractor(allow=(), restrict_xpaths=('//a[@class="pull-right"]',)), callback="parse_items", follow= True),
	 )

	 def parse_items(self, response):
			 hxs = HtmlXPathSelector(response)
			 contents = hxs.xpath('//div[@class="entry-content ktz-wrap-content-single clearfix ktz-post"]')
			 titles = hxs.xpath('//div[@class="entry-body"]')
			 items = []
			 for titles in titles:
					 item = CeritaSampleItem()
					 item["cerita"] = contents.xpath("p/text()").extract()
					 item["judul"] = titles.xpath("h1/text()").extract()
					 item["link"] = response.request.url
					 items.append(item)
			 return(items)
			 

# from scrapy.spider import BaseSpider
# from scrapy.selector import HtmlXPathSelector
# from cerita_sample.items import CeritaSampleItem
# from scrapy.contrib.spiders import CrawlSpider, Rule
# from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor

# class MySpider(CrawlSpider):
	 # name = "cerita"
	 # allowed_domains = ["dongengceritarakyat.com"]
	 # start_urls = ["http://dongengceritarakyat.com/cerita-rakyat-banten-legenda-asal-mula-cikaputrian/"]

	 # rules = (
			 # Rule(SgmlLinkExtractor(allow=(), restrict_xpaths=('//a[@class="pull-right"]',)), callback="parse_items", follow= True),
	 # )

	 # def parse_items(self, response):
			 # hxs = HtmlXPathSelector(response)
			 # titles = hxs.xpath('//div[@class="entry-content ktz-wrap-content-single clearfix ktz-post"]')
			 # items = []
			 # for titles in titles:
					 # item = CeritaSampleItem()
					 # item["link"] = titles.xpath("h2/text()").extract()
					 # item["title"] = titles.xpath("p/text()").extract()
					 # items.append(item)
			 # return(items)

"""
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from cerita_sample.items import CeritaSampleItem

class MySpider(BaseSpider):
    name = "cerita"
    allowed_domains = ["dongengceritarakyat.com"]
    start_urls = ["http://dongengceritarakyat.com/cerita-dongeng-nusantara-bulu-burung-gagak/"]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        titles = hxs.xpath("//div[@class='entry-content ktz-wrap-content-single clearfix ktz-post']")
        items = []
        for titles in titles:
            item = CeritaSampleItem()
            item["title"] = titles.select("h2/text()").extract()
            items.append(item)
        return items
				"""