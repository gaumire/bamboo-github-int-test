

from flaskapp import app as myapp
import unittest
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
    unittest.main(
        testRunner=xmlrunner.XMLTestRunner(
            output='test-reports'
        )
    )
