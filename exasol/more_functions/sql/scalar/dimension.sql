-- [impl -> dsn~st-alias-functions~1]
create or replace function dimension (val geometry) return decimal(9,0)
is
begin
    return st_dimension(val);
end dimension;
/
