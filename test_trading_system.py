import random
from unittest import TestCase
from unittest.mock import Mock

from auto_trading import AutoTrading
from stock_broker_driver import IStockBrokerDriver

WRONG_CODE = 'ABCDEFG'


def get_random_code():
    pre_fixes = ['A', 'B', 'C', 'K']
    rand_ind = random.randint(0, 3)
    rand_num = random.randint(0, 999999)
    rand_num_str = '{:06}'.format(rand_num)
    return pre_fixes[rand_ind] + rand_num_str


class TestAutoTrading(TestCase):

    def setUp(self):
        self.driver = Mock(spec=IStockBrokerDriver)
        self.sut = AutoTrading()
        self.sut.select_stock_broker(self.driver)

    def test_select_stock_broker(self):
        self.sut.select_stock_broker(self.driver)

    def test_login(self):
        self.driver.login.return_value = True

        self.assertEqual(True, self.sut.login('test', '1234'))

    def test_buy(self):
        self.driver.buy.return_value = True
        self.driver.get_price.return_value = 500
        self.assertEqual(True, self.sut.buy(get_random_code(), 500, 10))

    def test_buy_with_wrong_code(self):
        self.driver.buy.return_value = True
        with self.assertRaises(AttributeError):
            self.sut.buy(WRONG_CODE, 500, 10)

    def test_buy_fail_cause_expensive(self):
        self.driver.buy.return_value = True
        self.driver.get_price.return_value = 1000001
        self.assertEqual(False, self.sut.buy(get_random_code(), 1000001, 1))

    def test_sell(self):
        ticker = get_random_code()
        self.driver.sell.return_value = True
        self.driver.get_price.return_value = 500
        self.sut.buy(ticker, 700, 5)
        self.assertEqual(True, self.sut.sell(ticker, 700, 5))

    def test_sell_with_wrong_code(self):
        self.driver.sell.return_value = True
        with self.assertRaises(AttributeError):
            self.sut.sell(WRONG_CODE, 700, 5)

    def test_sell_fail_cause_dont_have(self):
        self.driver.sell.return_value = True
        self.assertEqual(False, self.sut.sell(get_random_code(), 1000, 1))

    def test_get_price(self):
        self.driver.get_price.return_value = 500
        self.assertEqual(500, self.sut.get_price('ABC123'))

    def test_buy_nice_timing(self):
        self.driver.get_price.side_effect = [100, 110, 150]
        self.sut.buy_nice_timing('ABC123', 500)
        self.assertEqual(1, self.driver.buy.call_count)
        self.assertEqual(3, self.driver.get_price.call_count)

    def test_sell_nice_timing(self):
        self.driver.get_price.side_effect = [150, 110, 100]
        self.sut.sell_nice_timing('ABC123', 3)
        self.assertEqual(1, self.driver.sell.call_count)
        self.assertEqual(3, self.driver.get_price.call_count)

    # 보유하고 있는 현금, 주식 환산액을 반환합니다.
    def test_get_asset(self):
        remain_money, stock_money = self.sut.get_asset()
        self.assertEqual(1000000, remain_money)
        self.assertEqual(0, stock_money)


    # 종목 코드를 입력하면 그 주식의 갯수를 반환합니다.
    def test_get_stock_quantity(self):
        code1 = get_random_code()
        code2 = get_random_code()
        self.sut.buy(code1, 1000, 5)
        self.sut.buy(code2, 500, 3)

        self.assertEqual(5, self.sut.get_stock_quantity(code1))
        self.assertEqual(3, self.sut.get_stock_quantity(code2))
