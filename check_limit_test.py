import unittest
from check_limits import battery_is_ok

class TestBatteryIsOk(unittest.TestCase):

    def test_battery_is_ok_with_valid_parameters(self):
        """Test the `battery_is_ok` function with a set of valid parameter values.

        This test verifies that the `battery_is_ok` function correctly returns `True`
        for a range of typical, valid parameter values. The function iterates through
        a list of predefined parameter tuples representing valid temperature, state of
        charge (SoC), and charge rate values, and asserts that `battery_is_ok` returns
        `True` for each set of values.

        The following valid parameter sets are tested:
        - Temperature: 25°C, SoC: 70%, Charge Rate: 0.7
        - Temperature: 30°C, SoC: 50%, Charge Rate: 0.8
        - Temperature: 25°C, SoC: 30%, Charge Rate: 0.5

        This ensures that the function behaves as expected when provided with standard
        and typical input values within acceptable ranges.
        """
        valid_parameters = [
            (25, 70, 0.7),
            (30, 50, 0.8),
            (25, 30, 0.5)
        ]
        for temp, soc, charge_rate in valid_parameters:
            self.assertTrue(battery_is_ok(temp, soc, charge_rate))

    def test_battery_ok_boundary_values(self):
        """Test the `battery_is_ok` function with boundary parameter values.

        This test verifies that the `battery_is_ok` function correctly returns `True`
        for parameter values that are at the edge of acceptable ranges. The function
        iterates through a list of predefined boundary parameter tuples representing
        the lower and upper limits for temperature, state of charge (SoC), and charge rate,
        and asserts that `battery_is_ok` returns `True` for each set of boundary values.

        The following boundary parameter sets are tested:
        - Temperature: 0°C, SoC: 20%, Charge Rate: 0.8 (Lower bounds)
        - Temperature: 45°C, SoC: 80%, Charge Rate: 0.8 (Upper bounds)

        This ensures that the function handles values at the edges of acceptable ranges
        correctly, validating the boundaries of the acceptable input parameters.
        """
        boundary_parameters = [
            (0, 20, 0.8),
            (45, 80, 0.8)
        ]
        for temp, soc, charge_rate in boundary_parameters:
            self.assertTrue(battery_is_ok(temp, soc, charge_rate))

    def test_battery_is_ok_temperature_below_minimum(self):
        """
        Test the `battery_is_ok` function when the temperature is below the minimum acceptable limit.
        
        This test case verifies that `battery_is_ok` correctly returns `False` when the temperature 
        parameter is set to -1°C, which is below the acceptable minimum value, while other parameters 
        are within acceptable ranges.
        """
        self.assertFalse(battery_is_ok(-1, 70, 0.7))  # Temperature below minimum

    def test_battery_is_ok_soc_below_minimum(self):
        """
        Test the `battery_is_ok` function when the state of charge (SoC) is below the minimum acceptable limit.
        
        This test case verifies that `battery_is_ok` correctly returns `False` when the SoC parameter 
        is set to 19%, which is below the acceptable minimum value, while other parameters are within 
        acceptable ranges.
        """
        self.assertFalse(battery_is_ok(25, 19, 0.7))  # SoC below minimum

    def test_battery_is_ok_charge_rate_above_maximum(self):
        """
        Test the `battery_is_ok` function when the charge rate is above the maximum acceptable limit.
        
        This test case verifies that `battery_is_ok` correctly returns `False` when the charge rate 
        parameter is set to 0.9, which is above the acceptable maximum value, while other parameters 
        are within acceptable ranges.
        """
        self.assertFalse(battery_is_ok(25, 70, 0.9))  # Charge rate above maximum

    def test_battery_is_ok_temperature_above_maximum(self):
        """
        Test the `battery_is_ok` function when the temperature is above the maximum acceptable limit.
        
        This test case verifies that `battery_is_ok` correctly returns `False` when the temperature 
        parameter is set to 46°C, which is above the acceptable maximum value, while other parameters 
        are within acceptable ranges.
        """
        self.assertFalse(battery_is_ok(46, 70, 0.7))  # Temperature above maximum

    def test_battery_is_ok_soc_above_maximum(self):
        """
        Test the `battery_is_ok` function when the state of charge (SoC) is above the maximum acceptable limit.
        
        This test case verifies that `battery_is_ok` correctly returns `False` when the SoC parameter 
        is set to 81%, which is above the acceptable maximum value, while other parameters are within 
        acceptable ranges.
        """
        self.assertFalse(battery_is_ok(25, 81, 0.7))  # SoC above maximum

    def test_battery_is_ok_charge_rate_above_maximum_redundant(self):
        """
        Test the `battery_is_ok` function when the charge rate is above the maximum acceptable limit.
        
        This test case verifies that `battery_is_ok` correctly returns `False` when the charge rate 
        parameter is set to 0.81, which is above the acceptable maximum value, while other parameters 
        are within acceptable ranges.
        """
        self.assertFalse(battery_is_ok(25, 70, 0.81))  # Charge rate above maximum

    def test_battery_not_ok_soc_above_max(self):
        """
        Test the `battery_is_ok` function when state of charge (SoC) is above the maximum limit.
        
        This test case verifies that `battery_is_ok` correctly returns `False` when the 
        SoC parameter is set to 81%, which is above the acceptable maximum value, while 
        other parameters are within acceptable ranges.
        """
        self.assertFalse(battery_is_ok(0, 81, 0.8))  # SoC above max, temp at lower bound

    def test_battery_not_ok_temp_above_max(self):
        """
        Test the `battery_is_ok` function when temperature is above the maximum limit.
        
        This test case verifies that `battery_is_ok` correctly returns `False` when the 
        temperature parameter is set to 46°C, which is above the acceptable maximum value, 
        while other parameters are within acceptable ranges.
        """
        self.assertFalse(battery_is_ok(46, 20, 0.8))  # Temp above max, SoC at lower bound

    def test_battery_not_ok_charge_rate_above_max(self):
        """
        Test the `battery_is_ok` function when charge rate is above the maximum limit.
        
        This test case verifies that `battery_is_ok` correctly returns `False` when the 
        charge rate parameter is set to 0.81, which is above the acceptable maximum value, 
        while other parameters are within acceptable ranges.
        """
        self.assertFalse(battery_is_ok(25, 80, 0.81))  # Charge rate above max, valid temp/SoC


if __name__ == '__main__':
    unittest.main()
