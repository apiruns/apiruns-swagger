# apiruns-swagger

Swagger documentation for Apiruns projects

Install

```bash
pip install apiruns-swagger
```

Using
```python
from apiruns_swagger import json_to_yaml

apiruns_schema = {
    "path": "/users",
    "schema": {
        "name": "anybody",
        "last_name": "anybody",
    }
}

swagger_schema = json_to_yaml(apiruns_schema)
```
