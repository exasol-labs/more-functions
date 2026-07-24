-- [impl -> dsn~st-alias-functions~1]
create or replace function geomfromtext (value varchar(2000000)) return geometry is begin return st_geomfromtext(value); end geomfromtext;
/
