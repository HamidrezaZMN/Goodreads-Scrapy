import easygui as eg
lst = ['email', 'passw']
for i in lst:
    f = open(f'E:\\GoodReads\\goodreads\\goodreads\\spiders\\files\\props\\{i}.txt', 'w', encoding='utf-8')
    name = i
    if i=='passw':
        name+='ord'
    writer = eg.enterbox(f'enter your {name}: ')
    f.write(writer)
    f.close()
