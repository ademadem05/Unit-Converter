from flask import Flask, render_template, request, redirect
from unit_convertor import LENGTH_UNITS, convert_length
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
    return render_template("length.html", units = LENGTH_UNITS, result = result, error = error)

if __name__ == "__main__":
    app.run(debug=True)