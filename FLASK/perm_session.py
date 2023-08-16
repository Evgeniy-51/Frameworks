from  flask import Flask, request, render_template, redirect, url_for

app= Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("perm_sess_login.html")


@app.route("/<usr>")
def user(usr):
    return f"<h>{usr}</h1>"


if __name__ == '__main__':
    app.run(debug=True)