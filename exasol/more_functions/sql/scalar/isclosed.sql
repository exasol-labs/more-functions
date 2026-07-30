-- [impl -> dsn~st-alias-functions~1]
create or replace function isclosed (val geometry) return boolean
is
    begin return st_isclosed (val);
end isclosed;
/
