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

# Warning tolerance as 5% of the upper limit
TEMP_WARNING_TOLERANCE = 0.05 * TEMP_MAX_CELSIUS
SOC_WARNING_TOLERANCE = 0.05 * SOC_MAX_PERCENTAGE
CHARGE_RATE_WARNING_TOLERANCE = 0.05 * CHARGE_RATE_MAX

# Flags to enable/disable warnings for specific parameters
WARN_TEMP = True
WARN_SOC = True
WARN_CHARGE_RATE = True


def is_within_range(
    value, min_value, max_value, parameter, tolerance=0, warn_enabled=True
):
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
    return check_value_limits(
        value, min_value, max_value, parameter
    ) and handle_warnings(
        value, min_value, max_value, tolerance, parameter, warn_enabled
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

    if min_value <= value <= min_value + tolerance:
        print_to_console(
            f"Warning: {parameter} '{value}' is approaching discharge limit"
        )
    elif max_value - tolerance <= value <= max_value:
        print_to_console(
            f"Warning: {parameter} '{value}' is approaching charge-peak limit"
        )

    return True


def print_to_console(message):
    """Print a message to the console."""
    print(message)


def battery_is_ok(temperature, soc, charge_rate):
    """Check if the battery parameters are within their acceptable ranges and handle warnings."""
    return (
        is_within_range(
            temperature,
            TEMP_MIN_CELSIUS,
            TEMP_MAX_CELSIUS,
            "Temperature",
            TEMP_WARNING_TOLERANCE,
            WARN_TEMP,
        )
        and is_within_range(
            soc,
            SOC_MIN_PERCENTAGE,
            SOC_MAX_PERCENTAGE,
            "SOC",
            SOC_WARNING_TOLERANCE,
            WARN_SOC,
        )
        and is_within_range(
            charge_rate,
            0,
            CHARGE_RATE_MAX,
            "Charge rate",
            CHARGE_RATE_WARNING_TOLERANCE,
            WARN_CHARGE_RATE,
        )
    )
