-- [impl -> dsn~st-alias-functions~1]
create or replace function isempty (value geometry) return boolean is begin return st_isempty(value); end isempty;
/
