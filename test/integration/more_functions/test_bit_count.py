from test.integration.exasol_type_boundaries import (
    MAX_DECIMAL_36,
    MIN_DECIMAL_36,
)
from test.integration.more_functions.scalar_function_test_base import (
    ScalarFunctionTestBase,
)

import pytest


class TestBitCount(ScalarFunctionTestBase):
    # [itest -> dsn~bit-count-integer-literal~1]
    # [itest -> dsn~bit-count-exact-numeric-integer~1]
    # [itest -> dsn~bit-count-floating-point-integer~1]
    # [itest -> dsn~bit-count-ignore-higher-bits~1]
    @pytest.mark.parametrize(
        "expression, expected",
        [
            ("29", 4),
            ("cast(29 as decimal(18,0))", 4),
            ("cast(3.1414 as decimal(18,4))", 3),
            ("cast(29,52 as double precision)", 4),
            (
                f"cast({0b1_0000000001_0000000001_0000000010_11111} as decimal(36,0))",
                9,
            ),
            ("cast(9223372036854775808 as decimal(36,0))", 1),
            ("cast(18446744073709551615 as decimal(36,0))", 64),
            ("cast(-1 as decimal(36,0))", 64),
            ("cast(18446744073709551616 as decimal(36,0))", 0),
            ("cast(18446744073709551645 as decimal(36,0))", 4),
            (f"cast({MIN_DECIMAL_36} as decimal(36,0))", 14),
            (f"cast({MAX_DECIMAL_36} as decimal(36,0))", 51),
            ("0", 0),
        ],
    )
    def test_bit_count(self, expression, expected):
        self.load_function("bit_count")
        self.assert_query(f"select bit_count({expression})", expected)

    # [itest -> dsn~bit-count-null~1]
    def test_bit_count_null(self):
        self.load_function("bit_count")
        self.assert_query("select bit_count(null)", None)
