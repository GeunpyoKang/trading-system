from stock_broker_driver import IStockBrokerDriver
from kiwer_api import KiwerAPI

class KiwerDriver(IStockBrokerDriver):
    def __init__(self):
        self.api = KiwerAPI()

    def login(self, id: str, password: str):
        self.api.login(id, password)
        return True

    def buy(self, stock_code: str, price: int, amount: int):
        self.api.buy(stock_code, amount, price)
        return True

    def sell(self, stock_code: str, price: int, amount: int):
        self.api.sell(stock_code, amount, price)
        return True

    def get_price(self, stock_code: str):
        return self.api.current_price(stock_code)


