# Constants defining the acceptable ranges for battery parameters

TEMP_MIN_CELSIUS = 0
TEMP_MAX_CELSIUS = 45
SOC_MIN_PERCENTAGE = 20
SOC_MAX_PERCENTAGE = 80
CHARGE_RATE_MAX = 0.8

# constants defining the percetage tolerance
TEMP_WARNING_PERCENTAGE = 5
SOC_WARNING_PERCENTAGE = 5
CHARGE_RATE_WARNING_PERCENTAGE = 5

# Warning tolerance
temp_warning_tolerance = (temp_warning_percentage / 100) * temp_max_celsius
soc_warning_tolerance = (soc_warning_percentage / 100) * soc_max_percentage
charge_rate_warning_tolerance = (charge_rate_warning_percentage / 100) * charge_rate_max

# Flags to enable/disable warnings for specific parameters
WARN_TEMP = True
WARN_SOC = True
WARN_CHARGE_RATE = True


def is_within_range(value, min_value, max_value, parameter, tolerance=0, warn_enabled=True):
    """Check if a value is within the specified range, print if it is too high or low,
    and issue early warnings based on the tolerance.

    Args:
        value (float): The value of the parameter to check.
        min_value (float): The minimum acceptable value (inclusive).
        max_value (float): The maximum acceptable value (inclusive).
        parameter (str): The name of the parameter being checked.
        tolerance (float): Tolerance value to issue warnings for approaching limits.
        warn_enabled (bool): Flag to enable/disable warnings for this parameter.
    
    Returns:
        bool: True if the value is within the range [min_value, max_value];
              False otherwise. Also prints messages if the value is too high/low or in the warning zone.
    """
    return (
        check_value_limits(value, min_value, max_value, parameter) and
        handle_warnings(value, min_value, max_value, tolerance, parameter, warn_enabled)
    )


def check_value_limits(value, min_value, max_value, parameter):
    """Check if the value is within the limits."""
    if value < min_value:
        print_to_console(f"{parameter} '{value}' is too low")
        return False
    if value > max_value:
        print_to_console(f"{parameter} '{value}' is too high")
        return False
    return True


def handle_warnings(value, min_value, max_value, tolerance, parameter, warn_enabled):
    """Handle early warning messages if the value is approaching limits."""
    if not warn_enabled:
        return True

    approaching_limit = check_approaching_limits(value, min_value, max_value, tolerance)
    if approaching_limit:
        print_to_console(f"Warning: {parameter} '{value}' is approaching {approaching_limit} limit")

    return True


def check_approaching_limits(value, min_value, max_value, tolerance):
    """Check if the value is approaching the minimum or maximum limit and return a label."""
    if min_value <= value <= min_value + tolerance:
        return "discharge"
    if max_value - tolerance <= value <= max_value:
        return "charge-peak"
    return None


def print_to_console(message):
    """Print a message to the console."""
    print(message)


def battery_is_ok(temperature, soc, charge_rate):
    """Check if the battery parameters are within their acceptable ranges and handle warnings."""
    return (
        is_within_range(
            temperature, TEMP_MIN_CELSIUS, TEMP_MAX_CELSIUS, "Temperature", 
            temp_warning_tolerance, WARN_TEMP
        ) and is_within_range(
            soc, SOC_MIN_PERCENTAGE, SOC_MAX_PERCENTAGE, "SOC", 
            soc_warning_tolerance, WARN_SOC
        ) and is_within_range(
            charge_rate, 0, CHARGE_RATE_MAX, "Charge rate", 
            charge_rate_warning_tolerance, WARN_CHARGE_RATE
        )
    )
