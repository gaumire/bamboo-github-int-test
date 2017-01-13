

from flaskapp import app as myapp
import unittest
import os
import xmlrunner


class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = myapp.test_client()

    def tearDown(self):
        pass

    def test_index(self):
        rv = self.app.get('/')
        assert "Hello, world!" in rv.data


if __name__ == '__main__':
    test_dir = os.environ.get('TEST_DIR', 'shippable/testresults')
    unittest.main(
        testRunner=xmlrunner.XMLTestRunner(
            output=test_dir
        )
    )
