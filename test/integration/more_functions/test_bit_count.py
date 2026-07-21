from test.integration.more_functions.scalar_function_test_base import (
    ScalarFunctionTestBase,
)

import pytest


class TestBitCount(ScalarFunctionTestBase):
    # [itest -> dsn~bit-count-integer-literal~1]
    # [itest -> dsn~bit-count-exact-numeric-integer~1]
    # [itest -> dsn~bit-count-floating-point-integer~1]
    @pytest.mark.parametrize(
        "expression, expected",
        [
            ("29", "4"),
            ("cast(29 as decimal(18,0))", "4"),
            ("cast(29 as decimal(18,2))", "4"),
            ("cast(29 as double precision)", "4"),
            (
                f"cast({0b1_0000000001_0000000001_0000000010_11111} as decimal(36,0))",
                "9",
            ),
            ("0", "0"),
        ],
    )
    def test_bit_count(self, expression, expected):
        self.load_function("bit_count")
        self.assert_query(f"select bit_count({expression})", expected)

    # [itest -> dsn~bit-count-null~1]
    def test_bit_count_null(self):
        self.load_function("bit_count")
        self.assert_query("select bit_count(null)", None)
