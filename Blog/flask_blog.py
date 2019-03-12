from flask import Flask, render_template, url_for


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


app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html', posts = posts)


@app.route('/about')
def about():
	return render_template('about.html', title = 'About')


if __name__=='__main__':
	app.run(debug = True)