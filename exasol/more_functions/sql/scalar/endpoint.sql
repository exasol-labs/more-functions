-- [impl -> dsn~st-alias-functions~1]
create or replace function endpoint (val geometry) return geometry
is
begin
    return st_endpoint (val);
end endpoint;
/
