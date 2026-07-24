-- [impl -> dsn~st-alias-functions~1]
create or replace function issimple (value varchar(2000000)) return boolean is begin return st_issimple(value); end issimple;
/
