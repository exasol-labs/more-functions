-- [impl -> dsn~st-alias-functions~1]
create or replace function y (val geometry) return double
is
begin
    return st_y (val);
end y;
/
