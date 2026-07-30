-- [impl -> dsn~st-alias-functions~1]
create or replace function isring (val geometry) return boolean
is
begin
    return st_isring (val);
end isring;
/
