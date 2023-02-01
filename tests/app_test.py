import unittest
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, World!"

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        # create a test client for our application
        self.client = app.test_client()
        # propagate the exceptions to the test client
        self.client.testing = True

    def test_index(self):
        # send a GET request to the index endpoint
        response = self.client.get("/")
        # verify that the response contains the expected message
        self.assertIn(b"Hello, World!", response.data)

if __name__ == "__main__":
    unittest.main()
