from abc import ABC, abstractmethod


class StokerBroker(ABC):
    pass


class KiwerDriver(StokerBroker):
    pass


class NemoDriver(StokerBroker):
    pass


class MockDriver(StokerBroker):
    pass
