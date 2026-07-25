-- [impl -> dsn~st-alias-functions~1]
create or replace function geometryn (value geometry, index_value decimal(18,0)) return geometry is begin return st_geometryn(value, index_value); end geometryn;
/
