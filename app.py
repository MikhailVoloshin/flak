from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
@app.route("/contact")
def contact(name=None):
    return render_template("contact.html", name=name)


@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run()
