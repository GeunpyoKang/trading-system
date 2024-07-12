from IStockBrokerDriver import IStockBrokerDriver
from kiwer_api import KiwerAPI
from nemo_api import NemoAPI

from unittest.mock import Mock


class KiwerDriver(IStockBrokerDriver):
    def __init__(self):
        self.__driver = KiwerAPI()

    def login(self, id: str, password: str):
        self.__driver.login(id, password)

    def buy(self, stock_code: str, price: int, amount: int):
        self.__driver.buy(stock_code, amount, price)

    def sell(self, stock_code: str, price: int, amount: int):
        self.__driver.sell(stock_code, amount, price)

    def get_price(self, stock_code: str):
        self.__driver.current_price(stock_code)


class NemoDriver(IStockBrokerDriver):
    pass


class MockDriver(IStockBrokerDriver):
    pass
