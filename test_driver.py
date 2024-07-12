from unittest import TestCase
from unittest.mock import Mock

from nemo_driver import NemoDriver


class TestKiwerDriver(TestCase):
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


class TestNemoDriver(TestCase):
    def setUp(self):
        self.sut = NemoDriver()
        self.sut.driver = Mock()

    def testLogin(self):
        # Mocking Code
        id, passwd = 'test', '1234'
        self.sut.login(id, passwd)
        self.sut.driver.cerification.assert_called_with(id, passwd)

    def testBuy(self):
        stock_code, price, count = 'APPL', 200, 123
        self.sut.buy(stock_code, price, count)
        self.sut.driver.purchasing_stock.assert_called_with(stock_code, price, count)

    def testSell(self):
        stock_code, price, count = 'APPL', 200, 123
        self.sut.sell(stock_code, price, count)
        self.sut.driver.selling_stock.assert_called_with(stock_code, price, count)

    def testCurrentPrice(self):
        stock_code = 'APPL'
        self.sut.get_price(stock_code)
        self.sut.driver.get_market_price.assert_called_with(stock_code, 0)
