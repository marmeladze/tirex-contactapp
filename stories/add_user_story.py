# ask =>  name:
#         surname:
#         phone_number: 
# if features already exist in phone_book inform user that person exists in phonebook
# otherwise add person to contact and alert information to user for checking
# then return commands section

class AddUserStory:
    def __init__(self,phonebook,person_factory):
        self.phonebook=phonebook
        self.person_factory=person_factory

    def run(self,first_name,last_name,phone_number):
        validated = self.validation(first_name,last_name,phone_number)
        if validated:
            person = self.person_factory(first_name=first_name,last_name=last_name,phone_number=phone_number)
            return self.phonebook.add_person(person)
        else:
            return self.validation_error()

    def validation(self,first_name,last_name,phone_number):
        return True if first_name or last_name or phone_number != "" else False 

    def validation_error(self):
        return "Missing parameter!"