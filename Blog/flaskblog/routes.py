from flask import render_template, url_for, flash, redirect
from flaskblog import app
from flaskblog.models import User, Post
from flaskblog.forms import RegistrationForm, LoginForm



posts = [
	{
		'author': 'Bla',
		'title': 'Title 1',
		'content': 'Content #1',
		'date_posted': 'Mai 2, 1987'
	},
	{
		'author': 'FSasfg ',
		'title': 'Title 2',
		'content': 'Content #2',
		'date_posted': 'Mai 12, 1987'
	},
]



@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html', posts = posts)


@app.route('/about')
def about():
	return render_template('about.html', title = 'About')


@app.route('/register', methods = ['GET','POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		flash(f'Account created for {form.username.data}!','success')
		return redirect(url_for('home'))
	return render_template('register.html', title = 'Registration', form = form)


@app.route('/login', methods = ['GET','POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():

		# test data
		if form.email.data == 'admin@blog.com' and form.password.data == 'asd':
			flash('You have been logged in', 'success')
			return redirect(url_for('home'))
		else:
			flash('Login Unsuccessful. Please check username and password', 'danger')
	return render_template('login.html', title = 'Login', form = form)
