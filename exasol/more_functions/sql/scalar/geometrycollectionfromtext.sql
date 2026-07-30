-- [impl -> dsn~st-alias-functions~1]
create or replace function geometrycollectionfromtext (val varchar(2000000))return geometry
is
begin
    return st_geometrycollectionfromtext (val);
end geometrycollectionfromtext;
/
