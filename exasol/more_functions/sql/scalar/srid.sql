-- [impl -> dsn~st-alias-functions~1]
create or replace function srid (value geometry) return decimal(18,0) is begin return st_srid(value); end srid;
/
