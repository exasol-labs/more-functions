-- [impl -> dsn~st-alias-functions~1]
create or replace function equals (left_value geometry, right_value geometry) return boolean
is
begin
    return st_equals(left_value, right_value);
end equals;
/
