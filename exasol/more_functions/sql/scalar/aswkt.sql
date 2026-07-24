-- [impl -> dsn~st-alias-functions~1]
create or replace function aswkt (value varchar(2000000)) return varchar(2000000) is begin return st_aswkt(value); end aswkt;
/
