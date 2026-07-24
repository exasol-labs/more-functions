-- [impl -> dsn~st-alias-functions~1]
create or replace function numinteriorrings (value varchar(2000000)) return decimal(18,0) is begin return st_numinteriorrings(value); end numinteriorrings;
/
