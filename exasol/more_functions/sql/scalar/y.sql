-- [impl -> dsn~st-alias-functions~1]
create or replace function y (value varchar(2000000)) return double is begin return st_y(value); end y;
/
