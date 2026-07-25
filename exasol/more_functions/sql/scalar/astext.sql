-- [impl -> dsn~st-alias-functions~1]
create or replace function astext (value geometry) return varchar(2000000) is begin return st_astext(value); end astext;
/
