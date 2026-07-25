-- [impl -> dsn~st-alias-functions~1]
create or replace function polygonfromtext (value varchar(2000000)) return geometry is begin return st_polygonfromtext(value); end polygonfromtext;
/
