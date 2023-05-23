from flask import Flask, render_template, request

app = Flask(__name__)

app.route("/")
def index():
    return render_template("index.html", title="Habit Tracker - Home")



app.route("/add", methods=["GET", "POST"])
def add_habit():
    return render_template("add.html", title="Habit Tracker - Add Habit")