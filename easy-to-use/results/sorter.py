books = [...]

withNumber = []
withoutNumber = []
for book in books:
    if book['number']!='NO_NUMBER':
        withNumber.append(book)
    else:
        withoutNumber.append(book)

from operator import itemgetter
SortedRead = sorted(withNumber, key=itemgetter('number'), reverse=True)
f = open('SortedReads.py', 'a', encoding='utf-8')
for i in SortedRead:
    f.write(f'{i}')
    f.write(',\n')
for i in withoutNumber:
    f.write(f'{i}')
    f.write(',\n')
f.close()