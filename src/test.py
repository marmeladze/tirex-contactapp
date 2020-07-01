from app.models import PhoneBook, Person
import unittest


class TestPersonMethods(unittest.TestCase):

    def test_person_has_full_info(self):
        person = Person(first_name="John", last_name="Malkovich", phone_number="464564")
        self.assertEqual(person.first_name, "John")
        self.assertEqual(person.last_name, "Malkovich")
        self.assertEqual(person.phone_number, "464564")




class TestPhoneBook(unittest.TestCase):

    def setUp(self):
        self.pb = PhoneBook()
        self.pb_collection = self.pb.collection
        john = Person(first_name="John", last_name="Malkovich", phone_number="464564")
    
    def test_can_instantiate_phone_book(self):
        self.assertIsInstance(self.pb, PhoneBook)

    def test_phone_book_has_empty_list_when_instantianized(self):
        self.assertIsNotNone(self.pb_collection)
        self.assertEqual(self.pb_collection, [])

    def test_can_add_person_to_phone_book(self):
        person = Person(first_name="John", last_name="Malkovich", phone_number="464564")
        self.pb.add_person(person)        
        self.assertIsInstance(person, Person)
        self.assertEqual(len(self.pb_collection), 1)


    def test_can_not_remove_unexisting_person(self):
        person = Person(first_name="John", last_name="Malkovich", phone_number="464564")
        result = self.pb.remove_person(person)
        self.assertFalse(result)


    def test_can_remove_person_from_phone_book(self):
        person = Person(first_name="John", last_name="Malkovich", phone_number="464564")
        self.pb.add_person(person)
        result = self.pb.remove_person(person)
        self.assertTrue(result)

    def test_can_sort_contact_list_by_first_name(self):
        person = Person(first_name="Lamar", last_name="Taylor", phone_number="768540")
        person_two = Person(first_name="Cash", last_name="Franklin", phone_number="990540")
        self.pb.add_person(person)
        self.pb.add_person(person_two)
        result = self.pb.sort_by()
        ex_list = [person_two, person]
        self.assertEqual(ex_list, result)

    def test_can_sort_contact_list_by_last_name(self):
        person = Person(first_name="Lamar", last_name="Taylor", phone_number="768540")
        person_two = Person(first_name="Cash", last_name="Franklin", phone_number="990540")
        self.pb.add_person(person)
        self.pb.add_person(person_two)
        result = self.pb.sort_by(attr="last_name")
        ex_list = [person_two, person]
        self.assertEqual(ex_list, result)

    def test_can_sort_contact_list_by_phone_number(self):
        person = Person(first_name="Lamar", last_name="Taylor", phone_number="768540")
        person_two = Person(first_name="Cash", last_name="Franklin", phone_number="990540")
        self.pb.add_person(person)
        self.pb.add_person(person_two)
        result = self.pb.sort_by(attr="phone_number")
        ex_list = [person, person_two]
        self.assertEqual(ex_list, result)
    
    def test_can_find_by_first_name(self):
        person = Person(first_name="Lamar", last_name="Taylor", phone_number="768540")
        person_two = Person(first_name="Cash", last_name="Franklin", phone_number="990540")
        self.pb.add_person(person)
        self.pb.add_person(person_two)
        result = self.pb.find_by("first_name", "Lamar")
        self.assertEqual(result, person)



if __name__ == '__main__':
    unittest.main()