-- [impl -> dsn~st-alias-functions~1]
create or replace function numgeometries (value geometry) return decimal(18,0) is begin return st_numgeometries(value); end numgeometries;
/
