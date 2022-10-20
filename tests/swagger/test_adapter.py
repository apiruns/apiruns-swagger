from apiruns_swagger.swagger.adapters import TransFormOpenApi3

class TestTransForms:
    
    tranform = TransFormOpenApi3()
    
    def test_execute(self, schema):
        """Test """
        expected = {'openapi': '3.0.3', 'info': {'title': 'Swagger doc - OpenAPI 3.0', 'version': '1.0.11'}, 'servers': [{'url': 'http://localhost:8080'}], 'paths': {'/users/{id}': {'get': {'parameters': [{'name': 'id', 'in': 'path', 'description': 'Id of the resource.', 'required': True, 'schema': {'type': 'string'}}], 'tags': ['users'], 'responses': {'200': {'description': 'Successful operation', 'content': {'application/json': {'schema': {'properties': {'public_id': {'type': 'string', 'example': '550e8400-e29b-41d4-a716-446655440000'}, 'username': {'type': 'string'}, 'age': {'type': 'integer'}, 'is_admin': {'type': 'boolean'}, 'level': {'type': 'string'}}}}}}}}, 'patch': {'parameters': [{'name': 'id', 'in': 'path', 'description': 'Id of the resource.', 'required': True, 'schema': {'type': 'string'}}], 'tags': ['users'], 'requestBody': {'content': {'application/json': {'schema': {'type': 'object', 'properties': {'username': {'type': 'string'}, 'age': {'type': 'integer'}, 'is_admin': {'type': 'boolean'}, 'level': {'type': 'string'}}}}}}, 'responses': {'200': {'description': 'Successful operation', 'content': {'application/json': {'schema': {'properties': {'public_id': {'type': 'string', 'example': '550e8400-e29b-41d4-a716-446655440000'}, 'username': {'type': 'string'}, 'age': {'type': 'integer'}, 'is_admin': {'type': 'boolean'}, 'level': {'type': 'string'}}}}}}}}, 'put': {'parameters': [{'name': 'id', 'in': 'path', 'description': 'Id of the resource.', 'required': True, 'schema': {'type': 'string'}}], 'tags': ['users'], 'requestBody': {'content': {'application/json': {'schema': {'type': 'object', 'properties': {'username': {'type': 'string'}, 'age': {'type': 'integer'}, 'is_admin': {'type': 'boolean'}, 'level': {'type': 'string'}}}}}}, 'responses': {'200': {'description': 'Successful operation', 'content': {'application/json': {'schema': {'properties': {'public_id': {'type': 'string', 'example': '550e8400-e29b-41d4-a716-446655440000'}, 'username': {'type': 'string'}, 'age': {'type': 'integer'}, 'is_admin': {'type': 'boolean'}, 'level': {'type': 'string'}}}}}}}}, 'delete': {'parameters': [{'name': 'id', 'in': 'path', 'description': 'Id of the resource.', 'required': True, 'schema': {'type': 'string'}}], 'tags': ['users'], 'responses': {'200': {'description': 'Successful operation', 'content': {'application/json': {'schema': {'properties': {'public_id': {'type': 'string', 'example': '550e8400-e29b-41d4-a716-446655440000'}, 'username': {'type': 'string'}, 'age': {'type': 'integer'}, 'is_admin': {'type': 'boolean'}, 'level': {'type': 'string'}}}}}}}}}, '/users': {'get': {'tags': ['users'], 'responses': {'200': {'description': 'Successful operation', 'content': {'application/json': {'schema': {'properties': {'public_id': {'type': 'string', 'example': '550e8400-e29b-41d4-a716-446655440000'}, 'username': {'type': 'string'}, 'age': {'type': 'integer'}, 'is_admin': {'type': 'boolean'}, 'level': {'type': 'string'}}}}}}}}, 'post': {'tags': ['users'], 'requestBody': {'content': {'application/json': {'schema': {'type': 'object', 'properties': {'username': {'type': 'string'}, 'age': {'type': 'integer'}, 'is_admin': {'type': 'boolean'}, 'level': {'type': 'string'}}}}}}, 'responses': {'201': {'description': 'Successful operation', 'content': {'application/json': {'schema': {'properties': {'public_id': {'type': 'string', 'example': '550e8400-e29b-41d4-a716-446655440000'}, 'username': {'type': 'string'}, 'age': {'type': 'integer'}, 'is_admin': {'type': 'boolean'}, 'level': {'type': 'string'}}}}}}}}}, '/rafa/{id}': {'get': {'parameters': [{'name': 'id', 'in': 'path', 'description': 'Id of the resource.', 'required': True, 'schema': {'type': 'string'}}], 'tags': ['rafa'], 'responses': {'200': {'description': 'Successful operation', 'content': {'application/json': {'schema': {'properties': {'public_id': {'type': 'string', 'example': '550e8400-e29b-41d4-a716-446655440000'}, 'name': {'type': 'string'}}}}}}}}, 'patch': {'parameters': [{'name': 'id', 'in': 'path', 'description': 'Id of the resource.', 'required': True, 'schema': {'type': 'string'}}], 'tags': ['rafa'], 'requestBody': {'content': {'application/json': {'schema': {'type': 'object', 'properties': {'name': {'type': 'string'}}}}}}, 'responses': {'200': {'description': 'Successful operation', 'content': {'application/json': {'schema': {'properties': {'public_id': {'type': 'string', 'example': '550e8400-e29b-41d4-a716-446655440000'}, 'name': {'type': 'string'}}}}}}}}, 'put': {'parameters': [{'name': 'id', 'in': 'path', 'description': 'Id of the resource.', 'required': True, 'schema': {'type': 'string'}}], 'tags': ['rafa'], 'requestBody': {'content': {'application/json': {'schema': {'type': 'object', 'properties': {'name': {'type': 'string'}}}}}}, 'responses': {'200': {'description': 'Successful operation', 'content': {'application/json': {'schema': {'properties': {'public_id': {'type': 'string', 'example': '550e8400-e29b-41d4-a716-446655440000'}, 'name': {'type': 'string'}}}}}}}}, 'delete': {'parameters': [{'name': 'id', 'in': 'path', 'description': 'Id of the resource.', 'required': True, 'schema': {'type': 'string'}}], 'tags': ['rafa'], 'responses': {'200': {'description': 'Successful operation', 'content': {'application/json': {'schema': {'properties': {'public_id': {'type': 'string', 'example': '550e8400-e29b-41d4-a716-446655440000'}, 'name': {'type': 'string'}}}}}}}}}, '/rafa': {'get': {'tags': ['rafa'], 'responses': {'200': {'description': 'Successful operation', 'content': {'application/json': {'schema': {'properties': {'public_id': {'type': 'string', 'example': '550e8400-e29b-41d4-a716-446655440000'}, 'name': {'type': 'string'}}}}}}}}, 'post': {'tags': ['rafa'], 'requestBody': {'content': {'application/json': {'schema': {'type': 'object', 'properties': {'name': {'type': 'string'}}}}}}, 'responses': {'201': {'description': 'Successful operation', 'content': {'application/json': {'schema': {'properties': {'public_id': {'type': 'string', 'example': '550e8400-e29b-41d4-a716-446655440000'}, 'name': {'type': 'string'}}}}}}}}}, '/pepito/{id}': {'get': {'parameters': [{'name': 'id', 'in': 'path', 'description': 'Id of the resource.', 'required': True, 'schema': {'type': 'string'}}], 'tags': ['pepito'], 'responses': {'200': {'description': 'Successful operation', 'content': {'application/json': {'schema': {'properties': {'public_id': {'type': 'string', 'example': '550e8400-e29b-41d4-a716-446655440000'}, 'name': {'type': 'string'}}}}}}}}, 'patch': {'parameters': [{'name': 'id', 'in': 'path', 'description': 'Id of the resource.', 'required': True, 'schema': {'type': 'string'}}], 'tags': ['pepito'], 'requestBody': {'content': {'application/json': {'schema': {'type': 'object', 'properties': {'name': {'type': 'string'}}}}}}, 'responses': {'200': {'description': 'Successful operation', 'content': {'application/json': {'schema': {'properties': {'public_id': {'type': 'string', 'example': '550e8400-e29b-41d4-a716-446655440000'}, 'name': {'type': 'string'}}}}}}}}, 'put': {'parameters': [{'name': 'id', 'in': 'path', 'description': 'Id of the resource.', 'required': True, 'schema': {'type': 'string'}}], 'tags': ['pepito'], 'requestBody': {'content': {'application/json': {'schema': {'type': 'object', 'properties': {'name': {'type': 'string'}}}}}}, 'responses': {'200': {'description': 'Successful operation', 'content': {'application/json': {'schema': {'properties': {'public_id': {'type': 'string', 'example': '550e8400-e29b-41d4-a716-446655440000'}, 'name': {'type': 'string'}}}}}}}}, 'delete': {'parameters': [{'name': 'id', 'in': 'path', 'description': 'Id of the resource.', 'required': True, 'schema': {'type': 'string'}}], 'tags': ['pepito'], 'responses': {'200': {'description': 'Successful operation', 'content': {'application/json': {'schema': {'properties': {'public_id': {'type': 'string', 'example': '550e8400-e29b-41d4-a716-446655440000'}, 'name': {'type': 'string'}}}}}}}}}, '/pepito': {'get': {'tags': ['pepito'], 'responses': {'200': {'description': 'Successful operation', 'content': {'application/json': {'schema': {'properties': {'public_id': {'type': 'string', 'example': '550e8400-e29b-41d4-a716-446655440000'}, 'name': {'type': 'string'}}}}}}}}, 'post': {'tags': ['pepito'], 'requestBody': {'content': {'application/json': {'schema': {'type': 'object', 'properties': {'name': {'type': 'string'}}}}}}, 'responses': {'201': {'description': 'Successful operation', 'content': {'application/json': {'schema': {'properties': {'public_id': {'type': 'string', 'example': '550e8400-e29b-41d4-a716-446655440000'}, 'name': {'type': 'string'}}}}}}}}}}, 'tags': [{'name': 'users', 'description': 'without description.'}, {'name': 'rafa', 'description': 'without description.'}, {'name': 'pepito', 'description': 'without description.'}]}
        specification = self.tranform.execute(schema)
        assert expected == specification
