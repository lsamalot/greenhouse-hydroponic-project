
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32


def calculate_vpd(temp_c, humidity):
    """
    Simple VPD approximation.
    Future expansion.
    """

    saturation_vapor_pressure = 0.6108 * (2.71828 ** ((17.27 * temp_c) / (temp_c + 237.3)))
    actual_vapor_pressure = saturation_vapor_pressure * (humidity / 100)

    vpd = saturation_vapor_pressure - actual_vapor_pressure

    return round(vpd, 2)