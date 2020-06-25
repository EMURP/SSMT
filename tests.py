try:
    from app import app
    import unittest
    import subprocess
except Exception as e:
    print('Some modules are missing {}'.format(e))

class TestBasicRoutes(unittest.TestCase):

    def test_home(self):
        tester = app.test_client(self)
        response = tester.get('/list_runtime', content_type='html/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.is_json, True)
        # Returns True or False.  
    def test(self):         
        self.assertTrue(True) 
    
if __name__ == '__main__':
    unittest.main()
    subprocess.check_output(['bash','config.sh'])
