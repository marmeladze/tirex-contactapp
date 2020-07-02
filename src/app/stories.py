from models import PhoneBook, Person

class FindUserStory:

    def __init__(self, phone_book):
        self.phone_book = phone_book


    def run(self):
        keyword = self.get_input()
        validated = self.validate_input(keyword)
        if validated:
            results = self.phone_book.find_by(keyword)
        else:
            results = self.validation_error_message(validated)

        return results

    def get_input(self):
        keyword = input("Enter keyword")
        return keyword

    def validate_input(self, keyword):
        return False if "%" in keyword else True

    def validation_error_message(validated):
        return {"message": "Keyword can not contain %"}




class RemovePersonStory:

    def __init__(self, phone_book):
        self.phone_book = phone_book

    def get_input(self):
        first_name = input("Enter the First name:\t")
        last_name = input("Enter the Last name:\t")
        return first_name
    
    def find_person(self):
        wanted_person = self.collection.find_by(first_name)
        return wanted_person

    def confirm_removing(self):
        confirm = input(f'Are you sure that you want remove {wanted_person} from contact list?')
        return confirm if confirm=="yes" else "Contact isn't deleted from contact list"

    def remove_from_contacts(self):
        self.collection.remove_person(wanted_person)
        return True
