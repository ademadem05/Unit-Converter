from flask import Flask, render_template, request, redirect
from unit_convertor import (
    LENGTH_UNITS, WEIGHT_UNITS, TEMPERATURE_UNITS,
    convert_length, convert_weight, convert_temperature,
)
app = Flask(__name__)


@app.route("/")
def home():
    return redirect("/length")

@app.route("/length", methods = ["GET","POST"])
def length():
    result = None
    error = None

    if request.method == "POST":
        try:
            value = float(request.form["value"])
        except ValueError:
            error = "Please enter a valid number"
        else:
            from_unit = request.form["from_unit"]
            to_unit = request.form["to_unit"]
            converted = convert_length(value, from_unit, to_unit)
            result = f"{value} {from_unit} = {round(converted, 4)} {to_unit}"
    return render_template("length.html", title = "Length", units = LENGTH_UNITS, result = result, error = error)

@app.route("/weight", methods = ["POST","GET"])
def weight():
    result = None
    error = None

    if request.method == "POST":
        try:
            value = float(request.form["value"])
        except ValueError:
            error = "Please enter a valid number"
        else:
            from_unit = request.form["from_unit"]
            to_unit = request.form["to_unit"]
            converted = convert_weight(value, from_unit, to_unit)
            result = f"{value} {from_unit} = {round(converted, 4)} {to_unit}"
    return render_template("weight.html", title = "Weight", units = WEIGHT_UNITS, result = result, error = error)


@app.route("/temperature", methods = ["POST","GET"])
def temperature():
    result = None
    error = None

    if request.method == "POST":
        try:
            value = float(request.form["value"])
        except ValueError:
            error = "Please enter a valid number"
        else:
            from_unit = request.form["from_unit"]
            to_unit = request.form["to_unit"]
            converted = convert_temperature(value, from_unit, to_unit)
            result =  result = f"{value} {from_unit} = {round(converted, 4)} {to_unit}"
    return render_template("temperature.html", title = "Temperature", units = TEMPERATURE_UNITS, error = error, result = result)



if __name__ == "__main__":
    app.run(debug=True)