-- [impl -> dsn~st-alias-functions~1]
create or replace function isclosed (value geometry) return boolean is begin return st_isclosed(value); end isclosed;
/
