-- [impl -> dsn~st-alias-functions~1]
create or replace function centroid (val geometry) return geometry
is
begin
    return st_centroid (val);
end centroid;
/
