-- [impl -> dsn~st-alias-functions~1]
create or replace function x (val geometry) return double
is
begin
    return st_x (val);
end x;
/
