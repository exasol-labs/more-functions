-- [impl -> dsn~st-alias-functions~1]
create or replace function interiorringn (value varchar(2000000), index_value decimal(18,0)) return varchar(2000000) is begin return st_interiorringn(value, index_value); end interiorringn;
/
