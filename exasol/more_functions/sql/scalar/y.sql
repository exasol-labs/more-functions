-- [impl -> dsn~st-alias-functions~1]
create or replace function y (value geometry) return double is begin return st_y(value); end y;
/
