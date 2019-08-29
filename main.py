from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, World!"


# added a route, like a subdirectory
# pushing update check within PyCharm to Git repo
@app.route("/salvador")
def salvador():
    return "Hello, Salvador"


if __name__ == "__main__":
    app.run(debug=True)