import pyexasol
import pytest

from exasol.tdbp.dialects.exasol.exasol_object_factory import ExasolObjectFactory

@pytest.fixture(scope='session', autouse=True)
def schema(connection):
    factory = ExasolObjectFactory(connection)
    schema=factory.create_schema("string_functions")
    connection.execute('open schema ' + schema.fully_qualified_name())
    return schema


def load_function(connection, name):
    with open("exasol/more_functions/sql/scalar/" + name +  ".sql") as file:
        sql = file.read()
    connection.execute(sql)

def assert_query(connection, query, expected_result):
    result = connection.execute(query).fetchall()
    assert result[0][0] == expected_result

@pytest.mark.parametrize(
    "value, expected", [
        ("", "NULL"), # Exasol's empty string is the same as NULL
        ("''", "''''"),
        ("Hello ''world''!", "'Hello ''world''!'"),
    ])
def test_quote(connection, value, expected):
    load_function(connection, "quote")
    assert_query(connection, "select quote('" + value + "')", expected)

def test_quote_null(connection):
    load_function(connection, "quote")
    assert_query(connection, "select quote(null)", "NULL")
