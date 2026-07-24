-- [impl -> dsn~st-alias-functions~1]
create or replace function isring (value varchar(2000000)) return boolean is begin return st_isring(value); end isring;
/
