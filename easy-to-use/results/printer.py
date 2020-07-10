books = [...]

f = open('Printedbooks.txt', 'a', encoding='utf-8')
for i in range(len(books)):
    label = books[i]['label']
    author = books[i]['author']
    f.write(f'--{i+1}--\n')
    f.write(f'name: {label}\n')
    f.write(f'author: {author}\n')
    try:
        rate = books[i]['rate']
        f.write(f'rating: {rate}\n')
    except:
        f.write(f'rating: without rating\n')
    try:
        date = books[i]['date']
        f.write(f'date: {date}\n')
    except:
        f.write(f'date: without dating\n')
    f.write("-----------------------------------------------------------------------\n")
f.close()