-- [impl -> dsn~st-alias-functions~1]
create or replace function exteriorring (value geometry) return geometry is begin return st_exteriorring(value); end exteriorring;
/
