from unittest import TestCase
from unittest.mock import Mock
from kiwer_driver import KiwerDriver

class TestKiwerDriver(TestCase):
    def setUp(self):
        # self.sut = Mock()
        self.sut = KiwerDriver()

    def testLogin(self):
        # Mocking Code
        # self.sut.login.return_value = True

        self.assertEqual(True, self.sut.login('test', '1234'))

    def testBuy(self):
        # Mocking Code
        # self.sut.buy.return_value = True

        self.assertEqual(True, self.sut.buy('ABC123', 500, 10))

    def testSell(self):
        # Mocking Code
        # self.sut.sell.return_value = True

        self.assertEqual(True, self.sut.sell('ABC123', 700, 5))

    def testCurrentPrice(self):
        # Mocking Code
        # self.sut.get_price.return_value = 123

        self.assertEqual(int, type(self.sut.get_price('ABC123')))


class TestNemoDriver(TestCase):
    def setUp(self):
        self.sut = Mock()

    def testLogin(self):
        # Mocking Code
        self.sut.login.return_value = True

        self.assertEqual(True, self.sut.login('test', '1234'))

    def testBuy(self):
        # Mocking Code
        self.sut.buy.return_value = True

        self.assertEqual(True, self.sut.buy('ABC123', 500, 10))

    def testSell(self):
        # Mocking Code
        self.sut.sell.return_value = True

        self.assertEqual(True, self.sut.sell('ABC123', 700, 5))

    def testCurrentPrice(self):
        # Mocking Code
        self.sut.get_price.return_value = 123

        self.assertEqual(int, type(self.sut.get_price('ABC123')))
