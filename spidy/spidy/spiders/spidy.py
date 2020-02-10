import scrapy

class Scrapinghub(scrapy.Spider):
  name = "scrapinghub"
  
  start_urls = ["https://blog.scrapinghub.com/"]
  
  def parse(self, res):
    #to add to html file
    """ page = res.url.split('/')[-1]
    file = "post-%s.html" % page
    with open(file, 'wb') as f:
      f.write(res.body) """
    
    for post in res.css('div.post-item'):
      yield {
        "title": post.css('.post-header h2 a::text')[0].get(),
        "date": post.css('.post-header a::text')[1].get(),
        "author": post.css('.post-header a::text')[2].get(),
      }
    nextPage = res.css('a.next-posts-link::attr(href)').get()
    if nextPage:
      nextPage = res.urljoin(nextPage)
      yield scrapy.Request(nextPage, callback=self.parse)


