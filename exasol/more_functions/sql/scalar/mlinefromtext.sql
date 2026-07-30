-- [impl -> dsn~st-alias-functions~1]
create or replace function mlinefromtext (val varchar(2000000)) return geometry
is
begin
    return st_mlinefromtext (val);
end mlinefromtext;
/
