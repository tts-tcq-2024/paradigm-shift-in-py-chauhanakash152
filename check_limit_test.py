import unittest
from check_limits import battery_is_ok

class TestBatteryIsOk(unittest.TestCase):

    def test_battery_ok_typical_values(self):
        self.assertTrue(battery_is_ok(25, 70, 0.7))
        self.assertTrue(battery_is_ok(30, 50, 0.8))
        self.assertTrue(battery_is_ok(25, 30, 0.5))

    def test_battery_ok_boundary_values(self):
        self.assertTrue(battery_is_ok(0, 20, 0.8))
        self.assertTrue(battery_is_ok(45, 80, 0.8))

    def test_battery_not_ok_invalid_scenarios(self):
        self.assertFalse(battery_is_ok(-1, 70, 0.7))  # Temperature below minimum
        self.assertFalse(battery_is_ok(25, 19, 0.7))  # SoC below minimum
        self.assertFalse(battery_is_ok(25, 70, 0.9))  # Charge rate above maximum
        self.assertFalse(battery_is_ok(46, 70, 0.7))  # Temperature above maximum
        self.assertFalse(battery_is_ok(25, 81, 0.7))  # SoC above maximum
        self.assertFalse(battery_is_ok(25, 70, 0.81))  # Charge rate above maximum

    def test_battery_ok_edge_cases(self):
        self.assertTrue(battery_is_ok(0, 20, 0.8))  # Lower bounds
        self.assertTrue(battery_is_ok(45, 80, 0.8))  # Upper bounds

    def test_battery_not_ok_edge_cases(self):
        self.assertFalse(battery_is_ok(0, 81, 0.8))  # SoC above max, temp at lower bound
        self.assertFalse(battery_is_ok(46, 20, 0.8))  # Temp above max, SoC at lower bound
        self.assertFalse(battery_is_ok(25, 80, 0.81))  # Charge rate above max, valid temp/SoC

if __name__ == '__main__':
    unittest.main()
