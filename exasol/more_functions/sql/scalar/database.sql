-- [impl -> req~metadata-database-function~1]
create or replace function database ()
return varchar(128)
is
begin
    return current_schema;
end database;
/
