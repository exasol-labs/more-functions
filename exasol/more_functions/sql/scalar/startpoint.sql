-- [impl -> dsn~st-alias-functions~1]
create or replace function startpoint (val geometry) return geometry
is
begin
    return st_startpoint (val);
end startpoint;
/
