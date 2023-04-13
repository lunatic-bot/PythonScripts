from flask import Flask

app = Flask(__name__)


## route to a page in browser
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
