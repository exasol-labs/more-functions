-- [impl -> dsn~st-alias-functions~1]
create or replace function isring (value geometry) return boolean is begin return st_isring(value); end isring;
/
