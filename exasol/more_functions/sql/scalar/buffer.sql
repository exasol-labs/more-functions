-- [impl -> dsn~st-alias-functions~1]
create or replace function buffer (val geometry, distance double) return geometry
is
begin
    return st_buffer(val, distance);
end buffer;
/
