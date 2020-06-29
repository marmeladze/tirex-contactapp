import os

class Config:
	FILE_PATH = os.getenv('FILE_PATH')
	DEBUG = True

class TestConfig(Config):
	ENV = 'test'

class DevelopmentConfig(Config):
	ENV = 'development'

class ProdutcionConfig(Config):
	ENV = 'production'


app = { 
	'test': TestConfig(),
	'development': DevelopmentConfig(),
	'production': ProdutcionConfig()
}