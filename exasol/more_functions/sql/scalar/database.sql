create or replace function database ()
return varchar(128)
is
begin
    -- [impl -> dsn~database-returns-current-schema~1]
    return current_schema;
end database;
/
