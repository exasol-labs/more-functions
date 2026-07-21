import pyexasol
import pytest

from exasol.tdbp.dialects.exasol.exasol_object_factory import ExasolObjectFactory


@pytest.fixture(scope="session")
def connection(backend_aware_database_params):
    with pyexasol.connect(**backend_aware_database_params) as conn:
        yield conn

@pytest.fixture
def factory(connection):
    factory = ExasolObjectFactory(connection)
    factory.purge_user_objects()  # Clean slate for each test
    return factory


@pytest.fixture(scope='session', autouse=True)
def schema(connection):
    factory = ExasolObjectFactory(connection)
    schema=factory.create_schema("test_schema")
    connection.execute('open schema ' + schema.fully_qualified_name())
    return schema
