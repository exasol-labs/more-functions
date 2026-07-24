-- [impl -> dsn~st-alias-functions~1]
create or replace function isclosed (value varchar(2000000)) return boolean is begin return st_isclosed(value); end isclosed;
/
