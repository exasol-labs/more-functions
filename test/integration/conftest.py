import pyexasol
import pytest
import exasol.tdbp


@pytest.fixture(scope="session")
def connection(backend_aware_database_params):
    with pyexasol.connect(**backend_aware_database_params) as conn:
        yield conn

@pytest.fixture
def factory(connection):
    factory = ExasolObjectFactory(connection)
    factory.purge_user_objects()  # Clean slate for each test
    return factory
