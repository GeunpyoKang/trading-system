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
        current_price = self.get_price(ticker)
        for _ in range(2):
            prev_price = current_price
            current_price = self.get_price(ticker)
            if current_price < prev_price:
                return
        return self.buy(ticker, price, 1) # TODO: need to check balance


    def sell_nice_timing(self, ticker, shares):
        current_price = self.get_price(ticker)
        for _ in range(2):
            prev_price = current_price
            current_price = self.get_price(ticker)
            if current_price > prev_price:
                return
        return self.sell(ticker, current_price, shares)
