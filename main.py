from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    # return "Hello, World!"
    return render_template("home.html")


# added a route, like a subdirectory
@app.route("/salvador")
def salvador():
    return "Hello, Salvador"


# my own subdirectory
@app.route("/stowers")
def stowers():
    return "Hello, Robert.  Welcome back!"


if __name__ == "__main__":
    app.run(debug=True)