-- [impl -> dsn~st-alias-functions~1]
create or replace function touches (left_value varchar(2000000), right_value varchar(2000000)) return boolean is begin return st_touches(left_value, right_value); end touches;
/
