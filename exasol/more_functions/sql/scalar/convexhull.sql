-- [impl -> dsn~st-alias-functions~1]
create or replace function convexhull (val geometry) return geometry
is
begin
    return st_convexhull (val);
end convexhull;
/
