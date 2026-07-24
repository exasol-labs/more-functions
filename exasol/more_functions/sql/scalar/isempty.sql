-- [impl -> dsn~st-alias-functions~1]
create or replace function isempty (value varchar(2000000)) return boolean is begin return st_isempty(value); end isempty;
/
