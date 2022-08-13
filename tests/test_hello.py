from apiruns_swagger.transpirables import hello_world


def test_call_hello():
    assert "Hello world" == hello_world()
