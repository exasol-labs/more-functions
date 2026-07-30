-- [impl -> dsn~st-alias-functions~1]
create or replace function numpoints (val geometry) return decimal(18,0)
is
begin
    return st_numpoints (val);
end numpoints;
/
