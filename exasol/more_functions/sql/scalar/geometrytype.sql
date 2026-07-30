-- [impl -> dsn~st-alias-functions~1]
create or replace function geometrytype (val geometry) return varchar(18) ascii
is
begin
    return st_geometrytype(val);
end geometrytype;
/
