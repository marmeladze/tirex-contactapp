import os
from config import app
from models import Person, PhoneBook
from stories import FindUserStory



phone_book = PhoneBook()
find_user_story = FindUserStory(phone_book)
find_user_story.run()





class Application:
    def __init__(self, conf):
        self.conf = conf

    def run(self):
        print(f'[x] Starting contact app')




env = os.getenv('ENVIRONMENT')
application = Application(app[env])
application.run()
