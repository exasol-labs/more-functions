-- [impl -> dsn~st-alias-functions~1]
create or replace function polyfromtext (value varchar(2000000)) return geometry is begin return st_polyfromtext(value); end polyfromtext;
/
