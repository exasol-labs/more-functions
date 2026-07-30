-- [impl -> dsn~st-alias-functions~1]
create or replace function polygonfromtext (val varchar(2000000)) return geometry
is
begin
    return st_polygonfromtext (val);
end polygonfromtext;
/
