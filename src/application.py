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
class Command:
    def __init__(self, name, required_inputs):
        self.name = name
        self.required_inputs = required_inputs
    
    def prompt(self):
        params = {}
        for param in self.required_inputs:
            params[param] = input(f"Input for {param}:\t")
        return params



class Application:
    def __init__(self, conf):
        self.conf = conf
        self.commands = set()

    def register(self, command):
        self.commands.add(command)
    
    def resolve_choice_to_command(self, choice):
        try:
          return next(command for command in self.commands if command.name == choice)
        except StopIteration as si:
          return None

    def run(self):
        print(f'[x] Starting app')
        print(f'[x] Enter command')
        choice = input("::=>")
        command = self.resolve_choice_to_command(choice)
        if isinstance(command, Command):
          params = command.prompt()
          print(params)
        else:
          print("Nothing")




add = Command("ADD", ['first_name', 'last_name', 'phone_number'])
find = Command("FIND", ['attr', 'value'])
remove = Command("REMOVE", ['phone_number'])
show = Command("LIST", [])




env = os.getenv('ENVIRONMENT') or "development"
application = Application(app[env])

application.register(add)
application.register(find)
application.register(remove)
application.register(show)

application.run()
