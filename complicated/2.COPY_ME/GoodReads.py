import scrapy
import easygui as eg
from scrapy.http import FormRequest

def prop(foo):
    f = open(f'E:\\GoodReads\\goodreads\\goodreads\\spiders\\files\\props\\{foo}.txt')
    n = f.read()
    f.close()
    return n

class GoodReads(scrapy.Spider):
    name = 'spider'
    start_urls = [
        'https://www.goodreads.com/user/sign_in'
    ]

    # user data
    email = prop('email')
    passw = prop('passw')
    bookshelves= {}
    
    question = 'which one do you want?'
    title = 'shelf'
    options = ['read', 'currently reading', 'want to read']
    order = eg.choicebox(question , title, options)
    if order=='currently reading':
        order='cr'
    elif order=='want to read':
        order='wtr'
        
    # file name
    file_name = order
    if order=='cr':
        file_name='currently reading'
    elif order=='wtr':
        file_name='want to read'
        
    # the beginning of the file
    f = open(f'E:\\GoodReads\\results\\{file_name}.txt', 'a', encoding='utf-8')
    if order=='read':
        f.write('read books\n\n-----------------------------------------------------------------------\n')
    elif order=='cr':
        f.write('currently reading books\n\n-----------------------------------------------------------------------\n')
    else:
        f.write('want to read books\n\n-----------------------------------------------------------------------\n')
    f.close()
    
    # sign in function
    def parse(self, response):

        # signing in values
        values = {
            'utf8' : '&#x2713;',
            'authenticity_token' : response.css("form input::attr(value)")[1].extract(),
            'user[email]' : self.email,
            'user[password]' : self.passw,
            'remember_me' : 'on',
            'next' : 'Sign in',
            'n' : response.css("form input::attr(value)")[3].extract()
        }

        return FormRequest.from_response(response, formdata=values, callback=self.start_scraping)
    
    def start_scraping(self, response):
        # passing my books section
        MyBooks = "https://www.goodreads.com/" + response.css(".siteHeader__topLevelItem--home+ .siteHeader__topLevelItem .siteHeader__topLevelLink::attr(href)").extract_first()
        yield response.follow(MyBooks, self.middle_parse)

    def middle_parse(self, response):
        # making bookshelves and passing them accordingly
        self.bookshelves['read'] = "https://www.goodreads.com/" + response.css(".userShelf:nth-child(1) .actionLinkLite::attr(href)").extract_first()
        self.bookshelves['cr'] = "https://www.goodreads.com/" + response.css(".userShelf:nth-child(2) .actionLinkLite::attr(href)").extract_first()
        self.bookshelves['wtr'] = "https://www.goodreads.com/" + response.css(".userShelf:nth-child(3) .actionLinkLite::attr(href)").extract_first()
        yield response.follow(self.bookshelves[self.order], self.find_book)
    
    def find_book(self, response):
        #open file
        f = open(f'E:\\GoodReads\\results\\{self.file_name}.txt', 'a', encoding='utf-8')
        
        # scraper
        tbody = response.xpath("//tbody[@id='booksBody']/tr")
        for x in tbody:
            # properties
            label = x.xpath("td[@class='field title']/div/a/text()").extract_first()
            author = x.xpath("td[@class='field author']/div/a/text()").extract_first()
            rate = x.xpath("td[@class='field rating']/div/div/@data-rating").extract_first()
            date = x.xpath("td[@class='field date_read']/div/div/div/span/text()").extract_first()
            
            # write in file
            f.write(f'name: "{label.strip()}"\n')
            f.write(f'author: "{author.strip()}"\n')
            if self.order=='read': 
                if rate is not None:
                    f.write(f'rating: {rate.strip()}\n')
                else:
                    f.write(f'rating: without rating\n')
                if date is not None:
                    f.write(f'date: {date.strip()}\n')
                else:
                    f.write(f'date: without date\n')
            # end-of-book line
            f.write("-----------------------------------------------------------------------\n")
        
        # close file
        f.close()
        
        # next page
        next_page = response.xpath("//a[@class='next_page']/@href").extract_first()
        if next_page is not None:
            yield response.follow("https://www.goodreads.com"+next_page, self.find_book)

# hamidreza zamanian

