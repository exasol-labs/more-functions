from pathlib import Path

import pytest


class ScalarFunctionTestBase:
    @pytest.fixture(autouse=True)
    def _connection(self, connection):
        self.connection = connection

    def load_function(self, name):
        sql_files = [
            Path("exasol/more_functions/sql/scalar") / f"{name}.sql",
            Path("exasol/more_functions/lua/scalar") / f"{name}.sql",
        ]
        function_file = next((path for path in sql_files if path.exists()), None)
        if function_file is None:
            msg = f"Could not find function definition for {name!r}"
            raise FileNotFoundError(msg)
        with function_file.open() as file:
            self.connection.execute(file.read())

    def assert_query(self, query, expected_result):
        result = self.connection.execute(query).fetchall()
        assert result[0][0] == expected_result
