import unittest
from check_limits import battery_is_ok

class TestBatteryIsOk(unittest.TestCase):

    def test_ok(self):
        self.assertTrue(battery_is_ok(25, 70, 0.7) is True)
