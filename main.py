from flask import Flask, render_template
import properties as prop
import heat_transfer as ht

app = Flask(__name__, static_folder='static')


@app.route('/')
def index():
    return render_template('index.html')


# added a route, like a subdirectory
@app.route("/api/v1/convert/<celsius_value>")
def converter(celsius_value):
    # return str(((9 / 5) * float(celsius_value)) + 32)
    return str(ht.convert(float(celsius_value)))


# calculate conductivity
@app.route("/api/v1/conductivity/<temp_value>")
def air_cond(temp_value):
    return str(prop.conductivity('AIR', temp_value))


# calculate conductivity
@app.route("/api/v1/solve1d/<inputs>")
def solve1d(inputs):
    """
    Receives string of inputs separated by '_'

    :param inputs:
        Material, Material tk, T hot side, HTC hot side, T cold side, HTC cold side
    :return:
        Final T of solid hot side, avg, cold side
    """

    input_1d = inputs.split("_")
    # return str(ht.solver(input_1d))
    return ht.solver(input_1d)


# # added a route, like a subdirectory
# @app.route("/api/v1/salvador")
# def salvador():
#     return "Hello, Salvador"
#
#
# # my own subdirectory
# @app.route("/api/v1/stowers")
# def stowers():
#     return "Hello, Robert.  Welcome back!"


# george = "1_1_mom"
# print(solve1d(george))

if __name__ == "__main__":
    app.run(debug=True)
