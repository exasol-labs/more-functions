-- [impl -> dsn~st-alias-functions~1]
create or replace function area (val geometry)
return double
is
begin
    return st_area(val);
end area;
/
