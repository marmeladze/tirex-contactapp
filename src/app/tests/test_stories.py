import unittest

from models import *
from stories import *


class TestStories(unittest.TestCase):
    def setUp(self):
        phone_book = PhoneBook()
        person_factory = Person
        self.add_user_story = AddUserStory(phone_book, person_factory)

    def test_can_add_person(self):
        self.assertFalse(True)

    def test_fail_when_missing_params(self):
        self.assertFalse(True)

    def test_can_remove_person(self):
        self.assertFalse(True)

    def test_can_not_remove_if_person_not_in_contacts(self):
        self.assertFalse(True)

    def test_can_find_person_by_name(self):
        self.assertFalse(True) 

    def test_can_find_person_by_last_name(self):
        self.assertFalse(True)

    def test_can_find_person_by_phone_number(self):
        # ... 
        # ... 
        number = "345345346"
        person = find_user_story(phone=number)
        assertEqual(person.phone_number, number)
        assertTrue(isinstance(person, Person))

    def test_returns_empty_list_when_not_found(self):
        name = "Səməd"
        result = find_user_story(name=name)
        self.assertEqual(result, [])

    def test_sort_contacts(self):
        self.add_user_story(p1) #Ziya
        self.add_user_story(p2) #Babək
        results = self.sort_contacts_story()
        self.assertEqual(results, [p2, p1])

    def test_list_users(self):
        self.add_user_story(p1) #Ziya
        self.add_user_story(p2) #Babək
        results = self.list_users_story()
        self.assertEqual(results, [p1, p2])

    def test_list_users(self):
        results = self.list_users_story()
        self.assertEqual(results, [])
