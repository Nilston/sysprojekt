import os
import unittest
import datetime
import tempfile
from pprint import pprint
from scrumbag import add_team_json

class ScrumbagTestCase(unittest.TestCase):

    def generate_valid_test_data(self):
        return dict(
            name = "Test",
            player1 = "player1",
            player2 = "player2",
            player3 = "player3",
            player4 = "player4",
            player5 = "player5",
            location = "rum 3",
            time = "22:15",
            contact = "Test",
            database='test_database.json'
        )

    # Titel
    def test_title_cant_be_empty(self):
        test_data = self.generate_valid_test_data()
        test_data['name'] = ""
        assert not add_team_json(**test_data)

    def test_title_can_have_characters(self):
        test_data = self.generate_valid_test_data()
        test_data['name'] = "Test"
        assert add_team_json(**test_data)

    def test_title_can_have_numbers(self):
        test_data = self.generate_valid_test_data()
        test_data['name'] = 1234
        assert add_team_json(**test_data)

    # Ansvarig
    def test_contact_cant_be_empty(self):
        test_data = self.generate_valid_test_data()
        test_data['contact'] = ""
        assert not add_team_json(**test_data)

    def test_contact_can_have_characters(self):
        test_data = self.generate_valid_test_data()
        test_data['contact'] = "Test"
        assert add_team_json(**test_data)

    def test_contact_cant_have_numbers(self):
        test_data = self.generate_valid_test_data()
        test_data['contact'] = 1234
        assert not add_team_json(**test_data)

    # Deltagare 1
    def test_participant1_cant_be_empty(self):
        test_data = self.generate_valid_test_data()
        test_data['player1'] = ""
        assert not add_team_json(**test_data)

    def test_participant1_cant_have_numbers(self):
        test_data = self.generate_valid_test_data()
        test_data['player1'] = 12345
        assert not add_team_json(**test_data)

    def test_participant1_can_have_characters(self):
        test_data = self.generate_valid_test_data()
        test_data['player1'] = "Test"
        assert add_team_json(**test_data)

    # Deltagare 2
    def test_participant2_can_be_empty(self):
        test_data = self.generate_valid_test_data()
        test_data['player2'] = ""
        assert add_team_json(**test_data)

    def test_participant2_cant_have_numbers(self):
        test_data = self.generate_valid_test_data()
        test_data['player2'] = 12345
        assert not add_team_json(**test_data)

    def test_participant2_can_have_characters(self):
        test_data = self.generate_valid_test_data()
        test_data['player2'] = "Test"
        assert add_team_json(**test_data)

    # Deltagare 3
    def test_participant3_can_be_empty(self):
        test_data = self.generate_valid_test_data()
        test_data['player3'] = ""
        assert add_team_json(**test_data)

    def test_participant3_cant_have_numbers(self):
        test_data = self.generate_valid_test_data()
        test_data['player3'] = 12345
        assert not add_team_json(**test_data)

    def test_participant3_can_have_characters(self):
        test_data = self.generate_valid_test_data()
        test_data['player3'] = "Test"
        assert add_team_json(**test_data)

    # Deltagare 4
    def test_participant4_can_be_empty(self):
        test_data = self.generate_valid_test_data()
        test_data['player4'] = ""
        assert add_team_json(**test_data)

    def test_participant4_cant_have_numbers(self):
        test_data = self.generate_valid_test_data()
        test_data['player4'] = 12345
        assert not add_team_json(**test_data)

    def test_participant4_can_have_characters(self):
        test_data = self.generate_valid_test_data()
        test_data['player4'] = "Test"
        assert add_team_json(**test_data)

    # Deltagare 5
    def test_participant5_can_be_empty(self):
        test_data = self.generate_valid_test_data()
        test_data['player5'] = ""
        assert add_team_json(**test_data)

    def test_participant5_cant_have_numbers(self):
        test_data = self.generate_valid_test_data()
        test_data['player5'] = 12345
        assert not add_team_json(**test_data)

    def test_participant5_can_have_characters(self):
        test_data = self.generate_valid_test_data()
        test_data['player5'] = "Test"
        assert add_team_json(**test_data)

    # Lokal
    def test_location_can_have_characters(self):
        test_data = self.generate_valid_test_data()
        test_data['location'] = "Lokal"
        assert add_team_json(**test_data)

    def test_location_can_have_numbers(self):
        test_data = self.generate_valid_test_data()
        test_data['location'] = 123456789
        assert add_team_json(**test_data)

    def test_location_cant_be_empty(self):
        test_data = self.generate_valid_test_data()
        test_data['location'] = ""
        assert not add_team_json(**test_data)

    # Tid
    def test_time_can_have_time(self):
        test_data = self.generate_valid_test_data()
        test_data['time'] = datetime.datetime.now()
        assert add_team_json(**test_data)

    def test_time_cant_have_numbers(self):
        test_data = self.generate_valid_test_data()
        test_data['time'] = 123456789
        assert not add_team_json(**test_data)

    def test_time_cant_have_characters(self):
        test_data = self.generate_valid_test_data()
        test_data['time'] = "ABC"
        assert not add_team_json(**test_data)

    def test_time_cant_be_empty(self):
        test_data = self.generate_valid_test_data()
        test_data['time'] = ""
        assert not add_team_json(**test_data)

if __name__ == '__main__':
    unittest.main()
