from models import PhoneBook, Person

class FindUserStory:

    def __init__(self, phone_book):
        self.phone_book = phone_book


    def run(self, keyword):
        validated = self.validate_input(keyword)
        if validated:
            results = self.phone_book.find_by(keyword)
        else:
            results = self.validation_error_message(validated)
        return results

    def validate_input(self, keyword):
        return False if "%" in keyword else True

    def validation_error_message(validated):
        return {"message": "Keyword can not contain %"}





class RemoveUserStory:

    def __init__(self, phone_book):
        self.phone_book = phone_book

    def find_person(self, first_name):
        wanted_person = self.collection.find_by('first_name', first_name)
        return wanted_person

    def remove_from_contacts(self):
        self.collection.remove_person(wanted_person)
        return True
