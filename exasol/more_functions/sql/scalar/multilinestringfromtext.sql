-- [impl -> dsn~st-alias-functions~1]
create or replace function multilinestringfromtext (val varchar(2000000)) return geometry
is
begin
    return st_multilinestringfromtext (val);
end multilinestringfromtext;
/
