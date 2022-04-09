from flask import render_template
from app_package import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Ravi'}
    posts = [
        {
            'author': {'username': 'Charlie'},
            'body': 'Beautiful day in Bangalore!'
        },
        {
            'author': {'username': 'James'},
            'body': 'The new Marvel film was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
