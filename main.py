from flask import Flask, render_template

app = Flask(__name__, static_folder='static')


@app.route('/')
def index():
    return render_template('index.html')


# added a route, like a subdirectory
@app.route("/api/v1/convert/<celsius_value>")
def converter(celsius_value):
    return str(((9 / 5) * float(celsius_value)) + 32);


# added a route, like a subdirectory
@app.route("/api/v1/salvador")
def salvador():
    return "Hello, Salvador"


# my own subdirectory
@app.route("/api/v1/stowers")
def stowers():
    return "Hello, Robert.  Welcome back!"


if __name__ == "__main__":
    app.run(debug=True)
