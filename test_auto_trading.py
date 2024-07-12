from unittest import TestCase

from kiwer_api import KiwerAPI
from nemo_api import NemoAPI


class AutoTrading(TestCase):
    def setUp(self):
        self.kiwer = KiwerAPI()
        self.nemo = NemoAPI()

    def testSelectWrongStockBroker(self):
        pass

    def testSelectKiwerStockBroker(self):
        pass

    def testSelectNemoStockBroker(self):
        pass




