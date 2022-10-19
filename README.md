# apiruns-swagger

Swagger documentation for Apiruns projects

Install

```bash
pip install apiruns-swagger
```

Using
```python
from apiruns_swagger import json_to_swagger

apiruns_schema = [
        {
            "path": "/users",
            "schema": {
                "name": {"type": "string"},
            }
        },
        {
            "path": "/inventory",
            "schema": {
                "price": {"type": "integer"},
            }
        }
    ]

servers = [{"url": "https://google.cloud.apiruns.com"}]

swagger_schema = json_to_swagger(apiruns_schema, servers=servers)
```
