import os
import scrumbag
import unittest
import tempfile
from pprint import pprint

class ScrumbagTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, scrumbag.app.config['DATABASE'] = tempfile.mkstemp()
        scrumbag.app.config['TESTING'] = True
        self.app = scrumbag.app.test_client()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(scrumbag.app.config['DATABASE'])

    def test_empty_db(self):
        rv = self.app.get('/')
        assert b'scrumbag' in rv.data

    def test_add_activity(self):
        activity.title
        rv = self.app.post('/addactivity', dict(searchy='Bajs'))
        assert b'Du har lagt till' + activity.title

if __name__ == '__main__':
    unittest.main()
