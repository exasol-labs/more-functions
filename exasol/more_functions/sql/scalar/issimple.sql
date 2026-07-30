-- [impl -> dsn~st-alias-functions~1]
create or replace function issimple (val geometry) return boolean
is
begin
    return st_issimple (val);
end issimple;
/
