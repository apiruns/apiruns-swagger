from apiruns_swagger.hello import hello_world


def test_call_hello():
    assert "Hello world" == hello_world()
