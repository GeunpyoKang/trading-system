from unittest import TestCase


class TestKiwerDriver(TestCase):
    def setUp(self):
        self.sut = KiwerDriver()

    def testLogin(self):
        self.assertEqual(True, self.sut.login('test', '1234'))

    def testBuy(self):
        self.assertEqual(True, self.sut.buy('ABC123', 500, 10))

    def testSell(self):
        self.assertEqual(True, self.sut.sell('ABC123', 700,5))

    def testCurrentPrice(self):
        self.assertEqual(int, type(self.sut.get_price('ABC123')))


class TestNemoDriver(TestCase):
    def setUp(self):
        self.sut = NemoDriver()

    def testLogin(self):
        self.assertEqual(True, self.sut.login('test', '1234'))

    def testBuy(self):
        self.assertEqual(True, self.sut.buy('ABC123', 500, 10))

    def testSell(self):
        self.assertEqual(True, self.sut.sell('ABC123', 700,5))

    def testCurrentPrice(self):
        self.assertEqual(int, type(self.sut.get_price('ABC123')))

