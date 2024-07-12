import time

from stock_broker_driver import IStockBrokerDriver


class AutoTrading:
    def __init__(self, driver: IStockBrokerDriver):
        self.driver = driver
    def login(self, id, password):
        pass

    def buy(self, ticker, price, shares):
        pass

    def sell(self, ticker, price, shares):
        pass

    def get_price(self, ticker):
        pass

    def buy_nice_timing(self, ticker, price):
        trends = []
        for i in range(2):
            trends.append(self.driver.get_price(ticker))
            time.sleep(0.1)

        if trends[0] < trends[1]:
            current_price = self.driver.get_price(ticker)
            self.buy(ticker, current_price, price//current_price)

    def sell_nice_timing(self, ticker, shares):
        trends = []
        for i in range(2):
            trends.append(self.driver.get_price(ticker))
            time.sleep(0.1)

        if trends[0] > trends[1]:
            current_price = self.driver.get_price(ticker)
            self.sell(ticker, current_price, shares)
