-- [impl -> dsn~st-alias-functions~1]
create or replace function envelope (val geometry) return geometry
is
begin
    return st_envelope (val);
end envelope;
/
