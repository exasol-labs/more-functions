-- [impl -> dsn~st-alias-functions~1]
create or replace function pointonsurface (value geometry) return geometry is begin return st_pointonsurface(value); end pointonsurface;
/
