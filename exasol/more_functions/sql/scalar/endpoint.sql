-- [impl -> dsn~st-alias-functions~1]
create or replace function endpoint (value geometry) return geometry is begin return st_endpoint(value); end endpoint;
/
