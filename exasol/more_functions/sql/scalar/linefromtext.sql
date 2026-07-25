-- [impl -> dsn~st-alias-functions~1]
create or replace function linefromtext (value varchar(2000000)) return geometry is begin return st_linefromtext(value); end linefromtext;
/
