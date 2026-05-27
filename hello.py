from flask import Flask, render_template, request
from markupsafe import escape
app = Flask(__name__)

# ex43: Hello Flask
@app.route('/home')
def home():
    return render_template('home.html')

# ex44: URL Info
@app.route('/user/<username>')
def show_user(username):
    return f'User {escape(username)}'

# ex45: URL Info (same as ex44)
# ex46: Flask Load HTML
@app.route('/Apple')
def apple():
    return render_template('apple.html')

# ex47: Show Variables
@app.route('/page')
def page():
    x = {
        "name": "John",
        "age": 30,
        "city": "New York"
    }
    return render_template('page.html', x=x)

# ex48: Double Number
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    x = int(request.form['x'])
    result = x * 2
    return render_template('index.html', result=result)