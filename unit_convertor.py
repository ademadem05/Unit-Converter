LENGTH_UNITS = {
    "millimeter": 0.001,
    "centimeter": 0.01,
    "meter": 1,
    "kilometer": 1000,
    "inch": 0.0254,
    "foot": 0.3048,
    "yard": 0.9144,
    "mile": 1609.344,
}

WEIGHT_UNITS = {
    "milligram": 0.001,
    "gram": 1,
    "kilogram": 1000,
    "ounce": 28.349523125,
    "pound": 453.59237,
}

TEMPERATURE_UNITS = ["celsius", "fahrenheit", "kelvin"]


def convert_length(value, from_unit, to_unit):
    meters = value * LENGTH_UNITS[from_unit]
    return meters / LENGTH_UNITS[to_unit]

def convert_weight(value, from_unit, to_unit):
    grams = value * WEIGHT_UNITS[from_unit]
    return grams / WEIGHT_UNITS[to_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == "celsius":
        celsius = value
    elif from_unit == "fahrenheit":
        celsius = (value - 32) * 5 / 9
    else:
        celsius = value - 273.15

    if to_unit == "celsius":
        return celsius
    elif to_unit == "fahrenheit":
        return celsius * 9 / 5 + 32
    else:
        return celsius + 273.15



def main():

    print(convert_length(5, "kilometer", "meter"))        # 5000.0
    print(convert_length(100, "centimeter", "inch"))      # ~39.37
    print(convert_weight(1, "kilogram", "pound"))         # ~2.2046
    print(convert_temperature(100, "celsius", "fahrenheit"))  # 212.0
    print(convert_temperature(0, "celsius", "kelvin")) 




if __name__ == "__main__":
   main()