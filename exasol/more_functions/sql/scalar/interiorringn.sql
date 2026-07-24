-- [impl -> dsn~st-alias-functions~1]
create or replace function interiorringn (value geometry, index_value decimal(18,0)) return geometry is begin return st_interiorringn(value, index_value); end interiorringn;
/
