from flask import Blueprint, redirect, render_template

main = Blueprint("main", __name__)


@main.route("/")
def homepage():
    return redirect("/ui")


@main.route("/about")
def about_page():
    context = {"title": "About page"}
    return render_template("about.html", **context)
