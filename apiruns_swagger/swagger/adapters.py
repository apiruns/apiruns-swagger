from abc import ABC, abstractmethod
import typing

METHODS = ["get", "post", "put", "patch", "delete"]


class Adaptee(ABC):
    """Responsible for regulating the adapter

    Args:
        data (str): data to transform
    """

    @abstractmethod
    def execute(self, data: list, servers: list = []) -> dict:
        """Abstract method to execute transformation"""


class TransFormOpenApi3(Adaptee):
    default_server = [{"url": "http://localhost:8080"}]

    def execute(self, data: list, servers: list = []) -> typing.Union[dict, None]:
        paths = {}
        for endpoint in data:
            methods = {}
            for method in METHODS:
                methods.update(self._build_method(method, endpoint["schema"]))
            paths.update({endpoint["path"]: methods})
        if paths:
            header = {
                "openapi": "3.0.3",
                "info": {"title": "Swagger doc - OpenAPI 3.0", "version": "1.0.11"},
                "servers": self.default_server if not servers else servers,
                "paths": paths,
            }
            return header

    def _build_method(self, method: str, schema: dict) -> dict:
        properties = {}
        for proper, definition in schema.items():
            properties[proper] = {"type": definition["type"]}
        schema = {"schema": {"type": "object", "properties": properties}}
        request_body = {"content": {"application/json": schema}}
        open_api_schema = {
            method: {
                "requestBody": request_body,
                "responses": {
                    "200": {
                        "description": "Successful operation",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "properties": {
                                        "public_id": {
                                            "type": "string",
                                            "example": "550e8400-e29b-41d4-a716-446655440000"
                                        },
                                        **properties
                                    }
                                }
                            },
                        },
                    }
                },
            }
        }
        if method == "get" or method == "delete":
            del open_api_schema[method]["requestBody"]
        return open_api_schema
