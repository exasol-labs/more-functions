-- [impl -> dsn~st-alias-functions~1]
create or replace function numgeometries (val geometry) return decimal(9,0)
is
begin
    return st_numgeometries(val);
end numgeometries;
/
