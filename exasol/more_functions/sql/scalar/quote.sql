-- [impl -> dsn~quote-function~1]
create or replace function quote (val varchar(2000000))
return varchar(2000000)
is
    res varchar(2000000);
begin
    -- [impl -> dsn~quote-null~1]
    -- [impl -> dsn~quote-empty-string~1]
    if val is null then
        res := 'NULL';
    -- [impl -> dsn~quote-non-empty-string~1]
    else
        res := '''' || replace(val, '''', '''''') || '''';
    end if;
    return res;
end quote;
/
