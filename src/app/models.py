class PhoneBook:
	def __init__(self):
		self.collection = []

	def add_person(self, person):
		self.collection.append(person)
		return True

	def remove_person(self, person):
		if person in self.collection:
			self.collection.remove(person)
			return True
		return False 

	def sort_by(self, attr="first_name"):
		self.collection.sort(key=lambda p: getattr(p, attr))
		return self.collection

	def find_by(self, attr, value):
		try:
			name = [person for person in self.collection if getattr(person, attr) == value]
			name_generator = next(person for person in self.collection if getattr(person, attr) == value)
			return name_generator
		except AttributeError as e:
			print('Error')
			return []




class Person:
	def __init__(self, first_name, last_name, phone_number):
		self.first_name = first_name
		self.last_name = last_name
		self.phone_number = phone_number

