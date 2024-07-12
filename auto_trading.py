from collections import defaultdict


class UserAsset:
    def __init__(self):
        self.cash = 1000000
        self.stock = defaultdict(int)


class AutoTrading:
    def __init__(self):
        self.__broker = None
        self.__cach = 1000000
        self.__stocks = defaultdict(int)

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
        stock_price = 0
        for stock_code, quantity in self.__stocks:
            stock_price += self.get_price(stock_code) * self.get_stock_quantity(stock_code)
        return self.__cash, stock_price

    def get_stock_quantity(self, stock_code):
        return self.__stocks[stock_code]

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
