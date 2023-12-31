from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return "INDEX"

@app.route("/about")
def about():
    return "<h1>About Us<h1>"

if __name__ == '__main__':
    app.run(debug=True)