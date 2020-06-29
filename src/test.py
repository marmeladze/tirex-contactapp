from app.models import PhoneBook, Person
import unittest


class TestPersonMethods(unittest.TestCase):

    def test_person_has_full_info(self):
        person = Person(first_name="John", last_name="Malkovich", phone_number="464564")
        self.assertEqual(person.first_name, "John")
        self.assertEqual(person.last_name, "Malkovich")
        self.assertEqual(person.phone_number, "464564")




class TestPhoneBook(unittest.TestCase):

    def test_can_instantiate_phone_book(self):
        pb = PhoneBook()
        self.assertIsInstance(pb, PhoneBook)

    def test_phone_book_has_empty_list_when_instantianized(self):
        pb = PhoneBook()
        collection = pb.collection
        self.assertIsNotNone(collection)
        self.assertEqual(collection, [])

    def test_can_add_person_to_phone_book(self):
        pb = PhoneBook()
        collection = pb.collection
        person = Person(first_name="John", last_name="Malkovich", phone_number="464564")
        pb.add_person(person)        
        self.assertIsInstance(person, Person)
        self.assertEqual(len(collection), 1)


    def test_can_not_remove_unexisting_person(self):
        pb = PhoneBook()
        person = Person(first_name="John", last_name="Malkovich", phone_number="464564")
        result = pb.remove_person(person)
        self.assertFalse(result)


    def test_can_remove_person_from_phone_book(self):
        pb = PhoneBook()
        person = Person(first_name="John", last_name="Malkovich", phone_number="464564")
        pb.add_person(person)
        result = pb.remove_person(person)
        self.assertTrue(result)



if __name__ == '__main__':
    unittest.main()