from collections import defaultdict


class AutoTrading:
    def __init__(self):
        self.__broker = None
        self.__cache = 1000000
        self.__stocks = defaultdict(int)

    def select_stock_broker(self, broker):
        self.__broker = broker

    def login(self, id, password):
        return self.__broker.login(id, password)

    def buy(self, ticker, price, shares):
        if self.get_price(ticker) * shares > self.__cache:
            return False
        if not self.__broker.buy(ticker, price, shares):
            return False
        if ticker not in self.__stocks:
            self.__stocks[ticker] = 0
        self.__stocks[ticker] += shares
        self.__cache -= self.get_price(ticker) * shares
        return True

    def sell(self, ticker, price, shares):
        if ticker not in self.__stocks:
            return False
        if self.__stocks[ticker] < shares:
            return False
        if not self.__broker.sell(ticker, price, shares):
            return False
        self.__stocks[ticker] -= shares
        self.__cache += self.get_price(ticker) * shares
        return True

    def get_price(self, ticker):
        return self.__broker.get_price(ticker)

    def buy_nice_timing(self, ticker, price):
        current_price = self.get_price(ticker)
        for _ in range(2):
            prev_price = current_price
            current_price = self.get_price(ticker)
            if current_price < prev_price:
                return
        return self.buy(ticker, price, 1)  # TODO: need to check balance

    def sell_nice_timing(self, ticker, shares):
        current_price = self.get_price(ticker)
        for _ in range(2):
            prev_price = current_price
            current_price = self.get_price(ticker)
            if current_price > prev_price:
                return
        return self.sell(ticker, current_price, shares)

    def get_asset(self):
        return self.__cache, self.__get_value_of_stocks()

    def __get_value_of_stocks(self):
        value = 0
        for stock_name, shares in self.__stocks.items():
            value += self.get_price(stock_name) * shares
        return value

    ###
    def is_valid_stock_code(self, stock_code):
        if not (6 <= len(stock_code) <= 7):
            raise Exception()

        if len(stock_code) == 7:
            if stock_code[0] not in ('A', 'B', 'C', 'K'):
                raise Exception()
            stock_code = stock_code[1:]

        if len(stock_code) == 6:
            if not ('000000' <= str(stock_code) <= '999999'):
                raise Exception()

        return True
