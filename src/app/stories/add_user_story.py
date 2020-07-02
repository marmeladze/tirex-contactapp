class AddUserStory:
    def __init__(self,phonebook,person_factory):
        self.phonebook=phonebook
        self.person_factory=person_factory

    def run(self,first_name,last_name,phone_number):
        person=self.person_factory(first_name=first_name,last_name=last_name,phone_number=phone_number)
        
        return self.phonebook.add_person(person)