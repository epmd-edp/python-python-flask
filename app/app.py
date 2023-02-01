from flask import Flask
"""Example of flask main file."""
app = Flask(__name__)

@app.route('/')
def hello_world():
    """Returns Hello, World."""
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
