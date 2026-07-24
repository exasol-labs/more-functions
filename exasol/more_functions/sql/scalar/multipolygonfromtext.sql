-- [impl -> dsn~st-alias-functions~1]
create or replace function multipolygonfromtext (value varchar(2000000)) return geometry is begin return st_multipolygonfromtext(value); end multipolygonfromtext;
/
