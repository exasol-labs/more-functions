-- [impl -> dsn~st-alias-functions~1]
create or replace function issimple (value geometry) return boolean is begin return st_issimple(value); end issimple;
/
