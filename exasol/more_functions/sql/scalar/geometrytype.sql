-- [impl -> dsn~st-alias-functions~1]
create or replace function geometrytype (value varchar(2000000)) return varchar(2000000) is begin return st_geometrytype(value); end geometrytype;
/
