import pytest

@pytest.fixture
def schema():
    response = [
        {
            "created_at": "2022-08-13T16:55:08.313767+00:00",
            "path": "/users",
            "name": "model-45b07e1e-469d-483e-a1f7-ea9a216b60e7",
            "schema": {
                "username": {
                    "type": "string",
                    "required": True
                },
                "age": {
                    "type": "integer",
                    "required": True
                },
                "is_admin": {
                    "type": "boolean",
                    "required": True
                },
                "level": {
                    "type": "string"
                }
            },
            "status_code": {},
            "static": None,
            "features": {
                "internal": {},
                "externals": {}
            }
        },
        {
            "path": "/rafa",
            "name": "model-88bfef6e-90b2-4da8-9cee-3d5224a54aa1",
            "schema": {
                "name": {
                    "type": "string"
                }
            },
            "status_code": {},
            "static": None,
            "features": {
                "internal": {},
                "externals": {}
            }
        },
        {
            "path": "/pepito",
            "name": "model-64c701b4-e18f-4e37-a96e-9a9d2557a2e6",
            "schema": {
                "name": {
                    "type": "string"
                }
            },
            "status_code": {},
            "static": None,
            "features": {
                "internal": {},
                "externals": {}
            }
        }
    ]
    return response