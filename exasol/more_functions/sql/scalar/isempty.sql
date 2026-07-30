-- [impl -> dsn~st-alias-functions~1]
create or replace function isempty (val geometry) return boolean is
begin
    return st_isempty (val);
end isempty;
/
