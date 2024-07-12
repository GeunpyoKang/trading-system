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
        pass

    def sell_nice_timing(self, ticker, shares):
        pass
