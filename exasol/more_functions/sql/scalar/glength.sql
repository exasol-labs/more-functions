-- [impl -> dsn~st-alias-functions~1]
create or replace function glength (value geometry) return double is begin return st_length(value); end glength;
/
