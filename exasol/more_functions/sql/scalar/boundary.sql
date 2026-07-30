-- [impl -> dsn~st-alias-functions~1]
create or replace function boundary (val geometry) return geometry
is
begin
    return st_boundary (val);
end boundary;
/
