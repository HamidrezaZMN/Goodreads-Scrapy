import scrapy, os, ctypes
import easygui as eg
from scrapy.http import FormRequest

#-------------------------------------------------------------------------------------------------------------------------------------------------#
class GoodReads(scrapy.Spider):
    # init
    name = 'gg'
    start_urls = [
        'https://www.goodreads.com/user/sign_in'
    ]
    email = 'YOUREMAIL@gmail.com' #         ***change this****
    passwd = 'YOURPASSWORD'       #         ***change this****

    # for hrefs
    gr = 'https://www.goodreads.com'
    link = 'https://www.goodreads.com/user/show/35791861-hamidreza' # user page url         ***change this****
    
    # read & cr & wtr
    shelves = {}

    # order
    order = 'read' #         ***change this****

    # saving path
    path = 'C:\\Users\\Reza\\Desktop\\gdreads\\results\\'

    # name of the ordered file
    file_name = ''
    if order=='read':
        file_name='read'
    elif order=='cr':
        file_name='currently reading'
    elif order=='wtr':
        file_name='want to read'

    # for the book's name
    counter = 0

    months = {
        'Jan' : '01',
        'Feb' : '02',
        'Mar' : '03',
        'Apr' : '04',
        'May' : '05',
        'Jun' : '06',
        'Jul' : '07',
        'Aug' : '08',
        'Sep' : '09',
        'Oct' : '10',
        'Nov' : '11',
        'Dec' : '12'
    }

#-------------------------------------------------------------------------------------------------------------------------------------------------#
    # init parse
    def parse(self, response):
        values = {
            'utf8' : '&#x2713;',
            'authenticity_token' : response.css("form input::attr(value)")[1].extract(),
            'user[email]' : self.email,
            'user[password]' : self.passwd,
            'remember_me' : 'on',
            'next' : 'Sign in',
            'n' : response.css("form input::attr(value)")[3].extract()
        }

        return FormRequest.from_response(response, formdata=values, callback=self.start_scraping)

#-------------------------------------------------------------------------------------------------------------------------------------------------#
    # yield wanted page
    def start_scraping(self, response):
        yield scrapy.Request(self.link, self.shelf_finder)

#-------------------------------------------------------------------------------------------------------------------------------------------------#
    # yield the wanted shelf
    def shelf_finder(self, response):
        self.shelves['read'] = self.gr + response.css('.userShowPageShelfListItem::attr(href)')[0].extract()
        self.shelves['cr'] = self.gr + response.css('.userShowPageShelfListItem::attr(href)')[1].extract()
        self.shelves['wtr'] = self.gr + response.css('.userShowPageShelfListItem::attr(href)')[2].extract()

        yield scrapy.Request(self.shelves[self.order], self.parse_book)

#-------------------------------------------------------------------------------------------------------------------------------------------------#
    # yield the wanted shelf
    def parse_book(self, response):
        # open file
        f = open(self.path + f'{self.file_name}.py', 'a', encoding='utf-8') # for sorting

        book_dict = {}

        # scraper
        tbody = response.xpath("//tbody[@id='booksBody']/tr")
        for x in tbody:
            # init book num
            self.counter += 1

            # book's name
            label = x.xpath("td[@class='field title']/div/a/text()").extract_first().strip()
            
            # book's author
            author1 = x.xpath("td[@class='field author']/div/a/text()").extract_first().strip()
            author = ''
            check = False
            for i in author1:
                if i==',':
                    check = True
                    break
            if check==True:
                author1 = author1.split(', ')
                author = author1[1]+' '+author1[0]
            else:
                author = author1

            # book's rating
            rate = x.xpath("td[@class='field rating']/div/div/@data-rating").extract_first()
            
            # book's read date
            date = x.xpath("td[@class='field date_read']/div/div/div/span/text()").extract_first()
            book_dict['label'] = label
            book_dict['author'] = author
            if self.order=='read': 
                if rate is not None:
                    book_dict['rate'] = rate.strip()
                else:
                    book_dict['rate'] = 'NO_RATE'
                if date!=None:
                    if date.strip()!='not set':
                        book_dict['date'] = date.strip()
                        date_list = date.strip().split(' ')
                        if len(date_list)==3:
                            date_list[1] = date_list[1][0:2]
                            book_dict['number'] = date_list[2] + self.months[date_list[0]] + date_list[1]
                        elif len(date_list)==2:
                            book_dict['number'] = date_list[1] + self.months[date_list[0]] + '00'
                        else:
                            book_dict['number'] = date_list[0] + '0000'
                    else:
                        book_dict['number'] = 'NO_NUMBER'
                else:
                    book_dict['date'] = 'NO_DATE'
                    book_dict['number'] = 'NO_NUMBER'

            f.write(f'{book_dict}')
            f.write(',\n')
        f.close()

        next_page = response.xpath("//a[@class='next_page']/@href").extract_first()
        if next_page is not None:
            yield response.follow("https://www.goodreads.com"+next_page, self.parse_book)