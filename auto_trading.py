import time

class AutoTrading:
    def __init__(self):
        self.__broker = None

    def select_stock_broker(self, broker):
        self.__broker = broker

    def login(self, id, password):
        return self.__broker.login(id, password)

    def buy(self, ticker, price, shares):
        return self.__broker.buy(ticker, price, shares)

    def sell(self, ticker, price, shares):
        return self.__broker.sell(ticker, price, shares)

    def get_price(self, ticker):
        return self.__broker.get_price(ticker)

    def buy_nice_timing(self, ticker, price):
        trends = []
        for i in range(2):
            trends.append(self.__broker.get_price(ticker))
            time.sleep(0.1)

        if trends[0] < trends[1]:
            current_price = self.__broker.get_price(ticker)
            self.buy(ticker, current_price, price//current_price)

    def sell_nice_timing(self, ticker, shares):
        trends = []
        for i in range(2):
            trends.append(self.__broker.get_price(ticker))
            time.sleep(0.1)

        if trends[0] > trends[1]:
            current_price = self.__broker.get_price(ticker)
            self.sell(ticker, current_price, shares)
