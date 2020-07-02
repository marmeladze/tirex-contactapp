import os
from app.models import PhoneBook, Person
from app.stories import FindUserStory, RemoveUserStory
from config import app


phone_book = PhoneBook()
find_user_story = FindUserStory(phone_book)
keyword = input("Enter keyword")
find_user_story.run(keyword)


class Application:
    def __init__(self, conf):
        self.conf = conf

    def run(self):
        print(self.conf.ROCKETS)
        print(self.conf.SPACE_SHIPS)
        print(self.conf.NAME)
        print(self.conf.DEBUG)
        print(self.conf.FILE_PATH)

env = os.getenv("ENVIRONMENT")
app = Application(app[env])
app.run()