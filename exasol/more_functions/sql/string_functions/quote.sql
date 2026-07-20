create or replace function quote (val varchar(2000000))
return varchar(2000000)
is
    res varchar(2000000);
begin
    if val is null then
        res := 'NULL';
    else
        res := '''' || regexp_replace(val, '(''|\|\x00|\x1a)', '\\\1') || '''';
    end if;
    return res;
end quote;
/
