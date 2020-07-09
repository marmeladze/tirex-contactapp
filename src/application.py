import os
from config import app
from app.models import Person, PhoneBook
from app.stories import FindUserStory
from app.stories import AddUserStory

#find-by
phone_book = PhoneBook()
find_user_story = FindUserStory(phone_book)
keyword = input("Enter keyword")
find_user_story.run(keyword)


#add-person
phone_book = PhoneBook()
first_name = input("Enter name:")
last_name = input("Enter surname:")
phone_number = input("Enter phone number:")
person = Person
add_user_story = AddUserStory(phone_book,person)
add_user_story.run(first_name,last_name,phone_number)


class Application:
    def __init__(self,conf):
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
