# Constants defining the acceptable ranges for battery parameters

TEMP_MIN_CELSIUS = 0
"""Minimum acceptable temperature for the battery in degrees Celsius."""

TEMP_MAX_CELSIUS = 45
"""Maximum acceptable temperature for the battery in degrees Celsius."""

SOC_MIN_PERCENTAGE = 20
"""Minimum acceptable state of charge (SoC) for the battery in percentage."""

SOC_MAX_PERCENTAGE = 80
"""Maximum acceptable state of charge (SoC) for the battery in percentage."""

CHARGE_RATE_MAX = 0.8
"""Maximum acceptable charge rate for the battery (0.8 or less)."""


def is_within_range(value, min_value, max_value, parameter):
    """Check if a value is within the specified range, and print if it is too
        high or low.

    Args:
        value (float): The value of the parameter to check.
        min_value (float): The minimum acceptable value (inclusive).
        max_value (float): The maximum acceptable value (inclusive).
        parameter (str): The name of the parameter being checked.

    Returns:
        bool: True if the value is within the range [min_value, max_value];
              False otherwise. Also prints a message if the value is too
              high or low.
    """
    return parameter_to_low(value, min_value, parameter) and parameter_to_high(value, max_value, parameter) # noqa


def print_to_console(message):
    """Print a message to the console.

    Args:
        message (str): The message to be printed.
    """
    print(message)


def parameter_to_high(value, max_value, parameter):
    """Check if the parameter exceeds its maximum value.

    Args:
        value (float): The value of the parameter to check.
        max_value (float): The maximum acceptable value.
        parameter (str): The name of the parameter being checked.

    Returns:
        bool: True if the value is within the acceptable range;
              False if it is too high. Also prints a message if too high.
    """
    if value > max_value:
        print_to_console(f"{parameter} '{value}' is too high")
        return False
    return True


def parameter_to_low(value, min_value, parameter):
    """Check if the parameter is below its minimum value.

    Args:
        value (float): The value of the parameter to check.
        min_value (float): The minimum acceptable value.
        parameter (str): The name of the parameter being checked.

    Returns:
        bool: True if the value is within the acceptable range;
              False if it is too low. Also prints a message if too low.
    """
    if value < min_value:
        print_to_console(f"{parameter} '{value}' is too low")
        return False
    return True


def battery_is_ok(temperature, soc, charge_rate):
    """Check if the battery parameters are within their acceptable
    ranges.

    Args:
        temperature (float): The temperature of the battery, in degrees
        Celsius.
        soc (float): The state of charge (SoC) percentage of the battery.
        charge_rate (float): The charge rate of the battery.

    Returns:
        bool: True if all parameters (temperature, SoC, and charge rate)
        are within their acceptable ranges; False otherwise.
    """
    return (is_within_range(temperature, TEMP_MIN_CELSIUS, TEMP_MAX_CELSIUS, "Temperature") and is_within_range(soc, SOC_MIN_PERCENTAGE, SOC_MAX_PERCENTAGE, "SOC") and parameter_to_high(charge_rate, CHARGE_RATE_MAX, "Charge rate")) # noqa
