-- [impl -> dsn~st-alias-functions~1]
create or replace function touches (left_value geometry, right_value geometry) return boolean
is
begin
    return st_touches(left_value, right_value);
end touches;
/
