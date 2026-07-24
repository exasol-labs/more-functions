-- [impl -> dsn~st-alias-functions~1]
create or replace function crosses (left_value geometry, right_value geometry) return boolean is begin return st_crosses(left_value, right_value); end crosses;
/
