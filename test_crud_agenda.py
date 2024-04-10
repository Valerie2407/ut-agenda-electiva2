import unittest
from crud_agenda import Agenda

class TestAgenda(unittest.TestCase):
    def setUp(self):
        self.agenda = Agenda()
        self.agenda.add_contact("Alice", "123456789")
        self.agenda.add_contact("Bob", "987654321")

    def test_add_contact(self):
        self.agenda.add_contact("Charlie", "456789123")
        self.assertEqual(len(self.agenda.get_contacts()), 3)

    def test_update_contact(self):
        self.assertTrue(self.agenda.update_contact("Alice", "111111111"))
        self.assertFalse(self.agenda.update_contact("David", "000000000"))

    def test_delete_contact(self):
        self.assertTrue(self.agenda.delete_contact("Bob"))
        self.assertFalse(self.agenda.delete_contact("Eve"))

if __name__ == '__main__':
    unittest.main()