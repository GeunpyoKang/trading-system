from IStockBrokerDriver import IStockBrokerDriver
from nemo_api import NemoAPI


class NemoDriver(IStockBrokerDriver):
    def __init__(self):
        self.driver = NemoAPI()

    def login(self, id: str, password: str):
        try:
            self.driver.cerification(id, password)
            return True
        except:
            return False

    def buy(self, stock_code: str, price: int, amount: int):
        self.driver.purchasing_stock(stock_code, price, amount)

    def sell(self, stock_code: str, price: int, amount: int):
        self.driver.selling_stock(stock_code, price, amount)

    def get_price(self, stock_code: str):
        self.driver.get_market_price(stock_code, 0)
