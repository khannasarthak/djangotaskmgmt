from app import app
from flask import render_template, flash, redirect, url_for
from flask_pymongo import PyMongo
from app.forms import LoginForm

app.config['MONGO _DBNAME'] = 'taskmgmt'
app.config['MONGO_URI'] = 'mongodb://sarthak:qwerty123@ds157843.mlab.com:57843/taskmgmt'


mongo = PyMongo(app)

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Sarthak'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]

    # tasks = mongo.db.tasks
    # tasks.insert({'Name': 'Closing List 2'})
    # return ('Added User')
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login',methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)