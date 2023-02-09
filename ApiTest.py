import unittest
import requests
import json
import time

link = "http://localhost:5000/api"

class TestApi(unittest.TestCase):

    def api_on(self):
        response = requests.get(link + "/v1/hello")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "Hello, World!")

    def test_hello(self):
        response = requests.get(link + "/v1/hello")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "Hello, World!")

    def test_example(self):
        response = requests.get(link + "/v1/example")
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.text), 1)

if __name__ == '__main__':
    unittest.main()
