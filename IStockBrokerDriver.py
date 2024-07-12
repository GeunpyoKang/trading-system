from abc import ABC, abstractmethod


class IStockBrokerDriver(ABC):
    @abstractmethod
    def login(self, id: str, password: str):
        pass

    @abstractmethod
    def buy(self, stock_code: str, price: int, amount: int):
        pass

    @abstractmethod
    def sell(self, stock_code: str, price: int, amount: int):
        pass

    @abstractmethod
    def get_price(self, stock_code: str):
        pass
