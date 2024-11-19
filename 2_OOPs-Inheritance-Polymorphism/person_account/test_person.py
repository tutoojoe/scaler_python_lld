import unittest

from .person import Person


class TestPerson(unittest.TestCase):
    def test_constructor_with_name_only(self):
        person = Person("Alice")
        self.assertEqual(person.name, "Alice")
        self.assertFalse(hasattr(person, 'age'))

    def test_constructor_with_name_and_age(self):
        person = Person("Bob", 30)
        self.assertEqual(person.name, "Bob")
        self.assertEqual(person.age, 30)

    def test_constructor_with_no_arguments(self):
        with self.assertRaises(IndexError):
            person = Person()

    def test_constructor_with_too_many_arguments(self):
        with self.assertRaises(IndexError):
            person = Person("Alice", 25, "USA")


if __name__ == '__main__':
    unittest.main()
