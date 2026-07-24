-- [impl -> dsn~st-alias-functions~1]
create or replace function convexhull (value geometry) return geometry is begin return st_convexhull(value); end convexhull;
/
