-- [impl -> dsn~st-alias-functions~1]
create or replace function x (value geometry) return double is begin return st_x(value); end x;
/
