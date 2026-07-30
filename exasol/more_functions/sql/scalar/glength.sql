-- [impl -> dsn~st-alias-functions~1]
create or replace function glength (val geometry) return double
is
begin
    return st_length (val);
end glength;
/
