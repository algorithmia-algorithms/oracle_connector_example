from . import oracle_connector_example

def test_oracle_connector_example():
    assert oracle_connector_example.apply("Jane") == "hello Jane"
