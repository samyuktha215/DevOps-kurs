"""A simple Flask application.

This module demonstrates a basic Flask application with a single route.
"""
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    """A simple Flask application.

This module demonstrates a basic Flask application with a single route.
"""
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)
