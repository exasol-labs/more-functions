from test.integration.more_functions.scalar_function_test_base import (
    ScalarFunctionTestBase,
)

import pytest


# [itest -> dsn~st-alias-functions~1]
class TestStAliases(ScalarFunctionTestBase):
    @pytest.mark.parametrize(
        "name, target, arguments",
        [
            ("astext", "st_astext", "'POINT(1 2)'"),
            ("aswkt", "st_aswkt", "'POINT(1 2)'"),
            ("boundary", "st_boundary", "'POLYGON((0 0,0 1,1 1,1 0,0 0))'"),
            ("buffer", "st_buffer", "'POINT(1 2)', 1.0"),
            ("centroid", "st_centroid", "'POLYGON((0 0,0 1,1 1,1 0,0 0))'"),
            ("convexhull", "st_convexhull", "'MULTIPOINT((0 0),(1 1))'"),
            (
                "contains",
                "st_contains",
                "'POLYGON((0 0,0 2,2 2,2 0,0 0))', 'POINT(1 1)'",
            ),
            ("crosses", "st_crosses", "'LINESTRING(0 0,2 2)', 'LINESTRING(0 2,2 0)'"),
            ("dimension", "st_dimension", "'POINT(1 2)'"),
            ("disjoint", "st_disjoint", "'POINT(0 0)', 'POINT(1 1)'"),
            ("endpoint", "st_endpoint", "'LINESTRING(0 0,1 1)'"),
            ("envelope", "st_envelope", "'POINT(1 2)'"),
            ("exteriorring", "st_exteriorring", "'POLYGON((0 0,0 1,1 1,1 0,0 0))'"),
            ("equals", "st_equals", "'POINT(1 2)', 'POINT(1 2)'"),
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
            (
                "overlaps",
                "st_overlaps",
                "'POLYGON((0 0,0 2,2 2,2 0,0 0))', 'POLYGON((1 1,1 3,3 3,3 1,1 1))'",
            ),
            ("pointonsurface", "st_pointonsurface", "'POLYGON((0 0,0 1,1 1,1 0,0 0))'"),
            ("pointn", "st_pointn", "'LINESTRING(0 0,1 1)', 1"),
            ("startpoint", "st_startpoint", "'LINESTRING(0 0,1 1)'"),
            ("srid", "st_srid", "'POINT(1 2)'"),
            ("touches", "st_touches", "'POINT(0 0)', 'LINESTRING(0 0,1 1)'"),
            ("within", "st_within", "'POINT(1 1)', 'POLYGON((0 0,0 2,2 2,2 0,0 0))'"),
            ("x", "st_x", "'POINT(1 2)'"),
            ("y", "st_y", "'POINT(1 2)'"),
        ],
    )
    def test_alias_delegates_to_st_function(self, name, target, arguments):
        self.load_function(name)
        self.assert_query(
            f"select {name}({arguments}) = {target}({arguments})",
            True,
        )
        alias_metadata = self.connection.execute(
            f"select {name}({arguments}) from dual"
        ).columns()
        target_metadata = self.connection.execute(
            f"select {target}({arguments}) from dual"
        ).columns()
        assert (
            next(iter(alias_metadata.values()))["type"]
            == next(iter(target_metadata.values()))["type"]
        )
