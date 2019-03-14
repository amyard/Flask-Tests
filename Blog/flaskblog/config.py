import os


class Config:
	
	# SECRET_KEY = os.environ.get('SECRET_KEY')
	# MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') 
	SECRET_KEY = '729a9670f3f001dc76d2fd7985962c98'
	SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'

	MAIL_SERVER = 'smtp.googlemail.com'
	MAIL_PORT = 587
	MAIL_USE_TLS = True


	# MAIL_USERNAME = os.environ.get('EMAIL_USER')
	# MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
	MAIL_USERNAME = 'blackguarder1987@gmail.com'
	MAIL_PASSWORD = 'cyzxojnaagrjstrz'