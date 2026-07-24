-- [impl -> dsn~st-alias-functions~1]
create or replace function equals (left_value varchar(2000000), right_value varchar(2000000)) return boolean is begin return st_equals(left_value, right_value); end equals;
/
