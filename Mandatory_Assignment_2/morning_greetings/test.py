# test.py
import unittest  # Ensure unittest is imported
import os
import datetime
from contacts_manager import ContactsManager
from message_generator import generate_message
from message_sender import send_message
from logger import log_message

class TestMorningGreetings(unittest.TestCase):

    def setUp(self):
        """Set up a temporary contacts manager for testing."""
        self.cm = ContactsManager(file_name='test_contacts.json')
        self.cm.add_contact("Test User", "test@example.com", "08:00 AM")

    def tearDown(self):
        """Clean up by removing the test file after tests."""
        if os.path.exists('test_contacts.json'):
            os.remove('test_contacts.json')
        if os.path.exists('message_log.txt'):
            os.remove('message_log.txt')

    def test_add_contact(self):
        """Test adding a contact."""
        self.cm.add_contact("New User", "new@example.com", "09:00 AM")
        contacts = self.cm.get_contacts()
        self.assertEqual(len(contacts), 2)
        self.assertEqual(contacts[1]['name'], "New User")

    def test_remove_contact(self):
        """Test removing a contact."""
        self.cm.remove_contact("Test User")
        contacts = self.cm.get_contacts()
        self.assertEqual(len(contacts), 0)

    def test_generate_message(self):
        """Test message generation based on the current day."""
        message = generate_message("Test User")

        # Determine the expected message based on the current day of the week
        day_of_week = datetime.datetime.now().weekday()

        weekday_messages = {
            0: "Start your week with energy!",  # Monday
            1: "Keep going, you're doing great!",  # Tuesday
            2: "Halfway there!",  # Wednesday
            3: "Almost at the finish line!",  # Thursday
            4: "It's Friday! Time to relax.",  # Friday
            5: "Enjoy your weekend!",  # Saturday
            6: "Recharge and prepare for the week ahead!",  # Sunday
        }

        expected_message = f"Good Morning, Test User! {weekday_messages.get(day_of_week, 'Have a great day!')}"
        self.assertEqual(message, expected_message)

    def test_send_message(self):
        """Test message sending simulation."""
        with self.assertRaises(ValueError):
            send_message("", "Test Message")
        send_message("test@example.com", "Test Message")  # Should not raise an error

    def test_log_message(self):
        """Test logging a message."""
        contact = {'name': "Test User", 'email': "test@example.com"}
        log_message(contact, "Test Message")
        with open('message_log.txt', 'r') as log_file:
            log = log_file.read()
            self.assertIn("Test Message", log)

if __name__ == '__main__':
    unittest.main()
