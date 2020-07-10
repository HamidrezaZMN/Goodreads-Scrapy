# How-To-Use
Caution: Your E drive must be empty.
  1. If you can't open goodreads without VPN, then turn it on
  2. You have to have python 3.7 and nodejs in your computer. because it seems like scrapy doesn't work with python 3.8 and also the twisted package (which is installed during the installation of scrapy), needs nodejs
  3. Run the first file (1.run.bat) to do the initializings, such as installing scrapy, easygui and ...
  4. Open the 2nd file (2.COPY-ME) and copy everything in the folder to this dir: E:\goodreads\goodreads\goodreads\spiders
  5. The 3rd file is for your email and password. Run it and enter your Goodreads account info
  6. After running the 4th file you have to choose what shelf you want to extract. After choosing and pressing Enter the scraping starts. At the end, the folder containing your requested shelf's data, appears. Now, if you wanted to scrape other shelfs too, you have to run the 6th file again and choose the shelf you want. If someone else wanted to use this thing too, he/she have to run the 3rd file again to enter the email and pass, then running the 4th file.
  
If the results weren't satisfying, check if the scrapy is installed, easygui is installed and python 3.7 is added to path

Caution: if you have chosen a shelf before, and you want to choose it again, you have to go to the results folder and delete the files in that. The results folder is located at E:\goodreads

Contact me if you liked it :)
