class PhoneBook:
    def __init__(self):
        self.collection = []

    def add_person(self, person):
        self.collection.append(person)
        print(self.collection)
        return True
        #with open('contacts.txt', 'r+') as file:
            #collection = file.read()
            #file.write(person)
            #return collection

    def remove_person(self, person):
        if person in self.collection:    
            self.collection.remove(person)
            print(self.collection)
            return True
        return False   
        #with open('contacts.txt', 'r+') as file:
            #collection = file.readlines()
            #collection.remove(person)
            #file.seek(0)
            #file.writelines(collection)

    def sort_contact(self,attr):
        self.collection.sort(key=lambda p: getattr(p,attr))
        print(self.collection)
        return True
        #with open('contacts.txt', 'r+') as file:
            #collection = file.readlines()
            #collection.sort()
            #print(collection)

    def find_by(self,**kwargs):
        attr = kwargs["attr"]
        value = kwargs["value"]
        return [person for person in self.collection if getattr(person,attr)==value]