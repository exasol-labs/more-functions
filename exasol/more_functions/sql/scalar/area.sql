-- [impl -> dsn~area-function~1]
create or replace function area (val varchar(2000000))
return double
is
begin
    return st_area(val);
end area;
/
