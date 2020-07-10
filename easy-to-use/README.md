# How-To-Use
As you know, scrapy doesn't work with, like, copy and pasting the whole project. So go to the spiders folder and open the gg.py with any editor you want. Then change these informations: email(line 12), passwd(line 13) and link(line 17), order(line 23)
The link option is the link of your goodreads' page. for example, mine is https://www.goodreads.com/user/show/35791861-hamidreza
The order option is the shelf you want the data from. it must be one of these: read, cr, wtr
After that, go back and run gg.bat. Then open results
now you can do see the .py file that is made (with the name of the order you wrote). open it. copy everything in it. open sorter.py. in the first line inside the list, paste the copied text, instead of those three dots.
run sorter.py
open the SortedReads.py file and copy its text. open printer.py. paste the text inside books = [...]. run the file and the result will be in Printedbooks.txt.

if you wanted other shelves, do the same way for them
