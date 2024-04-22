from flask import (
    Flask,
    render_template,
    request,
    url_for,
    redirect
)

app = Flask(__name__, template_folder="templates", static_folder="static")


title_name1 = "Cost"
fruit = [
    {"f_name": "Orange","f_count": 15, "f_cost": 10.5},
    {"f_name": "Apple", "f_count": 20, "f_cost": 5.4}
]
max_score = 100
title_name = "Score"
students = [
    {"name": "Lilith", "score": 91},
    {"name": "Agia", "score": 100},
    {"name": "Patrik", "score": 50}
]


@app.route("/")
@app.route("/index")
def index():
    context = {
        "title": "Results",
        "students": students,
        "test_name": title_name,
        "max_score": max_score
    }

    fruit_info = {
        "title1": "Fruit",
        "name": title_name1,
        "fruits": fruit
    }
    return render_template("index.html", **context, **fruit_info)

@app.route("/url_for")
def my_url():
    return url_for("yes")

@app.route("/redirect")
def redirected():
    return redirect("login")

@app.route("/login", methods= ["GET", "POST"])
def login_form():
    if request.method == "POST":
        user = request.form["name"]
        return user
    else:
        #user = request.args.get["name"]
        return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True, port=8000)