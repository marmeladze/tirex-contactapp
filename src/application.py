import os
from config import app
from app.models import Person, PhoneBook
from app.stories import FindUserStory, AddUserStory, MainPageStory


#Load Dependencies
phone_book = PhoneBook()
person_factory = Person



#Inject Dependencies
find_user_story = FindUserStory(phone_book)
add_user_story = AddUserStory(phone_book, person_factory)
main_page_story = MainPageStory()



#Commands
commands = {
  "MAIN": main_page_story,
  "ADD": add_user_story,
  "FIND": find_user_story
}



class Application:
    def __init__(self, conf):
        self.conf = conf
        self.commands = commands
        self.last_command = "MAIN"

    def run(self):
        print(f'[x] Starting contact app')
        while self.last_command:
          res = commands[self.last_command].run()
          self.last_command = res





env = os.getenv('ENVIRONMENT') or "development"
application = Application(app[env])
application.run()
