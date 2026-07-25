-- [impl -> dsn~st-alias-functions~1]
create or replace function centroid (value geometry) return geometry is begin return st_centroid(value); end centroid;
/
