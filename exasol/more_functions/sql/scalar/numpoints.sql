-- [impl -> dsn~st-alias-functions~1]
create or replace function numpoints (value geometry) return decimal(18,0) is begin return st_numpoints(value); end numpoints;
/
