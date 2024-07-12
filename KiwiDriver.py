from IStockBrokerDriver import IStockBrokerDriver
from kiwer_api import KiwerAPI

class KiwiDriver(IStockBrokerDriver):
    def __init__(self):
        self.api = KiwerAPI()

    def login(self, id: str, password: str):
        self.api.login(id, password)

    def buy(self, stock_code: str, price: int, amount: int):
        self.api.buy(stock_code, amount, price)

    def sell(self, stock_code: str, price: int, amount: int):
        self.api.sell(stock_code, amount, price)

    def get_price(self, stock_code: str):
        return self.api.current_price(stock_code)


