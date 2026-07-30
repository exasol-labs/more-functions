-- [impl -> dsn~st-alias-functions~1]
create or replace function numinteriorrings (val geometry) return decimal(18,0)
is
begin
    return st_numinteriorrings (val);
end numinteriorrings;
/
