# project/test_basic.py

import os
import unittest
import api

class BasicTests(unittest.TestCase):

############################
#### setup and teardown ####
############################

# executed prior to each test
def setUp(self):
    api.config['TESTING'] = True
    api.config['DEBUG'] = False
    self.api = api.test_client()

# executed after each test
def tearDown(self):
    pass

###############
#### tests ####
###############

def test_main_page(self):
    response = self.api.get('/', follow_redirects=True)
    self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
