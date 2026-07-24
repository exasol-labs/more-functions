-- [impl -> dsn~st-alias-functions~1]
create or replace function contains (left_value varchar(2000000), right_value varchar(2000000)) return boolean is begin return st_contains(left_value, right_value); end contains;
/
