-- [impl -> dsn~st-alias-functions~1]
create or replace function within (left_value geometry, right_value geometry) return boolean is begin return st_within(left_value, right_value); end within;
/
