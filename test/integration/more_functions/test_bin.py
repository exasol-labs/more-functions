from test.integration.more_functions.scalar_function_test_base import (
    ScalarFunctionTestBase,
)

import pytest

MAX_UNSIGNED_64 = "1" * 64
MIN_SIGNED_64 = "1" + "0" * 63
NEGATIVE_TWO = "1" * 63 + "0"


class TestBin(ScalarFunctionTestBase):
    # [itest -> scn~bin-integer-literal~1]
    # [itest -> scn~bin-exact-numeric-integer~1]
    # [itest -> scn~bin-floating-point-integer~1]
    # [itest -> scn~bin-ignore-higher-bits~1]
    @pytest.mark.parametrize(
        "expression, expected",
        [
            ("0", "0"),
            ("1", "1"),
            ("2", "10"),
            ("5", "101"),
            ("29", "11101"),
            ("255", "11111111"),
            ("cast(29 as decimal(18,0))", "11101"),
            ("cast(29.5 as decimal(18,4))", "11101"),
            ("cast(29.5 as double precision)", "11101"),
            ("cast(-1 as decimal(36,0))", MAX_UNSIGNED_64),
            ("cast(-2 as decimal(36,0))", NEGATIVE_TWO),
            ("cast(-9223372036854775808 as decimal(36,0))", MIN_SIGNED_64),
            ("cast(-9223372036854775809 as decimal(36,0))", "1" * 63),
            ("cast(-18446744073709551615 as decimal(36,0))", "1"),
            ("cast(-18446744073709551616 as decimal(36,0))", MAX_UNSIGNED_64),
            ("cast(-18446744073709551617 as decimal(36,0))", MAX_UNSIGNED_64),
            (
                "cast(18446744073709551615 as decimal(36,0))",
                MAX_UNSIGNED_64,
            ),
            (
                "cast(18446744073709551616 as decimal(36,0))",
                MAX_UNSIGNED_64,
            ),
            (
                "cast(18446744073709551645 as decimal(36,0))",
                MAX_UNSIGNED_64,
            ),
        ],
    )
    def test_bin(self, expression, expected):
        self.load_function("bin")
        self.assert_query(f"select bin({expression})", expected)

    # [itest -> scn~bin-null~1]
    def test_bin_null(self):
        self.load_function("bin")
        self.assert_query("select bin(null)", None)
