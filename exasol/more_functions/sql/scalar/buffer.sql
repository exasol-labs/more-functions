-- [impl -> dsn~st-alias-functions~1]
create or replace function buffer (value varchar(2000000), distance double) return varchar(2000000) is begin return st_buffer(value, distance); end buffer;
/
