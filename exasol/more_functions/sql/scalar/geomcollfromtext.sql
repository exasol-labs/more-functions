-- [impl -> dsn~st-alias-functions~1]
create or replace function geomcollfromtext (value varchar(2000000)) return geometry is begin return st_geomcollfromtext(value); end geomcollfromtext;
/
