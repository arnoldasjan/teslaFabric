from unittest import TestCase

from tesla.factory import Tesla


class TestTesla(TestCase):
    def setUp(self) -> None:
        self.tesla = Tesla('Model 3', 'black')


class TestInit(TestTesla):
    def test_initial_battery_level(self) -> None:
        self.assertEqual(self.tesla.check_battery_level(), 'Battery charge level is 99.9%')

    def test_initial_lock(self) -> None:
        self.assertTrue(self.tesla.is_locked)


class TestCharge(TestTesla):
    def test_charge_battery(self):
        self.tesla.charge_battery()
        self.assertEqual(self.tesla.check_battery_level(), 'Battery charge level is 100%')


class TestUnlock(TestTesla):
    def test_unlock(self):
        self.tesla.unlock()
        self.assertFalse(self.tesla.is_locked)


