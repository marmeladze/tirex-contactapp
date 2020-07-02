import os

class Config:
	FILE_PATH = os.getenv('FILE_PATH')
	DEBUG = True

class TestConfig(Config):
	ENV = 'test'
	ROCKETS = True
	SPACE_SHIPS = None
	NAME = "kanan"
	DEBUG = True

class DevelopmentConfig(Config):
	ENV = 'development'
	ROCKETS = False
	SPACE_SHIPS = True
	NAME = "ahmad"
	DEBUG = None

class ProdutcionConfig(Config):
	ENV = 'production'
	ROCKETS = None
	SPACE_SHIPS = True
	NAME = "gafur"
	DEBUG = False

app = { 
	'test': TestConfig(),
	'development': DevelopmentConfig(),
	'production': ProdutcionConfig()
}