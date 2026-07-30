-- [impl -> dsn~st-alias-functions~1]
create or replace function multipointfromtext (val varchar(2000000)) return geometry
is
begin
    return st_multipointfromtext (val);
end multipointfromtext;
/
