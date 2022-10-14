from abc import ABC, abstractmethod
import yaml
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

    def transform(self, json_data: list) -> dict:
        """Implementation to transform XML to swagger
        :param json_data: json to transform to dict
        :return str: transformed data
        """
        return self.adaptee.execute(json_data)


def json_to_swagger(json: list, servers: list = []) -> dict:
    """Utilitarian method to implement the transformation

    Args:
        json (list): List of schema.
        example:
            [{
                "path": "/users",
                "schema": {
                    "name": "anybody",
                    "last_name": "anybody",
                }
            }]
        servers (list): List of servers.
        example:
            [{
                "url": "https://api.cloud.apiruns.com",
            }]
    Returns:
        json: swagger schema.
    """
    adaptee = TransFormOpenApi3()
    converter = ConvertSwagger(adaptee)
    return converter.transform(json)


def json_to_yaml(json: list, servers: list = []) -> str:
    """List of Apiruns schema to swagger.

    Returns:
        str: swagger schema.
    """
    json_swagger = json_to_swagger(json)
    return yaml.dump(json_swagger, allow_unicode=True)
