-- [impl -> dsn~st-alias-functions~1]
create or replace function geomcollfromtext (val varchar(2000000)) return geometry
is
begin
    return st_geomcollfromtext (val);
end geomcollfromtext;
/
