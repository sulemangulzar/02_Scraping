import requests
from bs4 import BeautifulSoup

url = 'https://books.toscrape.com/'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

book_list = soup.find('ol', class_='row')
books = book_list.find_all('li')


with open('books.txt', 'w') as f:
    f.write('') 

for book in books:
    title = book.h3.a['title']
    price = book.find('p', class_='price_color').text.strip()
    stock = book.find('p', class_='instock availability').text.strip()
    rating_tag = book.find('p', class_='star-rating')
    rating = 0
    if rating_tag:
        classes = rating_tag.get('class')
        if len(classes) > 1:
            word_to_number = {
                'One': 1,
                'Two': 2,
                'Three': 3,
                'Four': 4,
                'Five': 5
            }
            rating = word_to_number.get(classes[1], 0)

    with open('books.txt', 'a', encoding='utf-8') as f:
        f.write(f"📚 Title: {title}\n")
        f.write(f"💰 Price: {price}\n")
        f.write(f"📦 Stock: {stock}\n")
        f.write(f"⭐ Rating: {rating} stars\n")
        f.write("-" * 40 + "\n")
print('Saved!')