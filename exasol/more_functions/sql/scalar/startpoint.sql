-- [impl -> dsn~st-alias-functions~1]
create or replace function startpoint (value varchar(2000000)) return varchar(2000000) is begin return st_startpoint(value); end startpoint;
/
