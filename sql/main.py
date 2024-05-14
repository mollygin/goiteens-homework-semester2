from flask import (
    render_template,
    Flask,
    request
)
import sqlite3
from Database import (
    create_db,
    insert_variable,
    read_sqlite_table
)

app = Flask(__name__)
create_db()

@app.route("/")
@app.route("/home")
def index():
    return render_template("index.html")

@app.route("/join", methods=["GET", "POST"])
def join():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        joining_date = request.form["joining_date"]
        salary = request.form["salary"]

        insert_variable(name, email, joining_date, salary)
        return render_template("index.html")
    return render_template("join.html")

@app.route("/participants")
def participants():
    data = read_sqlite_table()
    return render_template("participants.html", data=data)

if __name__ == "__main__":
    app.run(debug=True, port=5200)
