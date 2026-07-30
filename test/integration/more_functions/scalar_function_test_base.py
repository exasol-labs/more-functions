from pathlib import Path

import pytest


class ScalarFunctionTestBase:
    @pytest.fixture(autouse=True)
    def _connection(self, connection):
        self.connection = connection

    def load_function(self, name):
        # [itest -> dsn~function-source-loader-selection~1]
        function_files = [
            Path("exasol/more_functions/sql/scalar") / f"{name}.sql",
            Path("exasol/more_functions/lua/scalar") / f"{name}.lua",
        ]
        function_file = next((path for path in function_files if path.exists()), None)
        if function_file is None:
            msg = f"Could not find function definition for {name!r}"
            raise FileNotFoundError(msg)
        with function_file.open() as file:
            source = file.read()
        self.connection.execute(self._prepare_function_source(function_file, source))

    @staticmethod
    def _prepare_function_source(function_file, source):
        if function_file.suffix != ".lua":
            return source
        # [itest -> dsn~lua-function-source-header~1]
        return (
            "\n".join(line.removeprefix("--| ") for line in source.splitlines())
            + "\n/\n"
        )

    def assert_query(self, query, expected_result):
        result = self.connection.execute(query).fetchall()
        assert len(result) == 1, f"Expected one row for query: {query}"
        actual_result = result[0][0]
        assert actual_result == expected_result, (
            f"Unexpected query result for: {query}\n"
            f"Expected: {expected_result!r} "
            f"({type(expected_result).__name__})\n"
            f"Actual:   {actual_result!r} ({type(actual_result).__name__})"
        )
