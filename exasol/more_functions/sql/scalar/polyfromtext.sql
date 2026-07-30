-- [impl -> dsn~st-alias-functions~1]
create or replace function polyfromtext (val varchar(2000000)) return geometry
is
begin
    return st_polyfromtext (val);
end polyfromtext;
/
