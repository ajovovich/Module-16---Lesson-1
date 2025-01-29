# test_app.py
import unittest
import json
from ..project.app import app, db, Sum 

class TestSumAPI(unittest.TestCase):

    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@localhost:3306/test_api'
        db.create_all()
        self.app = app.test_client()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_sums_by_result_success(self):
        # Add some test data to the database
        sum1 = Sum(num1=2, num2=2, result=4)
        sum2 = Sum(num1=3, num2=1, result=4)
        db.session.add_all([sum1, sum2])
        db.session.commit()

        response = self.app.get('/sum/result/4')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 2) 

    def test_get_sums_by_result_not_found(self):
        response = self.app.get('/sum/result/10') 
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['message'], "No sums found for this result.")

if __name__ == '__main__':
    unittest.main()
