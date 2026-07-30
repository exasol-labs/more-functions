-- [impl -> dsn~st-alias-functions~1]
create or replace function intersects (left_value geometry, right_value geometry) return boolean
is
begin
    return st_intersects(left_value, right_value);
end intersects;
/
