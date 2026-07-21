from test.integration.more_functions.scalar_function_test_base import (
    ScalarFunctionTestBase,
)

import pytest


class TestQuote(ScalarFunctionTestBase):
    # [itest -> dsn~quote-empty-string~1]
    # [itest -> dsn~quote-non-empty-string~1]
    @pytest.mark.parametrize(
        "value, expected",
        [
            ("", "NULL"),
            ("''", "''''"),
            ("Hello ''world''!", "'Hello ''world''!'"),
        ],
    )
    def test_quote(self, value, expected):
        self.load_function("quote")
        self.assert_query(f"select quote('{value}')", expected)

    # [itest -> dsn~quote-null~1]
    def test_quote_null(self):
        self.load_function("quote")
        self.assert_query("select quote(null)", "NULL")
