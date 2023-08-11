from flask import Flask, render_template

app = Flask(__name__)

menu = ["Log In", "Setting", "About"]
@app.route("/")
def index():
    return render_template("index.html", title="Flask lesson", menu=menu)


if __name__ == '__main__':
    app.run(debug=True)
