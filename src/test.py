import os
import unittest

from app.models import PhoneBook, Person
from application import Application
from config import app
from app.stories import AddUserStory



class TestPersonMethods(unittest.TestCase):

    def test_person_has_full_info(self):
        person = Person(first_name="John", last_name="Malkovich", phone_number="464564")
        self.assertEqual(person.first_name, "John")
        self.assertEqual(person.last_name, "Malkovich")
        self.assertEqual(person.phone_number, "464564")




class TestPhoneBook(unittest.TestCase):

    def setUp(self):
        self.pb = PhoneBook()
        self.person_factory = Person
        self.person1 = Person(first_name="John", last_name="Malkovich", phone_number="464564")
        self.person2 = Person(first_name="Jonas", last_name="Ironside", phone_number="464456")
        self.person3 = Person(first_name="Walter",last_name="White",phone_number="453244")
        self.person4 = Person(first_name="Jesse",last_name="Pinkman",phone_number="123456")

    def test_can_instantiate_phone_book(self):
        
        self.assertIsInstance(self.pb, PhoneBook)

    def test_phone_book_has_empty_list_when_instantianized(self):
        
        collection = self.pb.collection
        self.assertIsNotNone(collection)
        self.assertEqual(collection, [])

    def test_can_add_person_to_phone_book(self):
        
        collection = self.pb.collection
        
        self.pb.add_person(self.person1)        
        self.assertIsInstance(self.person1, Person)
        self.assertEqual(len(collection), 1)


    def test_can_not_remove_unexisting_person(self):
        
        result = self.pb.remove_person(self.person1)
        self.assertFalse(result)


    def test_can_remove_person_from_phone_book(self):

        self.pb.add_person(self.person1)
        result = self.pb.remove_person(self.person1)
        self.assertTrue(result)

    def test_can_sort_phone_book(self):
        self.pb.add_person(self.person1)
        self.pb.add_person(self.person2)
        self.pb.add_person(self.person3)
        result = self.pb.sort_contact("first_name")
        self.assertTrue(result)

    def test_can_find_by_name(self):
        
        self.pb.add_person(self.person1)
        self.pb.add_person(self.person2)
        self.pb.add_person(self.person3)
        request="John"
        result=self.pb.find_by(request)
        self.assertTrue(result)

    def test_app_gets_correct_configuration(self):
        os.environ["ENVIRONMENT"] = "production"
        env = os.getenv("ENVIRONMENT")
        conf = app[env]
        application = Application(conf)
        self.assertFalse(application.conf.DEBUG,False)
        self.assertIsNone(application.conf.ROCKETS,None)        

    def test_app_gets_correct_configuration_2(self):
        os.environ["ENVIRONMENT"] = "development"
        env = os.getenv("ENVIRONMENT")
        conf = app[env]
        application = Application(conf)
        self.assertFalse(application.conf.ROCKETS,False)
        self.assertIsNone(application.conf.DEBUG,None)

    def test_app_gets_correct_configuration_3(self):
        os.environ["ENVIRONMENT"] = "test"
        env = os.getenv("ENVIRONMENT")
        conf = app[env]
        application = Application(conf)
        self.assertTrue(application.conf.ROCKETS,True)
        self.assertIsNone(application.conf.SPACE_SHIPS,None)

    
    
    def test_can_add_person_story(self):
        collection = self.pb.collection
        add_user_story = AddUserStory(self.pb,self.person_factory)
        
        add_user_story.run("jesse","pinkman","123456")
        self.assertEqual(len(collection), 1)

    






if __name__ == '__main__':
    unittest.main()