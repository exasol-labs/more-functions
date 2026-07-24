-- [impl -> dsn~st-alias-functions~1]
create or replace function buffer (value geometry, distance double) return geometry is begin return st_buffer(value, distance); end buffer;
/
