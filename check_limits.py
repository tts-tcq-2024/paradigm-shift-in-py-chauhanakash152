def is_within_range(value, min_value, max_value):
    """Check if a value is within the specified range.

    Args:
        value (float): The value to check.
        min_value (float): The minimum acceptable value (inclusive).
        max_value (float): The maximum acceptable value (inclusive).

    Returns:
        bool: True if the value is within the range [min_value, max_value]; False otherwise.
    """
    return min_value <= value <= max_value

def battery_is_ok(temperature, soc, charge_rate):
    """Check if the battery parameters are within their acceptable ranges.

    Args:
        temperature (float): The temperature of the battery, in degrees Celsius.
        soc (float): The state of charge (SoC) percentage of the battery.
        charge_rate (float): The charge rate of the battery.

    Returns:
        bool: True if all parameters (temperature, SoC, and charge rate) 
        are within their acceptable ranges; False otherwise.
    """
    return (
        is_within_range(temperature, 0, 45) and
        is_within_range(soc, 20, 80) and
        charge_rate <= 0.8
    )

if __name__ == "__main__":
    assert battery_is_ok(25, 70, 0.7) is True
    assert battery_is_ok(50, 85, 0) is False
