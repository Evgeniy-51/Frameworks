from flask import Flask, request, url_for, render_template

app = Flask(__name__)

menu = [
    {'name': 'Login', 'url': 'tf_5_form.html'},
    {'name': 'First Application', 'url': 'first-app'},
    {'name': 'Feedback', 'url': 'contact'},
]


@app.route("/")
def index():
    print(url_for("index"))
    return render_template("tf_5_base.html", menu=menu)


@app.route("/contact", methods=["POST"])
def contact():
    if request.method == "POST":
        print(request.form["username"])
    return render_template("tf_5_form.html", title="Login", menu=menu)


if __name__ == '__main__':
    app.run(debug=True)
