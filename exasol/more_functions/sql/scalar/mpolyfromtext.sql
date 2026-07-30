-- [impl -> dsn~st-alias-functions~1]
create or replace function mpolyfromtext (val varchar(2000000)) return geometry
is
begin
    return st_mpolyfromtext (val);
end mpolyfromtext;
/
