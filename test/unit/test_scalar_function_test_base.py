from pathlib import Path
from test.integration.more_functions.scalar_function_test_base import (
    ScalarFunctionTestBase,
)

import pytest


# [itest -> dsn~function-source-loader-selection~1]
def test_prepare_sql_function_source_keeps_source_unchanged() -> None:
    source = "CREATE SCRIPT function_name AS\n/\n"
    prepared_source = ScalarFunctionTestBase._prepare_function_source(
        Path("function_name.sql"), source
    )
    assert prepared_source == source


# [itest -> dsn~lua-function-source-header~1]
def test_prepare_lua_function_source_strips_only_header_prefixes() -> None:
    source = """\
--| CREATE LUA SCALAR SCRIPT function_name()
--| RETURNS DECIMAL(2,0) AS
-- ordinary Lua comment
local header_marker = "--| not a header"
function run(ctx)
    return 1
end"""

    prepared_source = ScalarFunctionTestBase._prepare_function_source(
        Path("function_name.lua"), source
    )

    assert prepared_source == """\
CREATE LUA SCALAR SCRIPT function_name()
RETURNS DECIMAL(2,0) AS
-- ordinary Lua comment
local header_marker = "--| not a header"
function run(ctx)
    return 1
end
/
"""


def test_load_function_raises_file_not_found_for_missing_definition() -> None:
    test_base = ScalarFunctionTestBase()
    with pytest.raises(FileNotFoundError, match="missing_function"):
        test_base.load_function("missing_function")
