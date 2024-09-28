from flask import Flask, render_template, request, redirect, session, url_for
from books_api import get_book
from flask_bcrypt import Bcrypt, check_password_hash
from database.database import User, session as db_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
bcrypt = Bcrypt(app)


from flask import Flask, render_template, request
from books_api import get_book

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        book = request.form['search']
        return redirect(url_for('index', search=book))

    search = request.args.get('search')
    search_results = get_book([search]) if search else []

    books_name = ['Programming Python', 'Little Prince', 'Crime and Punishment', 'Dracula',
                  'Frankenstein', 'The Metamorphosis', 'Think Python']
    carousel_books = get_book(books_name)

    return render_template('index.html', carousel_books=carousel_books, search_results=search_results)



@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirmPassword = request.form['confirmPassword']

        if password != confirmPassword:
            session['msg'] = 'Passwords do not match'
            return redirect('/register')

        existing_user = db_session.query(User).filter_by(email=email).first()
        if existing_user:
            session['msg'] = 'Email already registered'
            return redirect('/register')

        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        new_user = User(username=username, email=email, password=hashed_password)

        db_session.add(new_user)
        db_session.commit()

        return redirect('/login')
    
    msg = session.pop('msg', '')
    return render_template('register.html', msg=msg)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = db_session.query(User).filter_by(email=email).first()

        if user and bcrypt.check_password_hash(user.password, password):
            return redirect('/')
        else:
            session['msg'] = 'Invalid email or password. Please try again.'

    msg = session.pop('msg', '')
    return render_template('login.html', msg=msg)


@app.route('/wishlist', methods=['GET','POST'])
def wishlist():
    return render_template('wishlist.html')


@app.route('/cart', methods=['GET', 'POST'])
def cart():
    return render_template('cart.html')


@app.route('/profile', methods=['GET', 'POST'])
def profile():
    return render_template('profile.html')

if __name__ == "__main__":
    app.run(debug=True)