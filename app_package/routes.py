from flask import flash, redirect, render_template, url_for
from app_package import app
from app_package.forms import LoginForm


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


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(
            f"Login requested for the user: {form.username.data}, \
                remember_me={form.remember_me.data}")
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
