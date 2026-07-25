-- [impl -> dsn~st-alias-functions~1]
create or replace function startpoint (value geometry) return geometry is begin return st_startpoint(value); end startpoint;
/
