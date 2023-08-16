from flask import Flask, request, render_template, redirect, url_for, session, flash
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "0"
app.permanent_session_lifetime = timedelta(days=10)


@app.route("/")
def home():
    return render_template("perm_sess_base.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user
        flash("Login successful!")
        return redirect((url_for("user")))
    else:
        if "user" in session:
            flash("Already Logged In!")
            return redirect(url_for('user'))
    return render_template("perm_sess_login.html")


@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return render_template("perm_sess_user.html", user=user)
    else:
        flash("You're not logged in!")
        redirect(url_for("login"))
    # return f"<h>Hello, {user}!</h1>"


@app.route("/logout")
def logout():
    if "user" in session:
        flash(f"You've been logged out, {user}!", "info")
        session.pop("user", None)
        return redirect(url_for("login"))


if __name__ == '__main__':
    app.run(debug=True)
