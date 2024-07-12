from IStockBrokerDriver import IStockBrokerDriver
from nemo_api import NemoAPI


class NemoDriver(IStockBrokerDriver):
    def __init__(self):
        self.__driver = NemoAPI()

    def login(self, id: str, password: str):
        self.__driver.cerification(id, password)

    def buy(self, stock_code: str, price: int, amount: int):
        self.__driver.purchasing_stock(stock_code, price, amount)

    def sell(self, stock_code: str, price: int, amount: int):
        self.__driver.selling_stock(self, stock_code, price, amount)

    def get_price(self, stock_code: str):
        self.__driver.get_market_price(self, stock_code, 0)
