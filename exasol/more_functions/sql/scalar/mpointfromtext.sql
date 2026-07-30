-- [impl -> dsn~st-alias-functions~1]
create or replace function mpointfromtext (val varchar(2000000)) return geometry
is
begin
    return st_mpointfromtext (val);
end mpointfromtext;
/
