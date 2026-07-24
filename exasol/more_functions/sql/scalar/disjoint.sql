-- [impl -> dsn~st-alias-functions~1]
create or replace function disjoint (left_value geometry, right_value geometry) return boolean is begin return st_disjoint(left_value, right_value); end disjoint;
/
