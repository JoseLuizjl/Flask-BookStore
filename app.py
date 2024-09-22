from flask import Flask, render_template, request
from books_api import get_book

app = Flask(__name__)

@app.route('/', methods=['GET', "POST"])
def index():
    if request.method == "POST":
        book = request.form['bookInput']
        title, author, categories, bookImage = get_book(book)

        return render_template('index.html', title=title, author=author, 
                            categories=categories, bookImage=bookImage)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)