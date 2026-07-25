-- [impl -> dsn~st-alias-functions~1]
create or replace function boundary (value geometry) return geometry is begin return st_boundary(value); end boundary;
/
