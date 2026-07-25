-- [impl -> dsn~st-alias-functions~1]
create or replace function envelope (value geometry) return geometry is begin return st_envelope(value); end envelope;
/
