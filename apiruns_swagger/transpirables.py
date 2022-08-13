from abc import ABC, abstractmethod
from apiruns_swagger.swagger import adapters
from apiruns_swagger.swagger.adapters import TransForm


class Convertible(ABC):
    """Adapter interface, to regulate adapters

    Args:
        adaptee (Adaptee): Specific class that executes the transformation
    """

    @abstractmethod
    def transform(self, xml: str) -> dict:
        """Abstract method in charge of regulating the transformation
        :param xlm: Input format to transform
        :return dict: transformed data
        """


class ConvertSwagger(Convertible):
    """Adapter implementation, to transform to swagger"""

    def __init__(self, adaptee: adapters) -> None:
        self.adaptee = adaptee

    def transform(self, path: str) -> str:
        """Implementation to transform XML to swagger
        :param xml: Format to transform
        :return dict: transformed data
        """
        with open(path, "r", encoding="utf-8") as file:
            data = file.read()
        return self.adaptee.execute(data)


def xml_to_swagger(path: str) -> str:
    """Utilitarian method to implement the transformation"""
    adaptee = TransForm()
    converter = ConvertSwagger(adaptee)
    return converter.transform(path)
