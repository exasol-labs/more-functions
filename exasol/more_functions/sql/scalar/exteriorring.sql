-- [impl -> dsn~st-alias-functions~1]
create or replace function exteriorring (val geometry) return geometry
is
begin
    return st_exteriorring (val);
end exteriorring;
/
