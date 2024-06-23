from flask import Flask, render_template
from requests import get

app = Flask(__name__)
url = "https://official-joke-api.appspot.com/jokes/ten"

@app.route("/")
def main():
    info = get(url).json()
    return render_template("main.html", info=info)