-- [impl -> dsn~st-alias-functions~1]
create or replace function pointfromtext (val varchar(2000000)) return geometry
is
begin
    return st_pointfromtext (val);
end pointfromtext;
/
