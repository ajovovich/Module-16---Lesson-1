import unittest
from app import app 

class AppTestCase(unittest.TestCase):


    def test_negative_sum(self):
        tester = app.test_client(self)
        response = tester.post('/calculate', json={'num1': 5, 'num2': -10}) 
        data = response.get_json()
        self.assertEqual(data['result'], -5) 
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
        unittest.main()
    