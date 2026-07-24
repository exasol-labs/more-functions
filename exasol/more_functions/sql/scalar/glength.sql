-- [impl -> dsn~st-alias-functions~1]
create or replace function glength (value varchar(2000000)) return double is begin return st_length(value); end glength;
/
