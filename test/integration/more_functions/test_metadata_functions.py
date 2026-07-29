import re
from test.integration.more_functions.scalar_function_test_base import (
    ScalarFunctionTestBase,
)

import pytest


class TestMetadataFunctions(ScalarFunctionTestBase):
    # [itest -> dsn~metadata-backed-lua-functions-current-schema~1]
    # [itest -> dsn~metadata-backed-lua-functions-database~1]
    # [itest -> dsn~metadata-backed-lua-functions-schema~1]
    # [itest -> dsn~metadata-backed-lua-functions-connection-id~1]
    # [itest -> dsn~metadata-backed-lua-functions-session-user~1]
    # [itest -> dsn~metadata-backed-lua-functions-system-user~1]
    @pytest.mark.parametrize(
        "source_name, invocation, expected_query",
        [
            ("current_schema", "current_schema()", "current_schema"),
            ("database", "database()", "current_schema"),
            ("schema", "schema()", "current_schema"),
            ("connection_id", "connection_id()", "current_session"),
            ("session_user", "session_user()", "current_user"),
            ("system_user", "system_user()", "current_user"),
        ],
    )
    def test_function_returns_current_session_value(
        self, source_name, invocation, expected_query
    ):
        self.load_function(source_name)
        expected = self.connection.execute(
            f"select {expected_query}"
        ).fetchall()[0][0]
        self.assert_query(f"select {invocation}", expected)

    # [itest -> dsn~metadata-backed-lua-functions-version~1]
    # [itest -> dsn~metadata-backed-lua-functions-version-major~1]
    # [itest -> dsn~metadata-backed-lua-functions-version-minor~1]
    # [itest -> dsn~metadata-backed-lua-functions-version-patch~1]
    def test_version_functions_return_database_version_components(self):
        self.load_function("version")
        version = self.connection.execute("select version()").fetchall()[0][0]
        match = re.fullmatch(r"(\d+)\.(\d+)\.(\d+).*", version)
        assert match is not None, f"Unexpected database version: {version!r}"

        for source_name, invocation, component in [
            ("sys_version_major", "sys.version_major()", 1),
            ("sys_version_minor", "sys.version_minor()", 2),
            ("sys_version_patch", "sys.version_patch()", 3),
        ]:
            self.load_function(source_name)
            self.assert_query(f"select {invocation}", int(match.group(component)))
