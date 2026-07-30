from test.integration.more_functions.scalar_function_test_base import (
    ScalarFunctionTestBase,
)

import pytest


# [itest -> dsn~st-alias-functions~1]
class TestStAliases(ScalarFunctionTestBase):
    def _fetch_single_value(self, query):
        rows = self.connection.execute(query).fetchall()
        assert len(rows) == 1, f"Expected exactly one row for query {query!r}, got {rows!r}"
        assert (
            len(rows[0]) == 1
        ), f"Expected exactly one column for query {query!r}, got {rows[0]!r}"
        return rows[0][0]

    def _assert_same_result(self, alias_query, target_query):
        alias_result = self._fetch_single_value(alias_query)
        target_result = self._fetch_single_value(target_query)
        assert alias_result == target_result, (
            "Alias and target returned different results.\n"
            f"Alias query:  {alias_query}\n"
            f"Target query: {target_query}\n"
            f"Alias result:  {alias_result!r} ({type(alias_result).__name__})\n"
            f"Target result: {target_result!r} ({type(target_result).__name__})"
        )

    def _assert_same_sql_type(self, alias_expression, target_expression):
        alias_sql_type = self._fetch_single_value(
            f"select typeof({alias_expression})"
        )
        target_sql_type = self._fetch_single_value(
            f"select typeof({target_expression})"
        )
        assert alias_sql_type == target_sql_type, (
            "Alias and target returned different SQL types.\n"
            f"Alias expression:  {alias_expression}\n"
            f"Target expression: {target_expression}\n"
            f"Alias SQL type:  {alias_sql_type!r}\n"
            f"Target SQL type: {target_sql_type!r}"
        )

    def _assert_same_pyexasol_type(self, alias_query, target_query):
        alias_metadata = next(iter(self.connection.execute(alias_query).columns().values()))
        target_metadata = next(
            iter(self.connection.execute(target_query).columns().values())
        )
        alias_pyexasol_type = alias_metadata["type"]
        target_pyexasol_type = target_metadata["type"]
        assert alias_pyexasol_type == target_pyexasol_type, (
            "Alias and target returned different PyExasol types.\n"
            f"Alias query:  {alias_query}\n"
            f"Target query: {target_query}\n"
            f"Alias PyExasol metadata:  {alias_metadata!r}\n"
            f"Target PyExasol metadata: {target_metadata!r}"
        )

    @pytest.mark.parametrize(
        "name, target, arguments",
        [
            ("area", "st_area", "'POLYGON((0 0,0 1,1 1,1 0,0 0))'"),
            ("boundary", "st_boundary", "'POLYGON((0 0,0 1,1 1,1 0,0 0))'"),
            ("buffer", "st_buffer", "'POINT(1 2)', 1.0"),
            ("centroid", "st_centroid", "'POLYGON((0 0,0 1,1 1,1 0,0 0))'"),
            ("convexhull", "st_convexhull", "'MULTIPOINT((0 0),(1 1))'"),
            ("crosses", "st_crosses", "'LINESTRING(0 0,2 2)', 'LINESTRING(0 2,2 0)'"),
            ("dimension", "st_dimension", "'POINT(1 2)'"),
            ("disjoint", "st_disjoint", "'POINT(0 0)', 'POINT(1 1)'"),
            ("endpoint", "st_endpoint", "'LINESTRING(0 0,1 1)'"),
            ("envelope", "st_envelope", "'POINT(1 2)'"),
            ("exteriorring", "st_exteriorring", "'POLYGON((0 0,0 1,1 1,1 0,0 0))'"),
            ("geometrytype", "st_geometrytype", "'POINT(1 2)'"),
            ("geometryn", "st_geometryn", "'MULTIPOINT((0 0),(1 1))', 1"),
            ("glength", "st_length", "'LINESTRING(0 0,1 1)'"),
            ("intersects", "st_intersects", "'POINT(1 1)', 'LINESTRING(0 0,2 2)'"),
            (
                "interiorringn",
                "st_interiorringn",
                "'POLYGON((0 0,0 2,2 2,2 0,0 0))', 1",
            ),
            ("isclosed", "st_isclosed", "'LINESTRING(0 0,1 1,0 0)'"),
            ("isempty", "st_isempty", "'POINT EMPTY'"),
            ("isring", "st_isring", "'LINESTRING(0 0,1 0,1 1,0 0)'"),
            ("issimple", "st_issimple", "'LINESTRING(0 0,1 1)'"),
            ("numgeometries", "st_numgeometries", "'MULTIPOINT((0 0),(1 1))'"),
            (
                "numinteriorrings",
                "st_numinteriorrings",
                "'POLYGON((0 0,0 2,2 2,2 0,0 0))'",
            ),
            ("numpoints", "st_numpoints", "'LINESTRING(0 0,1 1)'"),
            ("pointn", "st_pointn", "'LINESTRING(0 0,1 1)', 1"),
            ("startpoint", "st_startpoint", "'LINESTRING(0 0,1 1)'"),
            ("touches", "st_touches", "'POINT(0 0)', 'LINESTRING(0 0,1 1)'"),
            ("x", "st_x", "'POINT(1 2)'"),
            ("y", "st_y", "'POINT(1 2)'"),
        ],
    )
    def test_alias_delegates_to_st_function(self, name, target, arguments):
        self.load_function(name)
        alias_query = f"select {name}({arguments}) as alias from dual"
        target_query = f"select {target}({arguments}) as target from dual"
        alias_expression = f"{name}({arguments})"
        target_expression = f"{target}({arguments})"

        self._assert_same_result(alias_query, target_query)
        self._assert_same_sql_type(alias_expression, target_expression)
        self._assert_same_pyexasol_type(alias_query, target_query)
