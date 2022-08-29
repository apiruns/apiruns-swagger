from abc import ABC, abstractmethod
import json
from apiruns_swagger.swagger import adapters
from apiruns_swagger.swagger.adapters import TransFormOpenApi3


class Convertible(ABC):
    """Adapter interface, to regulate adapters

    Args:
        adaptee (Adaptee): Specific class that executes the transformation
    """

    @abstractmethod
    def transform(self, json_data: str) -> dict:
        """Abstract method in charge of regulating the transformation
        :param json_data: json to transform to dict
        :return str: transformed data
        """


class ConvertSwagger(Convertible):
    """Adapter implementation, to transform to swagger"""

    def __init__(self, adaptee: adapters) -> None:
        self.adaptee = adaptee

    def transform(self, json_data: list) -> str:
        """Implementation to transform XML to swagger
        :param json_data: json to transform to dict
        :return str: transformed data
        """
        data = json.loads(json)
        return self.adaptee.execute(data)


def json_to_swagger(json: list) -> str:
    """Utilitarian method to implement the transformation"""
    adaptee = TransFormOpenApi3()
    converter = ConvertSwagger(adaptee)
    return converter.transform(json)
