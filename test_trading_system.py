from unittest import TestCase
from unittest.mock import Mock

from auto_trading import AutoTrading
from stock_broker_driver import IStockBrokerDriver


class TestAutoTrading(TestCase):

    def setUp(self):
        self.driver = Mock(spec=IStockBrokerDriver)
        self.sut = Mock()

    def test_login(self):
        # Mocking Code
        self.sut.login.return_value = True

        self.assertEqual(True, self.sut.login('test', '1234'))

    def test_buy(self):
        # Mocking Code
        self.sut.buy.return_value = True

        self.assertEqual(True, self.sut.buy('ABC123', 500, 10))

    def test_sell(self):
        # Mocking Code
        self.sut.sell.return_value = True

        self.assertEqual(True, self.sut.sell('ABC123', 700, 5))

    def test_get_price(self):
        # Mocking Code
        self.sut.get_price.return_value = 500

        self.assertEqual(int, type(self.sut.get_price('ABC123')))

    def test_buy_nice_timing(self):
        # Mocking Code
        self.driver.buy()

        self.driver.get_price.side_effect = [100, 110, 150]
        self.sut.buy_nice_timing('ABC123', 500)
        self.assertEqual(1, self.driver.buy.call_count)

    def test_sell_nice_timing(self):
        # Mocking Code
        self.driver.sell()

        self.driver.get_price.side_effect = [150, 110, 100]
        self.sut.sell_nice_timing('ABC123', 3)
        self.assertEqual(1, self.driver.sell.call_count)
