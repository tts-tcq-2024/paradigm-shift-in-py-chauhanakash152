def temp_is_ok(temperature):
    """Check if the temperature is within the acceptable range.

    Args:
        temperature (float): The temperature value to check, in degrees Celsius.

    Returns:
        bool: True if the temperature is between 0 and 45 degrees Celsius,
        inclusive; False otherwise.
    """
    return False if temperature < 0 or temperature > 45 else True


def soc_is_ok(soc):
    """Check if the state of charge (SoC) is within the acceptable range.

    Args:
        soc (float): The state of charge (SoC) percentage to check.

    Returns:
        bool: True if the SoC is between 20% and 80%, inclusive; False otherwise.
    """
    return False if soc < 20 or soc > 80 else True


def charge_rate_is_ok(charge_rate):
    """Check if the battery parameters are within their acceptable ranges.

    Args:
        temperature (float): The temperature of the battery, in degrees Celsius.
        soc (float): The state of charge (SoC) percentage of the battery.
        charge_rate (float): The charge rate of the battery.

    Returns:
        bool: True if all parameters (temperature, SoC, and charge rate)
        are within their acceptable ranges; False otherwise.
    """
    return False if charge_rate > 0.8 else True


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
    return temp_is_ok(temperature) and soc_is_ok(soc) and charge_rate_is_ok(charge_rate)

if __name__ == "__main__":
    assert battery_is_ok(25, 70, 0.7) is True
    assert battery_is_ok(50, 85, 0) is False
