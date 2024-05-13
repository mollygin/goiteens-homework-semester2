from flask import Flask, render_template

site = Flask(__name__)

@site.route("/")
def first_p():
    return render_template("page1.html", title="Flowers")

@site.route("/lily")
def lily():
    return render_template("lily.html", title="Lily")

@site.route("/dahlia")
def dahlia():
    return render_template("dahlia.html", title="Dahlia")

@site.route("/valley_lily")
def valley_lily():
    return render_template("valley_lily.html", title="Lily of the valley")

if __name__ == "__main__":
    site.run(debug=True, port=9000)