import requests



def get_book(bookName):
    url = f'https://www.googleapis.com/books/v1/volumes?q=${bookName}'
    response = requests.get(url).json()
    
    if 'items' in response and len(response['items']) > 0:
        volume_info = response['items'][0]['volumeInfo']
        
        title = volume_info.get('title', 'No title Available')
        author = ''.join(volume_info.get('authors', ['No author Available']))
        categories = ''.join(volume_info.get('categories', ['No categories Available']))
        bookImage = volume_info.get('imageLinks', {}).get('thumbnail')
        
        return title, author, categories, bookImage
    return None, None, None, None
    
    