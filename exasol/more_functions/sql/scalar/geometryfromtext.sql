-- [impl -> dsn~st-alias-functions~1]
create or replace function geometryfromtext (val varchar(2000000)) return geometry
is
begin
    return st_geometryfromtext (val);
    end geometryfromtext;
/
