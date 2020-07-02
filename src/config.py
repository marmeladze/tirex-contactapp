import os

class Config:
	FILE_PATH = os.getenv('FILE_PATH')
	DEBUG = True

class TestConfig(Config):
	ROCKETS = True
	SPACE_SHIPS = False
	NAME = "Ziya"

class DevelopmentConfig(Config):
	ROCKETS = False
	SPACE_SHIPS = True
	NAME = "Ayiz"


class ProdutcionConfig(Config):
	ROCKETS = None
	SPACE_SHIPS = None
	NAME = "/\/\/"



app = { 
	'test': TestConfig(),
	'development': DevelopmentConfig(),
	'production': ProdutcionConfig()
}