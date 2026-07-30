-- [impl -> dsn~st-alias-functions~1]
create or replace function linestringfromtext (val varchar(2000000)) return geometry
is
begin
    return st_linestringfromtext (val);
end linestringfromtext;
/
