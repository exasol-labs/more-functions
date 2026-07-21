import pytest


class ScalarFunctionTestBase:
    @pytest.fixture(autouse=True)
    def _connection(self, connection):
        self.connection = connection

    def load_function(self, name):
        with open("exasol/more_functions/sql/scalar/{name}.sql") as file:
            self.connection.execute(file.read())

    def assert_query(self, query, expected_result):
        result = self.connection.execute(query).fetchall()
        assert result[0][0] == expected_result
