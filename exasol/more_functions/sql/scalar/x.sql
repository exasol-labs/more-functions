-- [impl -> dsn~st-alias-functions~1]
create or replace function x (value varchar(2000000)) return double is begin return st_x(value); end x;
/
