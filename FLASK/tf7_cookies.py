from flask import Flask, make_response, request, redirect, render_template, template_rendered

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello"


@app.route("/login/<username>")
def login(username):
    res = make_response()
    res.headers["my-header"] = "This is my header"

    res.set_cookie(
        "username",
        value=username,
        path="/",
    )
    return res


@app.route("/whoami")
def whoami():
    username = request.cookies.get("username")
    if not username:
        return redirect("/")
    return f"<h1>You are logged in as {username}</h>"


@app.route("/logout")
def logout():
    res = make_response(render_template("logout.html"))
    res.set_cookie("username", value="", expires=0)
    return res


if __name__ == '__main__':
    app.run(debug=True)
