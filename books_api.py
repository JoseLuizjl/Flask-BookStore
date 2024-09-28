import requests

def get_book(books_name):
    books_info = []  
    for book_name in books_name:
        url = f'https://www.googleapis.com/books/v1/volumes?q={book_name}'
        response = requests.get(url).json()

        if 'items' in response and response['items']:
            item = response['items'][0]
            title = item['volumeInfo'].get('title', 'Unknown Title')
            author = ', '.join(item['volumeInfo'].get('authors', ['Unknown Author']))
            categories = ', '.join(item['volumeInfo'].get('categories', ['No Category']))
            book_image = item['volumeInfo'].get('imageLinks', {}).get('thumbnail', '/static/assets/default_cover.png')

            sale_info = item.get('saleInfo', {})
            list_price = sale_info.get('listPrice', {})

            amount = list_price.get('amount', 0.0)
            if isinstance(amount, str):  
                try:
                    amount = float(amount)
                except ValueError:
                    amount = 0.0

            books_info.append({
                'name': title,
                'author': author,
                'categories': categories,
                'image': book_image,
                'price': f"US$ {amount:.2f}"  
            })
        else:
            books_info.append({
                'name': "No Title Found",
                'author': "No Author Found",
                'categories': "No Category",
                'image': "/static/assets/default_cover.png",
                'price': "US$ 0,00"
            })
    
    return books_info
