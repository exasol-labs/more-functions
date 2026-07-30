import re
from test.integration.more_functions.scalar_function_test_base import (
    ScalarFunctionTestBase,
)

import pytest


class TestMetadataFunctions(ScalarFunctionTestBase):
    @pytest.mark.parametrize(
        "source_name, invocation, expected_query",
        [
            ("database", "DATABASE()", "current_schema"),
            ("connection_id", "CONNECTION_ID()", "current_session"),
        ],
    )
    # [itest -> scn~metadata-database-function~1]
    # [itest -> scn~metadata-connection-id-function~1]
    def test_function_returns_current_session_value(
        self, source_name, invocation, expected_query
    ):
        self.load_function(source_name)
        expected = self.connection.execute(f"select {expected_query}").fetchall()[0][0]
        self.assert_query(f"select {invocation}", expected)

    # [itest -> scn~metadata-version-function~1]
    def test_version_function_returns_database_version(self):
        self.load_function("version")
        actual = self.connection.execute("select version()").fetchall()[0][0]
        assert isinstance(actual, str)
        assert re.fullmatch(r"\d+\.\d+\.\d+.*", actual) is not None
        self.assert_query("select version()", actual)
