from unittest import TestCase
from unittest.mock import Mock
from kiwer_driver import KiwerDriver

from nemo_driver import NemoDriver


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
        self.sut = NemoDriver()

    def testLogin(self):
        # Mocking Code
        id, passwd = 'test', '1234'
        self.assertTrue(self.sut.login(id, passwd))

    def testBuy(self):
        stock_code, price, count = 'APPL', 200, 123
        self.assertTrue(self.sut.buy(stock_code, price, count))

    def testSell(self):
        stock_code, price, count = 'APPL', 200, 123
        self.assertTrue(self.sut.sell(stock_code, price, count))

    def testCurrentPrice(self):
        stock_code = 'APPL'
        self.assertTrue(self.sut.get_price(stock_code))
