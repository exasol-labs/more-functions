-- [impl -> dsn~st-alias-functions~1]
create or replace function geometrytype (val geometry) return varchar(2000000)
is
begin
    return st_geometrytype (val);
end geometrytype;
/
