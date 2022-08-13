from abc import ABC, abstractmethod


class Adaptee(ABC):
    """Responsible for regulating the adapter

    Args:
        data (str): data to transform
    """

    @abstractmethod
    def execute(self, data: dict) -> str:
        """Abstract method to execute transformation"""


class TransForm(Adaptee):
    def execute(self, data: dict) -> str:
        print("transfor")
