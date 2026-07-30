-- [impl -> dsn~st-alias-functions~1]
create or replace function interiorringn (val geometry, index_value decimal(18,0)) return geometry
is
begin
    return st_interiorringn(val, index_value);
end interiorringn;
/
