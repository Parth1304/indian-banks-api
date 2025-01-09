import unittest
from app import app  
class FlaskAppTestCase(unittest.TestCase):

    def setUp(self):
        # Create a test client for the Flask app
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        # Test the home route ("/")
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('message', response.get_json())
        self.assertEqual(response.get_json()['message'], "Above are the API endpoints for getting bank details")

    def test_get_banks(self):
        # Test the "/get/banks" route
        response = self.app.get('/get/banks')
        self.assertEqual(response.status_code, 200)

        # Check that the response contains a list of banks
        banks = response.get_json()
        self.assertIsInstance(banks, list)

        # Check if each bank entry has id and name
        for bank in banks:
            self.assertIn('id', bank)
            self.assertIn('name', bank)

    def test_get_branch_by_ifsc(self):
        # Test the "/get/branch/<ifsc>" route 
        valid_ifsc = "ABHY0065003"  
        response = self.app.get(f'/get/branch/{valid_ifsc}')
        self.assertEqual(response.status_code, 200)
        
        branch = response.get_json()
        self.assertIn('ifsc', branch)
        self.assertIn('branch', branch)
        self.assertIn('address', branch)
        self.assertIn('city', branch)
        self.assertIn('district', branch)
        self.assertIn('state', branch)
        self.assertIn('bank_name', branch)

        # Test with an invalid IFSC
        invalid_ifsc = "INVALID000000"
        response = self.app.get(f'/get/branch/{invalid_ifsc}')
        self.assertEqual(response.status_code, 404)
        self.assertIn('error', response.get_json())
        self.assertEqual(response.get_json()['error'], 'Branch not found')

if __name__ == '__main__':
    unittest.main()
