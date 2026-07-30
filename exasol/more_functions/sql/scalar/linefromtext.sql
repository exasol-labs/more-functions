-- [impl -> dsn~st-alias-functions~1]
create or replace function linefromtext (val varchar(2000000)) return geometry
is
begin
    return st_linefromtext (val);
end linefromtext;
/
