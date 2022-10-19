from abc import ABC, abstractmethod
import typing

METHODS = ["get", "post", "put", "patch", "delete"]
ACTIONS = [
    ("list", "get"),
    ("retrieve", "get"),
    ("create", "post"),
    ("parcial_update", "patch"),
    ("update", "put"),
    ("destroy", "delete"),
]
ACTIONS_WITH_ID = (
    "retrieve",
    "parcial_update",
    "update",
    "destroy"
)


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
            methods_modificable = {}
            for action, method in ACTIONS:
                if action in ACTIONS_WITH_ID:
                    methods_modificable.update(self._build_method(method, action, endpoint["schema"]))
                else:
                    methods.update(self._build_method(method, action, endpoint["schema"]))

            path = f"{endpoint['path']}/{{id}}"
            paths.update({path: methods_modificable})
            paths.update({endpoint["path"]: methods})

        if paths:
            header = {
                "openapi": "3.0.3",
                "info": {"title": "Swagger doc - OpenAPI 3.0", "version": "1.0.11"},
                "servers": self.default_server if not servers else servers,
                "paths": paths,
            }
            return header

    def _build_method(self, method: str, action: str, schema: dict) -> dict:
        properties = {}
        for proper, definition in schema.items():
            properties[proper] = {"type": definition["type"]}
        schema = {"schema": {"type": "object", "properties": properties}}
        request_body = {"content": {"application/json": schema}}
        status_code = "201" if method == "post" else "200"
        params = {}
        if action in ACTIONS_WITH_ID:
            params = {
                "parameters": [
                    {
                        "name": "id",
                        "in": "path",
                        "description": "Id of the resource.",
                        "required": True,
                        "schema": {
                            "type": "string"
                        }
                    }
                ]
            }
        open_api_schema = {
            method: {
                **params,
                "requestBody": request_body,
                "responses": {
                    status_code: {
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
