
class RemoveUserStory:

    def __init__(self, phone_book):
        self.phone_book = phone_book

    def find_person(self, first_name):
        wanted_person = self.collection.find_by('first_name', first_name)
        return wanted_person

    def remove_from_contacts(self):
        self.collection.remove_person(wanted_person)
        return True