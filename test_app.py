import unittest
from app import app

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        pass


    def test_index_page(self):
        """Ensure the index page loads correctly."""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Temperature Converter', response.data)  


    def test_temperature_conversion(self):
        """Ensure the temperature conversion works correctly."""
        response = self.app.get('/convert?celsius=100')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'"fahrenheit": 212.0', response.data) 

    def test_default_conversion(self):
        """Ensure default conversion works when no parameter is provided."""
        response = self.app.get('/convert')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'"fahrenheit": 32.0', response.data) 

    def test_invalid_input(self):
        """Test with invalid input to see how it's handled."""
        response = self.app.get('/convert?celsius=abc')
        self.assertEqual(response.status_code, 400)  

if __name__ == '__main__':
    unittest.main()
