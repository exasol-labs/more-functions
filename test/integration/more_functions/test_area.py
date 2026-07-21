import pytest

from test.integration.more_functions.scalar_function_test_base import (
    ScalarFunctionTestBase,
)


# [itest -> dsn~area-function~1]
class TestArea(ScalarFunctionTestBase):
    @pytest.mark.parametrize('value, expected', [
        ("linestring(0 0, 0 1, 1 1)", 0),  # Line string is not a polygon, so area is zero
        ("polygon((0 0, 0 1, 1 1, 1 0, 0 0))", 1)
    ])
    def test_area(self, value, expected):
        self.load_function("area")
        self.assert_query(f"select area('{value}')", expected)

